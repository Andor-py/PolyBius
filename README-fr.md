Voici la traduction du fichier read.me en français :


# Polybius
### Un Selfbot Discord puissant écrit en Python utilisant [discord.py-self](https://github.com/dolfies/discord.py-self) !

<div align="center">
  <img src="https://i.imgur.com/EPJaixO.png" alt="icon" width="50%" height="50%">
</div>

<div align="center">

  ## ⛔ Avertissement
  **Les SelfBots Discord ne sont pas autorisés par les CGU de Discord et peuvent facilement entraîner la suspension de votre compte. Veuillez les utiliser uniquement à des fins éducatives. Ce projet est juste une preuve de concept.**
</div>

## 📖 Table des matières
1. [💾 Installation](https://github.com/Andor-py/PolyBius?tab=readme-ov-file#-installation)
2. [🔧 Configuration](https://github.com/Andor-py/PolyBius?tab=readme-ov-file#-config)
3. [🌟 Fonctionnalités](https://github.com/Andor-py/PolyBius?tab=readme-ov-file#-features)
4. [📜 Comment obtenir un token utilisateur](https://github.com/Andor-py/PolyBius?tab=readme-ov-file#-how-to-get-a-user-token)
5. [👀 Aperçu](https://github.com/Andor-py/PolyBius?tab=readme-ov-file#-preview)
6. [☣️ Problèmes](https://github.com/Andor-py/PolyBius?tab=readme-ov-file#%EF%B8%8F-issues)
7. [🛠️ Version de développement](https://github.com/Andor-py/PolyBius#%EF%B8%8F-developement-version)
8. [❓ Comment contribuer](https://github.com/Andor-py/PolyBius#-how-to-contribute)
9. [⭐ Contributeurs](https://github.com/Andor-py/PolyBius?tab=readme-ov-file#-contributors)
10. [🫂 Support](https://github.com/Andor-py/PolyBius?tab=readme-ov-file#support)

## 💾 Installation
1. Téléchargez la dernière version depuis la section [Releases](https://github.com/Andor-py/PolyBius/releases) sur GitHub.
2. Assurez-vous d'avoir [Python](https://www.python.org/downloads/ "Installez Python ici") installé.
3. Ouvrez votre terminal et allez dans le répertoire Nuclear avec `cd`.
4. Installez les dépendances : `pip install -r requirements.txt`
5. Lancez le programme : `python main.py`
6. C'est parti !

## 🔧 Configuration
Ouvrez `config_selfbot.py` avec n'importe quel éditeur de texte et entrez un [token utilisateur](https://github.com/Andor-py/PolyBius?tab=readme-ov-file#-how-to-get-a-user-token).

## 🌟 Fonctionnalités
* Commandes vocales,
* Commandes de raid,
* DM massif (DM à tous),
* Auto xp,
* Nitro Sniper,
* Commande de spam et de flood,
* Commande de snipe,
* Auto bump,
* Configuration de compte secondaire,
* Et bien d'autres !

## 📜 Comment obtenir un token utilisateur
1. Allez sur [Discord Web](https://discord.com/app)
2. Faites ``CTRL + MAJ + I`` et allez dans `Console`
3. Collez ce code :
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
Votre token est maintenant dans votre presse-papiers. <br><br>
3b. Si vous ne pouvez pas coller le code, tapez simplement `allow pasting` et réessayez. <br>
<br>
4. Collez votre token dans `config_selfbot.py`

## 👀 Aperçu
<div align="center">
  <img src="https://imgur.com/a/HysZTxt.png" alt="aperçu" width="" height="">
</div>

<br>

## ☣️ Problèmes
### Problèmes de bibliothèque
`discord.py-self` a quelques problèmes.
<br>

L'un des plus courants est lorsqu'une bibliothèque incompatible est déjà installée. Pour résoudre ce problème, vous pouvez les désinstaller :
```powershell
pip uninstall discord discord.py py-cord pycord nextcord discord.py-self aiohttp
```
Et maintenant, vous devez simplement réinstaller discord.py-self (depuis Git ou depuis [ici](https://github.com/Andor-py/PolyBius/releases/latest))

Si vous obtenez toujours une erreur, vous pouvez vérifier le [support de discord.py-self](https://t.me/dpy_self_discussions)
### Problèmes de Nuclear
Vérifiez [le support](https://github.com/Andor-py/PolyBius?tab=readme-ov-file#support) !

## 🛠️ Version de développement
1. Ouvrez votre terminal et allez dans le dossier souhaité avec `cd`.
2. Clonez le dépôt : `git clone https://github.com/Andor-py/PolyBius`
**ou**
Clonez-le simplement avec le bouton vert "Code" au-dessus du README.

## ❓ Comment contribuer

🖤 Vous ne pouvez pas. <br>

## ⭐ Contributeurs
<table align="center">
  <tr>
    <td align="center">
      <a href="https://github.com/Sitois">
        <img src="https://avatars.githubusercontent.com/u/143238636?v=4" alt="Sitois" width="80px" height="80px" style="border-radius: 50%;">
        <br>
        Sitois
      </a>
    </td>
  </tr>
</table>

Un grand merci à [Sitois](https://github.com/Sitois) pour le code de Nuclear et pour m'avoir appris un peu de Python ;-; ! Consultez son projet actuel [ici](https://github.com/Sitois/Nuclear-V2) !

# Support
* nous n'avons pas de support ^^

<br>

---

[![](https://visitcount.itsvg.in/api?id=Nuclear&label=Repo%20Views&color=2&icon=5&pretty=false)](https://visitcount.itsvg.in)

---
Nuclear-V1 Par sitois : [![wakatime](https://wakatime.com/badge/user/018af69f-9d50-4699-932d-026a9efb0401/project/018d13ec-4c15-459c-b9a8-e02089e7681b.svg)](https://wakatime.com/badge/user/018af69f-9d50-4699-932d-026a9efb0401/project/018d13ec-4c15-459c-b9a8-e02089e7681b)

Nuclear-V2 Par sitois : [![wakatime](https://wakatime.com/badge/user/018af69f-9d50-4699-932d-026a9efb0401/project/018e9e0c-29ce-4e43-9113-34945236a808.svg)](https://wakatime.com/badge/user/018af69f-9d50-4699-932d-026a9efb0401/project/018e9e0c-29ce-4e43-9113-34945236a808)

Mon temps total de code : environ 3 jours ...
