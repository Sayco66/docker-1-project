file = open('code.txt', 'r')
with open('results.csv', 'a') as csv_file:
    csv_file.write("Line-Number,Line-Content,Status\n")
rows = file.readlines()

success = 0
line_number = 0
for line in rows:
    try:
        exec(line)
        stripped_line=line.strip()
        with open('results.csv', 'a') as csv_file:
            csv_file.write(f"{line_number},{stripped_line},1\n")
        line_number = line_number + 1
        success = success + 1

    except:
        stripped_line=line.strip()
        with open('results.csv', 'a') as csv_file:
            csv_file.write(f"{line_number},{stripped_line},0\n")
            line_number = line_number + 1
with open('code.txt','r') as rf:
    lignes=len(rf.readlines())
percentage = (success / lignes) * 100
print(f"Le pourcentage de réussite est de : {percentage}%")