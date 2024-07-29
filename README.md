# RepartGroup

Cinepédia est un petit projet amusant, écrit ensemble avec __Praise Mazowa, Etudiant à l'ISP en promotion de L1 Informatique & Technologie__, la problématique était de créer un outil capable de repartir les étudiants de sa promotion en groupe de travail tâche qui se faisait habituellement à la main, du coup un dimanche soir on a écrit ce petit programme __RepartGroup__ pour effectuer cette tâche fastidieuse.

# Installation

Pour installer (utiliser) RepartGroup en local, commencer par installer une version de l’interpréteur python 3.x, pour ma part ce code à été écrit sous python 3.11. Ensuite télécharger ce répértoire sur votre machine locale et executer les quelques instructions suivantes pour pouvoir utilisez le projet :

## Environnement virtuel

Pour pouvoir isoler ce projet de tous les autres (ce qui en passant est une chose que vous devriez faire pour tous vos projets python), nous allons créer un environnement virtuel avec l'outil `venv` suivant le système que vous utilisez.

```bash 
// Sur Linux
cd repart-group
python3.x -m venv venv

// Sur Windows
cd repart-group
python -m venv venv
```

Ensuite il va falloir activez cet environnement virtuel et y installez toutes les dépendances de notre projet

```bas
// Sur Linux
source venv/bin/activate
python -m pip install -r requirements.txt

// Sur Windows
cd venv/Scripts
activate
cd ..
python -m pip install -r requirements.txt
```

Votre environnement virtuel crée et prêt à l'emploi il ne vous reste plus qu'à lancer le programme avec une instruction `python app.py`



https://github.com/user-attachments/assets/bcf40586-9569-48ef-8594-20486640669b

