import re

def isListaTruncada(dados):
    return re.search(r'\*', dados)

def calculaAvg(dados):
    return

def calculaSum(dados):
    return

def calculaMax(dados):
    return

def calculaMin(dados): 
    return

with open('notas.csv') as line:
    first_line = line.readline()
    campos = re.split(r";", first_line.strip())

file = open('notas.csv')
next(file)

print("[")

for line in file:
    print("{")
    valores = re.split(r";", line.strip())
    for i in range(len(valores) - 1):
        if not isListaTruncada(campos[i]):
            print(campos[i] + ": " + valores[i] + ",")
    i += 1
    if not isListaTruncada(campos[i]):
        print(campos[i] + ": " + valores[i])
        print("},")

print("]")