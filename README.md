[![Version française](https://img.shields.io/badge/Lire%20en-Fran%C3%A7ais-blue?style=for-the-badge&logo=appveyor)](https://github.com/Andor-py/PolyBius/blob/main/README-fr.md)



# Polybius v1.9.11
### A powerful Discord Selfbot written in Python using [discord.py-self](https://github.com/dolfies/discord.py-self)!

<div align="center">
  <img src="https://i.imgur.com/EPJaixO.png" alt="icon" width="50%" height="50%">

 
</div>

<div align="center">

  ## ⛔ Disclaimer
  **Discord SelfBots are not allowed by Discord TOS and can easily ban your account. Please use for educational purposes only. This project is just a proof of concept.**
</div>

## 📖 Table of content
1. [💾 Installation](https://github.com/Andor-py/PolyBius?tab=readme-ov-file#-installation)
2. [🔧 Config](https://github.com/Andor-py/PolyBius?tab=readme-ov-file#-config)
3. [🌟 Features](https://github.com/Andor-py/PolyBius?tab=readme-ov-file#-features)
4. [📜 How to get a user token](https://github.com/Andor-py/PolyBius?tab=readme-ov-file#-how-to-get-a-user-token)
5. [👀 Preview](https://github.com/Andor-py/PolyBius?tab=readme-ov-file#-preview)
6. [☣️ Issues](https://github.com/Andor-py/PolyBius?tab=readme-ov-file#%EF%B8%8F-issues)
7. [🛠️ Developement version](https://github.com/Andor-py/PolyBius#%EF%B8%8F-developement-version)
8. [❓ How to contribute](https://github.com/Andor-py/PolyBius#-how-to-contribute)
9. [⭐ Contributors](https://github.com/Andor-py/PolyBius?tab=readme-ov-file#-contributors)
10. [🫂 Support](https://github.com/Andor-py/PolyBius?tab=readme-ov-file#support)

## 💾 Installation
1. Download the latest version from the [Releases](https://github.com/Andor-py/PolyBius/releases) section on GitHub.
2. Make sure to have [Python](https://www.python.org/downloads/ "Install Python here") installed.
3. Open your Terminal and go to Nuclear with `cd`.
4. Install dependencies: `pip install -r requirements.txt`
5. Run the program: `python main.py`
6. Get started !

## 🔧 Config
Open `config_selfbot.py` with any text editor  and enter a [user token](https://github.com/Andor-py/PolyBius?tab=readme-ov-file#-how-to-get-a-user-token).

## 🌟 Features
* Voice commands,
* Raid commands,
* Massive DM (DM All),
* Auto xp,
* Nitro Sniper,
* Spam and Flood command,
* Snipe command,
* Auto bump,
* Alt Account Setup,
* And others!

## 📜 How to get a user token
1. Go to [Discord Web](https://discord.com/app)
2. Do ``CTRL + MAJ + I`` and go to `Console`
3. Paste this code:
```js
window.webpackChunkdiscord_app.push([
  [Math.random()],
  {},
  req => {
    if (!req.c) return;
    for (const m of Object.keys(req.c)
      .map(x => req.c[x].exports)
      .filter(x => x)) {
      if (m.default && m.default.getToken !== undefined) {
        return copy(m.default.getToken());
      }
      if (m.getToken !== undefined) {
        return copy(m.getToken());
      }
    }
  },
]);
console.log('%cWorked!', 'font-size: 50px');
console.log(`%cYou now have your token in the clipboard!`, 'font-size: 16px');
```
Now your token is in your clipboard. <br><br>
3b. If you can't paste the code, just type `allow pasting` and retry. <br>
<br>
4. Paste your token in `config_selfbot.py`

## 👀 Preview
<div align="center">
  <img src="https://i.imgur.com/RVhkwXC.png" alt="preview" width="" height="">
</div>


<br>

## ☣️ Issues
### Library Issues
`discord.py-self` has some issues.
<br>

One of the most common is when an incompatible library is already installed. To solve this problem, you can uninstall them:
```powershell
pip uninstall discord discord.py py-cord pycord nextcord discord.py-self aiohttp
```
And now, you just need to re-install discord.py-self (from Git or from [here](https://github.com/Andor-py/PolyBius/releases/latest))

If you still get an error, you can check [discord.py-self's support](https://t.me/dpy_self_discussions)
### Nuclear's issues
Check [support](https://github.com/Andor-py/PolyBius?tab=readme-ov-file#support)!

## 🛠️ Developement version
1. Open your Terminal and go to the wanted folder with `cd`.
2. Clone the repository: `git clone https://github.com/Andor-py/PolyBius`
**or**
Just clone it with the green "Code" button above the README.


## ❓ How to contribute

🖤 You can't . <br>


## ⭐ Contributors
<table align="center">
  <tr>
    <td align="center">
      <a href="https://github.com/Sitois">
        <img src="https://avatars.githubusercontent.com/u/143238636?v=4" alt="Sitois" width="80px" height="80px" style="border-radius: 50%;">
        <br>
        Sitois
      </a>
    </td>
<table>

A big thank to [Sitois](https://github.com/Sitois) for the code of Nuclear and for learning me a bit of Python ;-; ! Check her current [project](https://github.com/Sitois/Nuclear-V2)!

# Support
* we don't have any suport ^^

<br>

---

[![](https://visitcount.itsvg.in/api?id=ANDOR&label=Repos%20Views&color=12&icon=5&pretty=true)](https://visitcount.itsvg.in)

---
Nuclear-V1 By sitois: [![wakatime](https://wakatime.com/badge/user/018af69f-9d50-4699-932d-026a9efb0401/project/018d13ec-4c15-459c-b9a8-e02089e7681b.svg)](https://wakatime.com/badge/user/018af69f-9d50-4699-932d-026a9efb0401/project/018d13ec-4c15-459c-b9a8-e02089e7681b)

Nuclear-V2 By sitois: [![wakatime](https://wakatime.com/badge/user/018af69f-9d50-4699-932d-026a9efb0401/project/018e9e0c-29ce-4e43-9113-34945236a808.svg)](https://wakatime.com/badge/user/018af69f-9d50-4699-932d-026a9efb0401/project/018e9e0c-29ce-4e43-9113-34945236a808)

My total Code Time: about 3 day ...
