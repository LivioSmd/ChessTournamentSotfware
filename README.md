# logiciel de gestion de tournoi d'Échec

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
### Le logiciel comporte 2 Menu : 
- un menu principal : gestion et création de joueurs et de tournois.
- un menu secondaire : gestion, déroulement et génération de rapports d'un tournoi donné.

---
### Le menu principal comporte 6 options :
### 1. Ajouter un joueur à la base de donnée
- Renseigner le nom du joueur
- Renseigner le prénom du joueur
- Renseigner la date d'anniversaire du joueur
### 2. Créer et nouveau tournoi
- Renseigner le nom du tournoi
- Renseigner l'endroit du tournoi
- Renseigner la date de début du tournoi
- Renseigner la date de fin du tournoi
- Renseigner le nombre de round
- Renseigner la description du tournoi
- Choisir les joueurs pour votre tournoi parmi tous ceux présent en base de donnée (8 minimums)
### 3. Lancer un tournoi
- Sélectionner un tournoi parmi tous ceux présent en base de donnée
### 4. Récupérer la liste de tous les joueurs en base de donnée
### 5. Récupérer la liste de tous les tournois en base de donnée
### 6. Quitter le programme

---
### Le menu secondaire comporte 6 options :
(Le menu secondaire s'ouvre lorsque de l'on crée ou que l'on choisit de lancer un tournoi déjà crée.)

#### 1. Lancer ou continuer un round
#### 2. Stopper un round
#### 3. Récupérer les informations du tournoi
#### 4. Récupérer la liste des joueurs du tournoi
#### 5. Récupérer les informations concernant les rounds et les matchs du tournoi
#### 6. Retour au menu principal
