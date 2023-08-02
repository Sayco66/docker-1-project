# Exercice 1:
Explication du fichier "script.py".
```python
import datetime
import os
from urllib import request, parse
import ssl

import requests
import pandas as pd

# Le 1er bloc définie la variable urls qui correspont à 2 sites wikipedia (python et javascript)
urls = {
    "python": "https://fr.wikipedia.org/wiki/Python_(langage)",
    "javascript": "https://fr.wikipedia.org/wiki/JavaScript",
}

# Le 2ème bloc est une fonction(get_table) qui permet de récupérer une table grâce au module request et de mettre en forme le tableau avec pandas
def get_table(url):
    context = ssl._create_unverified_context()
    response = request.urlopen(url, context=context)
    html = response.read()
    return pd.read_html(html)[0].iloc[1:-1, 0:2].dropna()

# Le 3ème bloc va parcourir les urls créer un dossier language si il n'existe pas, créer une table avec les urls puis transformer cette table en fichier csv et nommer le fichier csv en fonction du language.
# Ensuite il va ouvrir un fichier "logs.txt" en mode "append", récupérer la date actuelle en format "YYYY-MM-DD" puis va définir du texte dans le fichier de logs au format : "date actuelle: language data scrapped" Puis il va afficher le message et l'écrire dans le fichier de logs.
if __name__ == "__main__":
    for language, url in urls.items():
        os.makedirs(language, exist_ok=True)
        table = get_table(url)
        table.to_csv(f"{language}/wikipedia_table.csv")

        with open("logs.txt", "a") as f:
            now = datetime.datetime.now().isoformat()
            message = f"{now}: {language} data scraped\n"
            print(message)
            f.write(message)

    ############################# question 4

    URL_LOGS = "????"

    with open("logs.txt", "r") as f:
        try:
            response = requests.post(URL_LOGS, json={"logs": f.read()})

            print("Status code", response.status_code)
            print(response.json())

        except Exception as e:
            print(e)
```

# Exercice 2:
- Voici les commandes a faire pour répondre à la question 2, j'ai utilisé un bind-mounts pour pouvoir vérifier le fonctionnement facilement.
```bash
docker build -t imc_1c .
docker run --rm -v $pwd/python:/usr/src/app/python img_1c
docker run --rm -v $pwd/javascript:/usr/src/app/javascript img_1c 
```

- Vérification :
    * La première commande a seulement récupéré la table python et la seconde seulement le javascript.
    * Donc il y a bien 2 volumes différents pour chaque language.
    * Si on fait un docker ps -a on voit bien que le container provenant de l'image "img_1c" n'apparaît pas.

# Exerice 3:
Voici les commandes a faire pour répondre à la question 3.
```bash
docker build -t imc_1cplus .
docker run --rm -v $pwd/python:/usr/src/app/python img_1cplus
docker run --rm -v $pwd/javascript:/usr/src/app/javascript img_1cplus
docker run --rm -v $pwd/php:/usr/src/app/php img_1cplus 
```

# Exercice 4:
Ce code ci-dessous va effectuer une requête post sur une l'url définie dans la variable URL_LOGS puis va lire le fichier de logs.
```python
URL_LOGS = "????"

with open("logs.txt", "r") as f:
    try:
        response = requests.post(URL_LOGS, json={"logs": f.read()})
        print("Status code", response.status_code)
        print(response.json())

    except Exception as e:
        print(e)

```

- Etape 1: créer le fichier "app.py", "dockerfile-app" et "requirements-app.txt".

- Etape 2: Modifier le fichier "script.py" et rebuild l'image "img_1cplus"

- Etape 3: run les containers dans le bon ordre : d'abord "img_1capp" puis "img_1cplus". (J'ai utilisé l'image run avec le volume php pour être sur qu'elle fonctionne toujours)
```bash
docker run -p 80:80 img_1capp
docker run --rm -v $pwd/php:/usr/src/app/php img_1cplus
```

