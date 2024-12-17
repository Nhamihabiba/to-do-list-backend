Prérequis

Avant de commencer, assurez-vous d'avoir installé les outils suivants sur votre machine :

    Python (version 3.8+) → Télécharger Python
    Git → Télécharger Git

 1. Cloner le projet
 git clone https://github.com/Nhamihabiba/to-do-list-backend.git
 cd <NOM_DU_REPERTOIRE>


3. Configuration de la base de données
python manage.py makemigrations
python manage.py migrate

4. Démarrer le serveur Django  
python manage.py runserver
 