'''
Pretende-se guardar numa lista de contactos dicionários com os seguintes atributos: nome, telefone

Deverá surgir no ecrã a mensagem: Pretende inserir um novo contacto [s/n]
O programa deverá dar indicação de valor inválido caso seja inserido um valor diferente de s e n
Se responder s deverá preencher um contacto  
Se responder n deverá executar as seguintes operações:
-> imprimir os dados de todos os contactos
-> Pesquisar o contacto pelo nome
'''

# functions
# FUNÇÃO PARA VALIDAR TIPOS DE VARIÁVEIS, AJUDA NA RESOLUÇÃO DE ERROS EM PROGRAMAS MAIORES
def insertValidValue(type, inputMsg):
    if type == "string":
        val = input(inputMsg).capitalize()
    elif type == "int":
        val = int(input(inputMsg))
    return val

def addInfo():
    person = {
        "nome" : insertValidValue("string", "Nome: "),
        "telefone" : insertValidValue("string", "Telefone: ")
    }
    return person

def maxNameLen(listPeople):
    # essa estrutura do len() for in: itera uma lista temporária e salva o maior comprimento
    maxLenName = max(len(person['nome']) for person in listPeople)
    return maxLenName

def printContact(person, size):
    print("-"*50)
    print(f"Nome: {person['nome']:<{size}}  Telefone: {person['telefone']}")

def selectPerson(listPeople):
    name = input("Digite o nome: ")
    size = maxNameLen(listPeople)
    for person in listPeople:
        if person['nome'].lower() == name.lower():
            printContact(person, size)
            break
    else:
        print(f"O nome {name.capitalize()} não foi encontrado na nossa base de dados!!")

def selectPeople(listPeople):
    while True:
        print("-"*50)
        op = input("Deseja pesquisar pelo nome? [s/n]: ")
        if op.lower() == "s":
            selectPerson(listPeople)
        elif op.lower() == "n":
            break
        else:
            print("\nErro! Opção inválida. Pretende inserir um novo contacto [s/n]")

def printData(listPeople):
    size = maxNameLen(listPeople)
    for person in listPeople:
        printContact(person, size)

def addPeople(listPeople):
    while True:
        op = input("Pretende inserir um novo contacto [s/n]: ")
        if op.lower() == "s":
            listPeople.append(addInfo())
        elif op.lower() == "n":
            printData(listPeople)
            selectPeople(listPeople)
            break
        else:
            print("\nErro! Opção inválida. Pretende inserir um novo contacto [s/n]")

# globals
listPeople = [] 

# call functions           
addPeople(listPeople)