import re

def isListaTruncada(dados):
    return re.search(r'\*', dados)

def calculaAvg(dados, campo):
    lista = re.split(",", dados)
    for i in range(len(lista)):
        lista[i] = int(lista[i])
    media = sum(lista)/len(lista)
    campo = re.sub(r'\*', r'_', campo)
    return (campo + ": " + str(media))

def calculaSum(dados, campo):
    lista = re.split(",", dados)
    for i in range(len(lista)):
        lista[i] = int(lista[i])
    soma = sum(lista)
    campo = re.sub(r'\*', r'_', campo)
    return (campo + ": " + str(soma))

def calculaMax(dados, campo):
    lista = re.split(",", dados)
    for i in range(len(lista)):
        lista[i] = int(lista[i])
    maximo = max(lista)
    campo = re.sub(r'\*', r'_', campo)
    return (campo + ": " + str(maximo))

def calculaMin(dados, campo):
    lista = re.split(",", dados)
    for i in range(len(lista)):
        lista[i] = int(lista[i])
    minimo = min(lista)
    campo = re.sub(r'\*', r'_', campo)
    return (campo + ": " + str(minimo))

csv = 'teste.csv'

with open(csv) as line:
    first_line = line.readline()
    campos = re.split(r"[;,]", first_line.strip())
    
file = open(csv)
next(file)

output = ""
output += "[\n"

for line in file:
    output += ("{\n")
    valores = re.split(r";", line.strip())
    for i in range(len(valores) - 1):
        if not isListaTruncada(campos[i]):
            output += (campos[i] + ": \"" + valores[i] + "\",\n")
        else:
            valor = re.sub(r"\(", r"", valores[i])
            valor = re.sub(r"\)", r"", valor)

            if campo := re.search(r'avg', campos[i]):
               output += calculaAvg(valor, campos[i])
               output += ",\n"

            elif campo := re.search(r'sum', campos[i]):
                output += calculaSum(valor, campos[i])
                output += ",\n"

            elif campo := re.search(r'max', campos[i]):
                output += calculaMax(valor, campos[i])
                output += ",\n"

            elif campo := re.search(r'min', campos[i]):
                output += calculaMin(valor, campos[i])
                output += ",\n"

            else:
             lista = re.split(",", valor)
             campo = re.sub(r'\*', r"", campos[i])
             output += (campo + ": ") 
             output += "["
             for index in range(len(lista) - 1):
                output += str(lista[index])
                output += ","
             output += str(lista[index - 1])
             output += "]"
             output += (",\n")
    i += 1
    if not isListaTruncada(campos[i]):
        output += (campos[i] + ": \"" + valores[i] + "\"\n")

    else:
            valor = re.sub(r"\(", r"", valores[i])
            valor = re.sub(r"\)", r"", valor)

            if campo := re.search(r'avg', campos[i]):
               output += calculaAvg(valor, campos[i])

            elif campo := re.search(r'sum', campos[i]):
                output += calculaSum(valor, campos[i])

            elif campo := re.search(r'max', campos[i]):
                output += calculaMax(valor, campos[i])

            elif campo := re.search(r'min', campos[i]):
                output += calculaMin(valor, campos[i])

            else:
             lista = re.split(",", valor)
             campo = re.sub(r'\*', r"", campos[i])
             output += (campo + ": ") 
             output += "["
             for index in range(len(lista) - 1):
                output += str(lista[index])
                output += ","
             output += str(lista[index - 1])
             output += "]"
             output += (",\n")
    output += ("},\n")

output += ("]")

output = re.sub("},\n]", "}\n]", output)
print(output)