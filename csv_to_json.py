import re

def isListaTruncada(dados):
    return re.search(r'\*', dados)

def calculaAvg(dados, campo, separator_lista):
    lista = re.split(separator_lista, dados)
    for i in range(len(lista)):
        lista[i] = int(lista[i])
    media = sum(lista)/len(lista)
    campo = re.sub(r'\*', r'_', campo)
    return ("\"" + campo + "\": " + str(media))

def calculaSum(dados, campo, separator_lista):
    lista = re.split(separator_lista, dados)
    for i in range(len(lista)):
        lista[i] = int(lista[i])
    soma = sum(lista)
    campo = re.sub(r'\*', r'_', campo)
    return ("\"" + campo + "\": " + str(soma))

def calculaMax(dados, campo, separator_lista):
    lista = re.split(separator_lista, dados)
    for i in range(len(lista)):
        lista[i] = int(lista[i])
    maximo = max(lista)
    campo = re.sub(r'\*', r'_', campo)
    return ("\"" + campo + "\": " + str(maximo))

def calculaMin(dados, campo, separator_lista):
    lista = re.split(separator_lista, dados)
    for i in range(len(lista)):
        lista[i] = int(lista[i])
    minimo = min(lista)
    campo = re.sub(r'\*', r'_', campo)
    return ("\"" + campo + "\": " + str(minimo))

def conversor(csv, fileOutput, separator, separator_lista): 
    file = open(csv)
    fileOutput = open(fileOutput, 'w')
    first_line = file.readline()
    campos = re.split(separator, first_line.strip())

    output = ""
    output += "[\n"

    for line in file:
        output += ("{\n")
        valores = re.split(separator, line.strip())
        for i in range(len(valores)):
            if not isListaTruncada(campos[i]):
                output += ("\"" + campos[i] + "\": \"" + valores[i] + "\",\n")
            else:
                valor = re.sub(r"\(", r"", valores[i])
                valor = re.sub(r"\)", r"", valor)

                if re.search(r'avg', campos[i]):
                    output += calculaAvg(valor, campos[i], separator_lista)
                    output += ",\n"

                elif re.search(r'sum', campos[i]):
                    output += calculaSum(valor, campos[i], separator_lista)
                    output += ",\n"

                elif re.search(r'max', campos[i]):
                    output += calculaMax(valor, campos[i], separator_lista)
                    output += ",\n"

                elif re.search(r'min', campos[i]):
                    output += calculaMin(valor, campos[i], separator_lista)
                    output += ",\n"

                else:
                    lista = re.split(separator_lista, valor)
                    campo = re.sub(r'\*', r"", campos[i])
                    output += ("\"" + campo + "\": ") 
                    output += "["
                    for index in range(len(lista)):
                        output += str(lista[index])
                        output += ","
                    output += "]"
                    output = re.sub(r',]', r']', output)
                    output += (",\n")
        output += ("},\n")

    output += ("]")

    output = re.sub(r",\n}", r"\n}", output)
    output = re.sub(r"},\n]", r"}\n]", output)
    fileOutput.write(output)


csv = input('Insira o ficheiro CSV que pretende ler: ')
json = input('Insira o nome do ficheiro JSON: ')
separator = input('CSV separado por:\n1) ;\n2) ,\n')
if separator == "1":
    conversor(csv, json, ";", ",")
    print('Conversão realizada com sucesso!')
elif separator == "2":
    conversor(csv, json, ",", ";")
    print('Conversão realizada com sucesso!')
else :
    print("Opção inválida")