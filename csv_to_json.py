import re

'''
    Função que, recorrendo ao uso de um search, analisa se o campo é, ou não, uma lista truncada
'''
def isListaTruncada(dados):
    return re.search(r'\*', dados)

'''
    Função que recebe três strings. A primeira corresponde aos dados
da lista truncada (dados), a segunda é o nome do campo (campo) a que diz
respeito e a terceira indica o separador da lista (separator_lista).
    Usando a função split, separa-se a string dos dados pelo separator_lista
armazenando a informação numa lista de int.
    Usando a função sum e len aplicadas à anterior lista calculamos a média dos
dados.
    Usando a função sub substituimos no argumento campo o "*" pelo "_",
retornando, por fim, o argumento campo, seguido pela variável calculada "media"
em formato de String.
'''
def calculaAvg(dados, campo, separator_lista):
    lista = re.split(separator_lista, dados)
    for i in range(len(lista)):
        lista[i] = float(lista[i])
    media = sum(lista)/len(lista)
    campo = re.sub(r'\*', r'_', campo)
    return ("\"" + campo + "\": " + str(media))

'''
    Função que recebe três strings. A primeira corresponde aos dados
da lista truncada (dados), a segunda é o nome do campo (campo) a que diz
respeito e a terceira indica o separador da lista (separator_lista).
    Usando a função split, separa-se a string dos dados pelo separator_lista
armazenando a informação numa lista de int.
    Usando a função sum aplicada à anterior lista calculamos o somatório dos
dados.
    Usando a função sub substituimos no argumento campo o "*" pelo "_",
retornando, por fim, o argumento campo, seguido pela variável calculada "soma"
em formato de String.
'''
def calculaSum(dados, campo, separator_lista):
    lista = re.split(separator_lista, dados)
    for i in range(len(lista)):
        lista[i] = float(lista[i])
    soma = sum(lista)
    campo = re.sub(r'\*', r'_', campo)
    return ("\"" + campo + "\": " + str(soma))

'''
    Função que recebe três strings. A primeira corresponde aos dados
da lista truncada (dados), a segunda é o nome do campo (campo) a que diz
respeito e a terceira indica o separador da lista (separator_lista).
    Usando a função split, separa-se a string dos dados pelo separator_lista
armazenando a informação numa lista de int.
    Usando a função max aplicada à anterior lista calculamos o máximo dos
dados.
    Usando a função sub substituimos no argumento campo o "*" pelo "_",
retornando, por fim, o argumento campo, seguido pela variável calculada "maximo"
em formato de String.
'''
def calculaMax(dados, campo, separator_lista):
    lista = re.split(separator_lista, dados)
    for i in range(len(lista)):
        lista[i] = float(lista[i])
    maximo = max(lista)
    campo = re.sub(r'\*', r'_', campo)
    return ("\"" + campo + "\": " + str(maximo))

'''
    Função que recebe três strings. A primeira corresponde aos dados
da lista truncada (dados), a segunda é o nome do campo (campo) a que diz
respeito e a terceira indica o separador da lista (separator_lista).
    Usando a função split, separa-se a string dos dados pelo separator_lista
armazenando a informação numa lista de int.
    Usando a função min aplicada à anterior lista calculamos o mínimo dos
dados.
    Usando a função sub substituimos no argumento campo o "*" pelo "_",
retornando, por fim, o argumento campo, seguido pela variável calculada "minimo"
em formato de String.
'''
def calculaMin(dados, campo, separator_lista):
    lista = re.split(separator_lista, dados)
    for i in range(len(lista)):
        lista[i] = float(lista[i])
    minimo = min(lista)
    campo = re.sub(r'\*', r'_', campo)
    return ("\"" + campo + "\": " + str(minimo))

'''
    Função responsável por ler os dados do ficheiro CSV e escrevê-los no
ficheiro JSON.
    O ficheiro CSV é aberto com a função pré-definida open, com o modo de
codificação binária "UTF-8" ativo. É aberto um descritor de ficheiro em modo de
escrita para o ficheiro JSON com o nome passado no segundo input da função
principal, caso este ficheiro não exista é criado um novo.
    É lida a primeira linha do ficheiro CSV com a função pré-definida readLine,
que vai ignorar qualquer espaço no início e fim desta, devido à função pré-
-definida strip. É separada e colocada numa lista pela função split, com o
separador definido na função principal (terceiro input).
'''
def conversor(csv, fileOutput, separator, separator_lista):
    file = open(csv,encoding="utf8")
    fileOutput = open(fileOutput, 'w')
    first_line = file.readline()
    campos = re.split(separator, first_line.strip())

    output = ""
    output += "[\n"

    for line in file:
        output += ("{\n")
        valores = re.split(separator, line.strip())
        for i in range(len(campos)):
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

'''
    Função principal do nosso conversor de CSV para JSON, onde, usando a função
input, pré-definida, é recebido:
        - O nome do ficheiro CSV a ler;
        - O nome do ficheiro JSON para onde a informação vai ser escrita,
caso o ficheiro JSON não exista, então é criado um com o nome dado no segundo
input;
        - O caracter que separa os campos de dados no ficheiro CSV;
    Após a receção destes parâmetros, é chamada a função conversor com os
mesmos, sendo que ela é responsável por executar a transformação dos dados entre
ficheiros.
    No final é impressa uma mensagem a notificar que a conversão foi bem
executada.
'''
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
