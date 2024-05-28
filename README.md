# Chess Tournament

## Installation:
1. clonez ce repository:
```
git clone https://github.com/LivioSmd/ChessTournamentSotfware.git
```
2. Créez un nouvel environnement virtuel (venv), depuis le projet:
```
python -m venv env
```
3. Lancez l'environnement virtuel:
Windows / Mac:
```
source venv/bin/activate
```

4. Installer les packages requis:
```
pip install -r requirements.txt
```

5. Lancer le programme:
```
python MainController.py
```

## Utilisation du logiciel de gestion de tournoi.
Le menu principal comporte 6 options :
### 1. Ajouter un joueur à la base de donnée
- Renseigner le nom du joueur
- Renseigner le prénom du joueur
- Renseigner la date d'anniversaire du joueur
### 2. Créer et nouveau tournoi
- Renseigner le nom du tournoi
- Renseigner l'endroit du tournoi
- Renseigner la date de début du tournoi
- Renseigner la date de fin du tournoi
- Renseigner le nombre de round(s)
- Renseigner la description du tournoi
- Choisir les joueurs pour votre tournoi parmis tous ceux présent en base de donnée (8 minimums)
### 3. Lancer un tournoi
- Sélectionner un tournoi parmis tous ceux présent en base de donnée
### 4. Récupérer la liste de tous les joueurs en base de donnée
- Renvoie la liste de tous les joueurs présent en base de donnée
### 5. Récupérer la liste de tous les tournois en base de donnée
- Renvoie la liste de tous les tournois présent en base de donnée
### 6. Quitter le programme
- ferme le programme
