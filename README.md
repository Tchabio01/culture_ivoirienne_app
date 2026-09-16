# 🇨🇮 Culture Ivoirienne App

Une application éducative et interactive pour découvrir, préserver et partager la richesse culturelle de la Côte d’Ivoire.  
Elle propose des proverbes, des contes, des recettes, de la musique, des événements et un quiz pour tester ses connaissances.

---

## ✨ Fonctionnalités

- 📜 **Traditions** : proverbes et contes ivoiriens
- 🍲 **Gastronomie** : plats typiques (Attiéké, Foutou, Garba, etc.)
- 🎶 **Musique** : playlist d’artistes emblématiques (Magic System, Alpha Blondy, DJ Arafat…)
- 🎭 **Événements** : festivals et carnavals (FEMUA, Popo Carnaval, Festival des Masques…)
- 🧩 **Quiz éducatif** : tester ses connaissances sur la culture ivoirienne
- 🔐 **Sécurité** : authentification avec mot de passe haché et token JWT
- 🗄️ **Base de données SQLite** : stockage des proverbes, recettes et événements
- 🌐 **API Flask** : accès aux données via endpoints REST

---

## ⚙️ Installation

### Prérequis
- Python 3.10+
- Termux ou environnement Linux
- Git
- Pip

### Étapes
```bash
# Cloner le dépôt
git clone https://github.com/Tchabio01/culture_ivoirienne_app.git
cd culture_ivoirienne_app

# Installer les dépendances
pip install -r requirements.txt

# Lancer l’application
python main.py
