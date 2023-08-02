import subprocess;
import time;

process=subprocess.Popen(["powershell",'docker build -f .\Dockerfile-new -t img_3new .'])
time.sleep(5)
file = open('code.txt', 'r')
rows = file.readlines()
ligne = 0

for line in rows:
    process=subprocess.Popen(["powershell",f'docker run --rm -e ID_CONTAINER="{ligne}" -v $pwd`:/usr/src/app img_3new'])
    ligne = ligne + 1
    time.sleep(1)

with open('code.txt','r') as rf:
    lignes=len(rf.readlines())

with open('success_file.txt','r') as fs:
    success=len(fs.readlines())

percentage = (success / lignes) * 100
print(f"Le pourcentage de réussite est de : {percentage}%")

