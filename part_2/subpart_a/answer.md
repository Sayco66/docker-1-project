Part_2

subpart_a :

2. 
Voici le dossier "docker-compose.yaml"

version: "3.8"      Ici on a la version 
services:
  app:      On construit le premier service
    build: .
    command: python -u app.py       Ici on indique que l'on veut lancer app.py avec python 
    ports:
      - "5000:5000"     Ici on indique que le port du container est le 5000
    volumes:
      - .:/app      On indique l'emplacement du volume
    links:
      - db    On met un lien avec le service "db"
  db:       On construit le deuxième service 
    image: mongo:latest     On importe la derniere image "mongo"
    hostname: test_mongodb
    environment:
      - MONGO_INITDB_DATABASE=animal_db     On initialise la BDD qui se nomme "animal_db"
      - MONGO_INITDB_ROOT_USERNAME=root     On indique le nom d'utilisateur "root"
      - MONGO_INITDB_ROOT_PASSWORD=pass     On indique le mot de passe "pass" 
    volumes:
      - ./init-db.js:/docker-entrypoint-initdb.d/init-db.js:ro      on initialise le volume 
    ports:
      - 27017:27017     on indique le port attribué qui est la 27017

3. 
docker-compose up --build nous permet de batir l'image.

4.  
- Ici le premier Dockerfile :

FROM python:3.9-slim

WORKDIR /usr/src/app

COPY app.py .
COPY requirements.txt .

RUN pip install -r requirements.txt

ENTRYPOINT python app.py

- On build l'image avec la commmande : docker build  -f .\Dockerfile-app -t app .
- On la run avec la commande : docker run -p 5000:5000 app

- Ici le deuxieme Dockerfile : 
FROM mongo:6.0.8

ENV MONGO_INITDB_DATABASE=animal_db
ENV MONGO_INITDB_ROOT_USERNAME=root
ENV MONGO_INITDB_ROOT_PASSWORD=pass

ADD init-db.js /docker-entrypoint-initdb.d/ 

- On build l'image avec la commmande : docker build -f .\Dockerfile-db -t data_base .
- On la run avec la commande : docker run -p 27017:27017 database

5. 
- Pour se rendre dans une invite de commande on utilise la commande suivante : docker exec -it {id_container} /bin/bash
- On lance la console python et on execute le code. 

6. 

- Le code en python pour ajouter des données. 
import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["animals_db"]
mycol = mydb["customers"]

mylist = [
  {
    id: 4,
    name: "Elephant",
    type: "wild",
  },
  {
    id: 5,
    name: "Horse",
    type: "domestic",
  },
  {
    id: 6,
    name: "Shark",
    type: "wild",
  },
]

x = mycol.insert_many(mylist)

#print list of the _id values of the inserted documents:
print(x.inserted_ids)

7. 


8. 
- On créer le Dockerfile-insert.
- Pour créer une nouvelle image img_insert : docker build -f .\Dockerfile-insert -t img_insert 
- Pour le conteneur on utilise : docker run img_insert 