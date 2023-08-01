1.a:
    docker build -t img_1a .
b: 
    docker run -e SRC="src" -e DST="dst" img_1a
c: 
    Pour vérifier que l'opération à réussi on exécute la commande ci-dessous :
    docker exec -it <container_id> bash
    Et on vérifie dans le dossier "dst" que le contenu de src y est.
 ```bash
    root@9a673f2ecc2e:/usr/src/app# ls
    Answers.md  Dockerfile  dst  script_a.py  src
    root@9a673f2ecc2e:/usr/src/app# ls dst/
    empty.txt  file_1.txt  file_2.txt
 ```

2: Modification du fichier scrip_a.py en commentant la ligne time.sleep(10000)

3.a:
    - Build de l'image bash: docker build -t bash .
# Le container suivant est executé en mode interactif pour qu'il reste actif lors de la copie des fichier et pour pouvoir vérifier que les fichiers ont bien été copiés sur le bind mounts.
    - Création du container "container_dst" : docker run -it --name container_dst -v $pwd/dst:/usr/src/app/dst bash 
# Le caractère "`" est nécessaire en powershell pour éviter que le caractère ":" soit interprété dans la variable d'environnement "$pwd"
    - Création du container "container_src" : docker run --name container_src -e SRC="src" -e DST="dst" -v $pwd`:/usr/src/app img_1a
    - On vérifie ensuite que les fichiers ont bien été copiés dans le "container_dst"
# Pour êre sur on supprime le contenu du dosier et on run a nouveau le "container_src" pour vérifier que celà fonctionne bien.
 ```bash 
    bash-5.2# ls
    bin    dev    etc    home   lib    media  mnt    opt    proc   root   run    sbin   srv    sys    tmp    usr    var
    bash-5.2# cd usr/src/app/dst/
    bash-5.2# ls
    empty.txt   file_1.txt  file_2.txt
    bash-5.2# rm file_1.txt file_2.txt
    bash-5.2# ls
    empty.txt
    bash-5.2# ls
    empty.txt   file_1.txt  file_2.txt
```
b.:
    - Build de l'image bash: docker build -t bash .
# Le container suivant est executé en mode interactif pour qu'il reste actif lors de la copie des fichier et pour pouvoir vérifier que les fichiers ont bien été copiés sur le bind mounts.
    - Création du container "container_dst" : docker run -it --name container_dst -v volume/dst:/usr/src/app/dst bash 
# Le caractère "`" est nécessaire en powershell pour éviter que le caractère ":" soit interprété dans la variable d'environnement "$pwd"
    - Création du container "container_src" : docker run --name container_src -e SRC="src" -e DST="dst" -v volume:/usr/src/app img_1a
    - On vérifie ensuite que les fichiers ont bien été copiés dans le "container_dst"
# Pour êre sur on supprime le contenu du dosier et on run a nouveau le "container_src" pour vérifier que celà fonctionne bien.

4:
    - On créer le fichier "script_observer.py" et le fichier "Dockerfile-observer.py"
    - On build l'image de l'observer qui s'appelle "img_observer" avec comme seul contenu le "script_observer.py"
    - On commence a run dans le bon ordres les containers :
        * Premier contenaier "container_dst" : docker run -it --name container_dst -v $pwd/dst:/usr/src/app/dst bash 
        * Second container "container_observer" : docker run --name container_observer -e OBSERVED="dst" -v $pwd`:/usr/src/app img_observer
        * Troisième container "container_src" : docker run --name container_src -e SRC="src" -e DST="dst" -v $pwd`:/usr/src/app img_1a

# Résultat obtenu :
Contenu du dossier observed : ['empty.txt'] à cette date : 2023-07-31 12:54:04.377851
Contenu du dossier observed : ['empty.txt'] à cette date : 2023-07-31 12:54:09.384436
Contenu du dossier observed : ['empty.txt'] à cette date : 2023-07-31 12:54:14.391486
Contenu du dossier observed : ['empty.txt'] à cette date : 2023-07-31 12:54:19.398695
Contenu du dossier observed : ['empty.txt'] à cette date : 2023-07-31 12:54:24.405830
Contenu du dossier observed : ['empty.txt'] à cette date : 2023-07-31 12:54:29.413209
Contenu du dossier observed : ['empty.txt'] à cette date : 2023-07-31 12:54:34.418966
Contenu du dossier observed : ['empty.txt'] à cette date : 2023-07-31 12:54:39.426156
Contenu du dossier observed : ['empty.txt'] à cette date : 2023-07-31 12:54:44.432880
Contenu du dossier observed : ['empty.txt'] à cette date : 2023-07-31 12:54:49.440464
Contenu du dossier observed : ['empty.txt', 'file_1.txt', 'file_2.txt'] à cette date : 2023-07-31 12:54:54.447788
Contenu du dossier observed : ['empty.txt', 'file_1.txt', 'file_2.txt'] à cette date : 2023-07-31 12:54:59.455509
