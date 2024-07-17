import random, string, os, json, asyncio

import discord

from .logger import log

def generate_random_string(length):
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for _ in range(length))

def random_cooldown(minimum, maximum):
      return 1


async def save_guild(guild: discord.Guild, channels):
    """Save the given guild into ./backups/guild_id.json"""

    log.separate_text("CREATING BACKUP")
    guild_info = {
        "id": guild.id,
        "name": guild.name,
        "roles": [],
        "categories": [],
        "channels": []
    }

    # Save guild's roles
    for role in guild.roles:
        if not role.is_integration() and role != guild.default_role:
            guild_info["roles"].append({
                "id": role.id,
                "name": role.name,
                "permissions": role.permissions.value,
                "color": role.color.value,
                "mentionable": role.mentionable,
                "hoist": role.hoist,
                "position": role.position  # Save the position of the role
            })
            log.success(f"Successfully saved role: {role.name}({role.id}) from {guild.name}({guild.id}).")

    # Save @everyone's permissions
    guild_info["default_role"] = {
        "permissions": guild.default_role.permissions.value
    }
    log.success(f"Successfully saved @everyone role from {guild.name}({guild.id}).")

    # Save guild's categories
    for category in guild.categories:
        guild_info["categories"].append({
            "id": category.id,
            "name": category.name,
            "position": category.position
        })
        log.success(f"Successfully saved category: {category.name}({category.id}) from {guild.name}({guild.id}).")

    # Save guild's channels
    for channel in channels:
        channel_info = {
            "id": channel.id,
            "name": channel.name,
            "type": str(channel.type),
            "position": channel.position,
            "category": channel.category_id,
            "permissions": []
        }
        log.success(f"Successfully saved channel: {channel.name}({channel.id}) from {guild.name}({guild.id}).")

        # Save channel's permissions, excluding user permissions
        for overwrite in channel.overwrites:
            if isinstance(overwrite, discord.Role) or overwrite == guild.default_role:
                allow, deny = channel.overwrites[overwrite].pair()
                channel_info["permissions"].append({
                    "id": overwrite.id,
                    "type": "role" if isinstance(overwrite, discord.Role) else "@everyone",
                    "allow": allow.value,
                    "deny": deny.value
                })
        log.success(f"Successfully saved role permissions for {channel.name}({channel.id}) from {guild.name}({guild.id}).")

        guild_info["channels"].append(channel_info)

    # Check if backups folder exists
    if not os.path.exists("backups"):
        os.makedirs("backups")
        log.alert("Created the 'backups' folder!")

    # Save guild's infos in a json file
    with open(f"./backups/{guild.id}.json", "w") as f:
        json.dump(guild_info, f, indent=4)

    log.success(f"Successfully saved guild: {guild.name}({guild.id}).")
    log.separate("CREATING BACKUP")



async def load_guild(guild: discord.Guild,
                     channels,
                     backup,
                     minimal_cooldown,
                     maximum_cooldown):
    """Load the given guild into the chosen guild."""
    log.separate_text("LOADING BACKUP")
    # Delete old channels
    for channel in channels:
        try:
            await channel.delete()
            log.success(f"Successfully deleted channel: {channel.name}({channel.id}) for {guild.name}({guild.id}).")
            await asyncio.sleep(random_cooldown(0.6, 12.9))  # Wait to avoid rate limit
        except Exception as e:
            log.fail(f"Error while trying to delete channel: {channel.name}({channel.id}): {e}")

    # Delete old roles (not @everyone, not bot roles)
    for role in guild.roles:
        if role.name != "@everyone" and not role.is_integration():
            try:
                await role.delete()
                log.success(f"Successfully deleted role: {role.name}({role.id}) for {guild.name}({guild.id}).")
                await asyncio.sleep(random_cooldown(0.4, 13.6))  # Wait to avoid rate limit
            except Exception as e:
                log.fail(f"Error while trying to delete role: {role.name}: {e}")

    # Delete old categories
    for category in guild.categories:
        try:
            await category.delete()
            log.success(f"Successfully deleted category: {category.name}({category.id}) for {guild.name}({guild.id}).")
            await asyncio.sleep(random_cooldown(0.8, 14.2))  # Wait to avoid rate limit
        except Exception as e:
            log.fail(f"Error while trying to delete category: {role.name}: {e}")

    # Add backup's roles
    role_map = {}
    for role_info in backup["roles"]:
        new_role = await guild.create_role(
            name=role_info["name"],
            permissions=discord.Permissions(role_info["permissions"]),
            color=discord.Color(role_info["color"]),
            mentionable=role_info["mentionable"],
            hoist=role_info["hoist"]
        )
        role_map[role_info["id"]] = new_role
        log.success(f"Successfully created role: {role_info['name']}({role_info['id']}) for {guild.name}({guild.id}).")
        await asyncio.sleep(random_cooldown(minimal_cooldown, maximum_cooldown))  # Wait to avoid rate limit

    # Adjust role positions
    for role_info in backup["roles"]:
        role = role_map.get(role_info["id"])
        if role:
            await role.edit(position=role_info["position"])
            log.success(f"Successfully adjusted position for role: {role_info['name']}({role_info['id']}) for {guild.name}({guild.id}).")
            await asyncio.sleep(random_cooldown(minimal_cooldown, maximum_cooldown))  # Wait to avoid rate limit

    # Add backup's categories
    category_map = {}
    for category_info in backup["categories"]:
        new_category = await guild.create_category(
            name=category_info["name"],
            position=category_info["position"]
        )
        category_map[category_info["id"]] = new_category.id
        log.success(f"Successfully created category: {category_info['name']}({category_info['id']}) for {guild.name}({guild.id}).")
        await asyncio.sleep(random_cooldown(minimal_cooldown, maximum_cooldown))  # Wait to avoid rate limit

    # Add backup's channels
    for channel_info in backup["channels"]:
        overwrites = {}
        for perm in channel_info["permissions"]:
            target = guild.get_role(perm["id"]) if perm["type"] == "role" else guild.default_role
            if target:
                overwrites[target] = discord.PermissionOverwrite.from_pair(
                    discord.Permissions(perm["allow"]),
                    discord.Permissions(perm["deny"])
                )

        category = guild.get_channel(category_map[channel_info["category"]]) if channel_info["category"] else None
        channel_type = discord.ChannelType.text if channel_info["type"] == "text" else discord.ChannelType.voice
        if channel_type == discord.ChannelType.text:
            await guild.create_text_channel(
                name=channel_info["name"],
                position=channel_info["position"],
                overwrites=overwrites,
                category=category
            )
        else:
            await guild.create_voice_channel(
                name=channel_info["name"],
                position=channel_info["position"],
                overwrites=overwrites,
                category=category
            )
        log.success(f"Successfully created channel: {channel_info['name']}({channel_info['id']}) for {guild.name}({guild.id}).")
        await asyncio.sleep(random_cooldown(minimal_cooldown, maximum_cooldown))  # Wait to avoid rate limit

    # Set backup's @everyone permissions
    await guild.default_role.edit(permissions=discord.Permissions(backup["default_role"]["permissions"]))
    log.success(f"Successfully set @everyone permissions to: {backup['default_role']['permissions']} for {guild.name}({guild.id}).")

    log.success(f"Successfully loaded backup: {backup['name']}({backup['id']}) to {guild.name}({guild.id}).")
    log.separate("CREATING BACKUP")