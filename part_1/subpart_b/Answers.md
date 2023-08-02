# Exercice 1:
La commande qui permet de bâtir l'image est :
```bash
docker build -t img_1b
```
Puis pour run le container :
```bash
docker run img_1b
```
# Exercice 2:
Ces valeurs ont été définis dans le Dockerfile : 
```Dockerfile
FROM busybox
# Définition de la valeur de "VAR_1", par conséquant la valeur de "VAR_2" n'a pas été définie.
ENV VAR_1="Some variable for 1" 

# Les variables sont ensuites exportés dans le container, il ne faut pas définir la valeur des variables d'environnement dans l'export mais avant.
RUN export VAR_1="Some variable for 1, but different"
RUN export VAR_2="Some variable for 2"

# Une fois le container Run il va exécuter la commande ci-dessous qui permet d'afficher un texte contenant les variables d'environnements.
CMD echo FOO is $VAR_1, BAR is $VAR_2
```

Voici ce que l'on obtient après modifications.
```bash 
FOO is Some variable for 1, BAR is Some variable for 2
```

# Exercice 3:
Voici à quoi ressemble le "Dockerfile-corrected" :
```Dockerfile
FROM busybox

CMD echo FOO is $VAR_1, BAR is $VAR_2
``` 

Voici la commande à utiliser pour définir les variables d'environnement à travers le docker run :
```bash
docker run -e VAR_1="Some variable for 1" -e VAR_2="Some variable for 2" img_1bcorrected
```

Résultat : 
```bash
FOO is Some variable for 1, BAR is Some variable for 2
```

# Exercice 4:
```bash
[+] Building 1.2s (7/7) FINISHED
 => [app internal] load build definition from Dockerfile                                                                                                                    0.0s
 => => transferring dockerfile: 319B                                                                                                                                        0.0s
 => [app internal] load .dockerignore                                                                                                                                       0.0s
 => => transferring context: 2B                                                                                                                                             0.0s
 => [app internal] load metadata for docker.io/library/busybox:latest                                                                                                       0.0s
 => CACHED [app 1/3] FROM docker.io/library/busybox                                                                                                                         0.0s
 => [app 2/3] RUN export VAR_1                                                                                                                                              0.4s
 => [app 3/3] RUN export VAR_2                                                                                                                                              0.5s
 => [app] exporting to image                                                                                                                                                0.1s
 => => exporting layers                                                                                                                                                     0.1s
 => => writing image sha256:9ed503fd6dd3b6693d75940bdc1f2639bc0ca72629e043242c5343f049820ec3                                                                                0.0s
 => => naming to docker.io/library/busybox                                                                                                                                  0.0s
[+] Running 1/1
 ✔ Container subpart_b-app-1  Created                                                                                                                                       0.1s
Attaching to subpart_b-app-1
subpart_b-app-1  | FOO is Some variable for 1, BAR is Some variable for 2
subpart_b-app-1 exited with code 0
```
On voit bien que la commande echo est executée avec les bonnes variables environnementales.