- Résultat:
```bash
2023-08-01T08:00:58.203989: python data scraped

2023-08-01T08:00:58.403641: javascript data scraped

2023-08-01T08:00:58.622933: php data scraped

Status code 200
{'data_received': {'logs': '2023-08-01T08:00:58.203989: python data scraped\n2023-08-01T08:00:58.403641: javascript data scraped\n2023-08-01T08:00:58.622933: php data scraped\n'}, 'success': True}
```

# Exerice 5:
- Etape 1: créer le fichier "script_simple.py", "dockerfile-simple" et "requirements-simple.txt".

- Etape 2: Build l'image du container avec le nom "img_1csimple".

- Run les containers dans le bon ordre: d'abord "img_1capp" puis "img_csimple". Sans oublier les variables d'environnements.
```bash
docker run -p 80:80 img_1capp
docker run --rm -e URL="https://fr.wikipedia.org/wiki/Structured_Query_Language" -e LANGUAGE="sql" -v $pwd/sql:/usr/src/app/sql img_1csimple
```

- Résultat:
```bash
2023-08-01T08:41:12.039397: sql data scraped

Status code 200
{'data_received': {'logs': '2023-08-01T08:41:12.039397: sql data scraped\n'}, 'success': True}
```

# Exercice 6:
- Creation et Exécution du fichier "orchestrate.py"
```python
import subprocess;
import time;
URL_PYTHON = "https://fr.wikipedia.org/wiki/Python_(langage)"
URL_JAVASCRIPT = "https://fr.wikipedia.org/wiki/JavaScript" 

process=subprocess.Popen(["powershell",'docker build -f .\Dockerfile-simple -t img_1csimple .'])
time.sleep(5)
process=subprocess.Popen(["powershell",f'docker run --rm -e URL="{URL_PYTHON}" -e LANGUAGE="python" -v $pwd/python:/usr/src/app/python img_1csimple'])
time.sleep(5)
process=subprocess.Popen(["powershell",f'docker run --rm -e URL="{URL_JAVASCRIPT}" -e LANGUAGE="javascript" -v $pwd/javascript:/usr/src/app/javascript img_1csimple'])
```

- Resultat:
```bash
python .\orchestrate.py
[+] Building 0.2s (10/10) FINISHED                                                                                                               docker:default
 => [internal] load .dockerignore                                                                                                                          0.0s
 => => transferring context: 2B                                                                                                                            0.0s
 => [internal] load build definition from Dockerfile-simple                                                                                                0.0s
 => => transferring dockerfile: 235B                                                                                                                       0.0s
 => [internal] load metadata for docker.io/library/python:3.9-slim                                                                                         0.0s
 => [1/5] FROM docker.io/library/python:3.9-slim                                                                                                           0.0s
 => [internal] load build context                                                                                                                          0.0s
 => => transferring context: 80B                                                                                                                           0.0s
 => CACHED [2/5] WORKDIR /usr/src/app                                                                                                                      0.0s
 => CACHED [3/5] COPY requirements-simple.txt .                                                                                                            0.0s
 => CACHED [4/5] RUN pip install -r requirements-simple.txt                                                                                                0.0s
 => CACHED [5/5] COPY script_simple.py .                                                                                                                   0.0s
 => exporting to image                                                                                                                                     0.0s
 => => exporting layers                                                                                                                                    0.0s
 => => writing image sha256:a5ffa25f5f67e96b26066893428332e078b94f3f4ae419bb65a785525cb98ac7                                                               0.0s
 => => naming to docker.io/library/img_1csimple                                                                                                            0.0s

What's Next?
  View summary of image vulnerabilities and recommendations → docker scout quickview
2023-08-01T08:55:57.342655: python data scraped

Status code 200
{'data_received': {'logs': '2023-08-01T08:55:57.342655: python data scraped\n'}, 'success': True}
PS C:\Users\gabym\Desktop\Cours , Important\Live Campus\Cours\docker\docker-1-project\part_1\subpart_c> 2023-08-01T08:56:02.302065: javascript data scraped

Status code 200
{'data_received': {'logs': '2023-08-01T08:56:02.302065: javascript data scraped\n'}, 'success': True}
```