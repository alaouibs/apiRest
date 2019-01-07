# apiRest
 microservice avec une API REST qui permet aux utilisateurs de réaliser un ensemble de fonctionnalités
 
 
### Installation 
Dans le dossier v2
```
git clone https://github.com/alaouibs/apiRest.git
cd apiRest/v2
```

Pour lancer l'application
```
python app.py
```

Sur un navigateur 

```
http://127.0.0.1:5000/api/v2/resources/users/all
http://127.0.0.1:5000/api/v2/resources/goods/all
```

#### En tant qu'utilisateur je veux pouvoir afficher les biens immobiliers d'une ville en particulier afin de me renseigner.
Pour afficher les biens immobiliers d'une ville : 
```
http://127.0.0.1:5000/api/v2/resources/goods/<ville_id>
```

Par exemple 
```
http://127.0.0.1:5000/api/v2/resources/goods/v
```
#### En tant qu'utilisateur je veux pouvoir modifier les caractéristiques d'un bien immobilier afin de le mettre à jour.
Sur un terminal, pour modifier une caractéristique d'un bien immobilier : 

```
curl -X PUT -H "Content-Type: application/json" http://127.0.0.1:5000/api/v2/resources/goods/<id>?<carac>=<valeur>
```

#### En tant qu'utilisateur je veux pouvoir modifier les caractéristiques me concernant afin de me mettre à jour.
Également sur un terminal, pour modifier une caractéristique de l'utilisateur : 
 
```
curl -X PUT -H "Content-Type: application/json" http://127.0.0.1:5000/api/v2/resources/users/<id>?<carac>=<valeur>
```

Il est possible de modifier plusieurs caractéristiques à la fois en faisant : 
```
<carac1>=<valeur1>&<carac2>=<valeur2>
```
