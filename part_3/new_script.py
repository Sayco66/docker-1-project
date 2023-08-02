import os 

ID_CONTAINER = os.environ.get("ID_CONTAINER")
ID = int(ID_CONTAINER)

file = open('code.txt', 'r')
content = file.readlines()

try:
    exec(content[ID])
    stripped_line=content[ID].strip()
    with open('results.csv', 'a') as csv_file:
        csv_file.write(f"{ID},{stripped_line},1\n")

    # La création de ce fichier va nous permettre de compter les succèes entre tous les containers pour avoir le pourcentage de réussite à la fin.
    success_file = open('success_file.txt','a')
    success_file.write('success\n')

except:
    stripped_line=content[ID].strip()
    with open('results.csv', 'a') as csv_file:
        csv_file.write(f"{ID},{stripped_line},0\n")

