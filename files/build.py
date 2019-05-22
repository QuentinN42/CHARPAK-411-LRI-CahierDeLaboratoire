import os
from datetime import date

listedFiles = list(os.listdir("./"))
dico = eval(open("ids", "r").read())
folders = []

for key in dico:
    if key in listedFiles:
        print("Adding {id} with tag {tag}".format(id=key, tag=dico[key]))
        folders.append(key)
    else:
        print("Error, can't add {id}".format(id=key))


all_days = []
for folder in folders:
    files = list(os.listdir(folder))
    for file in files:
        new = True
        for d in all_days:
            if d[0] == file:
                new = False
                break
        if new:
            all_days.append([file, folder])
        else:
            for i in range(len(all_days)):
                if all_days[i][0] == file:
                    all_days[i].append(folder)
                    break

all_days.sort()

out = open("result.tex", "w")

for day in all_days:
    y = int(day[0][0:4])
    m = int(day[0][4:6])
    d = int(day[0][6:8])
    out.write("\\newpage\n")
    out.write("\\section{Le " + date(y, m, d).strftime("%d/%m/%Y") + " :}\n")
    for i in range(len(day)):
        if i == 0:
            pass
        else:
            out.write("    \\subsection{" + dico[day[i]] + " :}\n")
            out.write("        \\input{files/" + day[i] + "/" + day[0] + "}\n")

out.close()


print("\n\n\n\n" + open("result.tex", "r").read())
