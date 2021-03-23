import re

with open('notas.csv') as line:
    first_line = line.readline()
    campos = re.split(r";", first_line)

file = open('notas.csv')
next(file)

print("[")

for line in file:
    print("{")
    camposNotas = re.split(r";", line)
    print(campos[0] + ": " + camposNotas[0] + " ,")
    print(campos[1] + ": " + camposNotas[1] + " ,")
    print(campos[2] + ": " + camposNotas[2] + " ,")
    notas = campos[3]
    if notas == 'notas*\n':
        result = re.sub(r'\(', r'[', camposNotas[3])
        result = re.sub(r'\)', r'\]', camposNotas[3])
        print("notas : " + result)
        print("}")
    elif notas == "notas*sum":
        print("notas*avg : " + camposNotas[3])
        print("}")
    elif notas == "notas*avg":
        print("notas*avg : " + camposNotas[3])
        print("}")
    elif notas == "notas*max":
        print("notas*avg : " + camposNotas[3])
        print("}")
    elif notas == "notas*min":
        print("notas*avg : " + camposNotas[3])
        print("}")


print("]")