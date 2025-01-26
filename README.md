# Projet DeskCore 26/01/2025

**Requis :**

- Python >= 3.10  
- CustomTkinter >= 5.1.2  

**Infos à savoir :**  
Les personnes sur le projet :  
- **GIRARDIN Tristan** (ryno57/lothevy sur GitHub)  
- **HOUSSEMAND Lucas** (KaitoT sur GitHub)  
- **LUTZ-SBARAGLI Nolan** (Nopox57/Nolan sur GitHub)  

Pour installer CustomTkinter, faites cette commande dans le terminal :  

`pip install customtkinter`


Documentation CustomTkinter : [cliquez ici](https://customtkinter.tomschimansky.com/documentation/)

Notre projet, DeskCore, est un logiciel servant de **"Hub d'applications"**. Par "applications", nous faisons référence principalement à des logiciels tiers intégrés.

### Exemples d'applications prévues :  
- Logiciel de notes  
- Logiciel de monitoring de logiciels/jeux/PC  
- Logiciel d'agenda/horloge  
- Logiciel d'enregistrement d'écran (screen, record, etc.)  
- Logiciel de conversion d'extensions  
- Etc...

### Nos objectifs en cours(+voir [issue sur le github](https://github.com/ryno57/ProjetNSI/issues)) :
- Implémenter un gestionnaire de thèmes  
- Finaliser l'application Notes  
- Corriger les problèmes liés à la compatibilité Linux  

Pour lancer DeskCore, ouvrez le fichier `DeskCore.py`, qui se trouve normalement dans `/Scripts/DeskCore.py`.

---

## **Structure :**  

### Ressources :  
- **Images :**  
  - `exemple.png`  
- **Icones :**  
  - `exemple.ico`  

### Scripts :  
- `DeskCore.py` : Le code principal qui gère l'ensemble du projet.  
- `dkce_extension.py` : Permet d'enregistrer des fichiers sous l'extension `.dkce` (DeskCore Extension).  
- `NomDuneFonctionnalité_app.py` : Les fichiers avec le suffixe `_app` correspondent aux applications tierces intégrées.  

### Autres fichiers :  
- `LICENCE` : terms & conditions be like.  
- `README.md` : Ce document là.  

---

# **DeskCore.py**

C'est le fichier principal du projet. En résumé, il constitue la base du logiciel, comme le tronc d'un arbre, reliant toutes les autres fonctionnalités (les branches). Sans lui, rien ne fonctionne.  

### **Importation de CustomTkinter :**  
CustomTkinter est importé sous `ctk`, pour rendre le code plus lisible et rapide à écrire (vous nours remercierez +tard). Dans la documentation, n’oubliez pas que nous utilisons `ctk` au lieu de `customtkinter` pour appeler les fonctionnalités.  

### **Initialisation :**  
Une variable `app` est utilisée pour créer la fenêtre principale. Ensuite, trois méthodes permettent de :  
1. Définir un titre.  
2. Configurer la résolution de la fenêtre.  
3. Rendre la fenêtre non redimensionnable (provisoirement, pour éviter les problèmes).  

Le reste concerne l'interface visuelle (boutons, frames, etc...).  

### **Affectation :**  
Les différents boutons permettent souvent d'appeller des méthodes spécifiques.  

Par exemple :  
- la méthode `show_settings` ouvre les paramètres. Elle contient quelques réglages en exemples. On risque de bouger les paramètres dans un fichier pytohn à part car sinon ca deviendra encombrant.

---

# **Notes_app.py**

Ce fichier gère l'application Notes, appelée par `DeskCore.py` via la méthode **`open_Notes_app`**.

### **Importations :**  
- Importation de `DKCE` depuis `dkce_extension` (voir plus bas).  
- Importation de CustomTkinter. (évidamment)
- Importation de `filedialog` depuis CustomTkinter (pour gérer les interactions avec l'explorateur de fichiers, comme sauvegarder ou ouvrir un fichier).  

### **Initialisation :**  
Lors de l'initialisation de la classe `NotesApp`, nous créons l'environnement :  
- Des boutons, pour des actions comme "sauvegarder une note".  
- Une zone de texte pour écrire les notes.  

---

# **dkce_extension.py**

Ce fichier gère la création et l’enregistrement de fichiers sous une extension spécifique à DeskCore.  

Pour l'instant, que l’extension `.dkceTXT` existe (attribuée aux fichiers texte). on prévoit d’ajouter d'autres types d'extensions, ainsi qu’un système de cryptage pour sécuriser les fichiers.

---

## **Infos bonus :**

### Méthode `clear_main_zone` :  
Si vous ajoutez une méthode qui toucge au front-end ou affichant une chose dans l'interface, appeler la méthode `clear_main_zone` au debut svp.  
Cette méthode wipe la main zone (la grande frame couvrant les 3/4 de l'écran), évitant les bugs comme :  
> "Vous essayez d'ouvrir l'application Notes alors que vous êtes déjà dans les paramètres ? Rien ne se passe."
(croyez-moi c'est chiant)
