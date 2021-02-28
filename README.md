<h2>Who, When 'n' Why ?</h2>

<p>J'ai develloppé cette plateforme seul dans le cadre de ma formation OpenClassrooms du parcours 'developpeur d'applications Python' durant les mois de novembre à janvier 2021. Je suis ouvert à toute amélioration de votre part bien entendu si vous le désirez.</p>

<h2>Kesako ?</h2>

<p>Cette plateforme propose à un utilisateur de pourvoir substituer un produit qu'il consomme en vue d'en consommer un plus sain. Il peut s'il le désire ouvrir un compte afin d'y enregistrer ou de supprimer ses substitus.</p>

<h2>Installation</h2>

1. Pour l'installer, créez un dossier en local et clonez le projet 'P8_Cottenceau_Thomas' sur Github à l'adresse suivante :<br>
<em>https://github.com/thomsart/P8_Cottenceau_Thomas</em>

2. Une fois fait créez votre environnement virtuel et activez le :<br>
<em>python -m venv env</em> (pour le créer)<br>
<em>.\env\Scripts\activate</em> (pour l'activer)

3. Une fois activé installé y toutes les dépendances néccéssaires au projet en tapant la commande suivante :<br>
<em>pip install -r requirements.txt</em>

4. Créez votre base de données à l'aide de Postgrès. Pensez à bien modifier les paramètres liés à votre base de données dans les 'settings.py' à l'url:<br>
'startup_pur_beurre/startup_pur_beurre/settings.py'

5. Maintenant il est temps de remplir la base de données en y entrant les produits que vous desirez, pour ce faire rendez vous sur l'API 'Open Food Facts' à cette adresse:
<em>https://fr.openfoodfacts.org/</em><br>
cherchez une categorie de produits qui vous intéresse et repérez bien le nombre de page associé. Une fois votre produit repérer enregistrez le ou les json associés en allant le récupérer à l'url:<br>
https://fr-en.openfoodfacts.org/category/camembert/1.json (Ici on a choisit par exemple de prendre la première page des camemberts)<br>
Enregistrer le en le nommant de cette manière: 'camembert_1.json' (pour la première page). Et placez le dans le répertoire nommé 'json_folder' de l'application 'database' du projet Django 'startup_pur_beurre'. Il ne vous reste plus qu'à lancer le script chargé de remplir la base de données avec le fichier en tapant la commande:<br>
<em>python manage.py runscript get_products</em><br>
Répetez autant de fois l'opération que vous désirez de produits dans votre base.

6. Une fois votre base de données bien remplis rendez-vous à la racine du projet l'aide de votre terminale et éxécutez la commande suivante pour lancer le server en local sur votre machine afin de pouvoir l'ouvrir ensuite avec votre navigateur :<br>
<em>python manage.py runserver</em>

5. Enfin ouvrez votre navigateur web et tapez y la l'url suivante :<br>
<em>http://localhost:8000</em> (ici '8000' sur ma machine mais regardez le numéro du votre dans le terminal lors de l'activation de votre server.)

6. Il vous est possible de lancer les tests et le coverage (couverture des test) après amélioration de votre part en éxécutant les commandes suivantes:<br>
<em>pytest</em> (lance tout les tests des applications)<br>
Et pour avoir la couverture des tests faites:<br>
<em>pytest --cov=users</em> (pour l'application 'users')<br>
<em>pytest --cov=database</em> (pour l'application 'database')<br>

<h2>Liens de la plateforme sur le web</h2>

<p>Vous pouvez toute-fois vous rendre sur le site en ligne à cette adresse:<br>
<em>https://pur-beurre-cottenceau-thomas.herokuapp.com/</em></p>