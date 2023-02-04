'''

#ESTRUTURA DE DADOS LISTAS, PILHAS, ARRAYS, SET, ARVORES

LISTAS O PRIMEIRO ITEM A SER ADICIONADO É O PRIMEIRO ITEM NA ORDEM DA ESTRUTUTURA DE DADOS
E O ÚLTIMO ITEM A SER ADICIONADO É O ÚLTIMO ITEM DA ESTRUTURA DE DADOS

PILHA O ÚLTIMO ITEM A SER ADICIONADO É O PRIMEIRO ITEM NA ORDEM DA ESTRUTURA DE DADOS
E O PRIMEIRO ITEM A SER ADICIONADO É O ÚLTIMO ITEM DA ESTRUTURA DE DADOS

ARRAY É UM CONJUNTO DE ELEMENTOS FINITOS E PRE DEFINIDOS NA SUA DECLARAÇÃO
TODO ARRAY POSSIU UM INDICIE E O INDICIE INICIA DO 0 E O ÚLTIMO ELEMENTO DO ARRAY É
TOTAL DE ELEMENTOS -1.

TUPLA É UMA LISTA DEFINITA COMO CONSTANTE, NÃO É POSSIVEL ADICIONAR, ALTERAR OU REMOVER ELEMENTOS
TODA TUPLA SERÁ UM CONJUNTO DE OBJETOS IMUTAVEIS

DICIONÁRIO É A ESTRUTURA NA QUAL CADA ITEM POSSUI UMA CHAVE ÚNICA E UM VALOR

ARVORE
RAIZ: ELEMENTO PERTENCENTE AO NÍVEL UM. TODA ARVORE TÉRA UMA UNICA RAIZ
NÓ/FILHO: ELEMENTO QUE FOI ADICIONADO A OUTRO ITEM
NÍVEL:PROPRIEDADE QUE INDICA QUANTOS NÓS ESTÃOS ACIMA DE UM FILHO
'''

#CLASS LIST I

    #EXEMPLOS DE LISTAS
lista = [1, 2, 4, 5, 6, 6, 10]

print(lista[1])
print(lista[2])
print(lista[3])

l = ['a', 'b', 'c', 'd', 'e', 'f']

print(l[0])
print(l[1])
print(l[2])

lista = list("L-G-TECNOLOGIA-INOVACAO")
print(lista)

lista = list([1, 2, 3, 4, 5])
print(lista)

lista = list(("L-G-TECNOLOGIA-INOVACAO", ))
print(lista)

lista = list([1, 2, 3, 4, 5,])
print(lista)

    #EXEMPLO DE TUPLA
a = (5,)
print(type(a))

#CLASS LIST II

lista = ['a', 3]

lista = [['a','b','c'],[1,2,3],[]]

print(lista)
print(lista[0])
print(lista[1][1])

#MÉTODOS DA CLASS LIST

    #MÉTODO LEN - RETORNA O NÚMERO DE ELEMENTOS DA LISTA
print(len(lista))
print(len("TECNOLOGIA"))

print(lista[len(lista)-1])
print(lista[-1])
print(lista[0][-1])

#CLASS LIST III

    #ADICIONANDO ELEMENTOS A LISTA
lista = [1,2,3,4,5]

lista = lista + [6]
print(lista)

lista =[0] + lista
print(lista)

lista = lista + [7,8,9,10]
print(lista)

lista.append(11)
print(lista)

lista.append([11])
print(lista)

del(lista[-1])
print(lista)

lista = 10*[0]
print(lista)

lista += 10*[0]
print(lista)


lista += 10*[0]
print(lista)

#INTERANDO LISTAS

    #funcao range
lista_nums = [100,200,300,400,500]
for item in range(len(lista_nums)):
    lista_nums[item] +=1000
    print(lista_nums[item])

    #função enumerate

lista_nums = [100,200,300,400,500,600,700,800]
for idx, item in enumerate(lista_nums):
    lista_nums[idx] +=1000
    print(lista_nums[idx])


#FATIANDO LISTAS

# lista[x:y:z] x - start / y - stop / z - step
lista = "Bem-vindo ao curso de Python"

print(lista[10])
print(lista[2])
print(lista[20])
print(lista[:20])
print(lista[10:20:1])
print(lista[::2])
print(lista[::-1])

#INCLUIR, ALTERAR E EXCLUIR ELEMENTOS

lista = ['bbb', 'ccc', 'ddd']
print(lista)

lista.append('eee')#inserindo no final da lista
print(lista)

lista.insert(0,'aaa') #inserindo no início da lista
print(lista)

print(lista[1])
lista[1] = 'bbbb' #alterando o valor do item
print(lista[1])


lista = ['aaa', 'bbb', 'ccc', 'ddd']
lista.clear() #limpando todos os itens da lista
print(lista)

lista = ['aaa', 'bbb', 'ccc', 'ddd']

lista.pop() #excluindo o último item da lista
print(lista)

lista.pop(0) #excluindo o primeiro item da lista
print(lista)

lista.pop(-1) #excluindo o último item da lista
print(lista)

    #funcao DEL - excluindo através de intervalos
lista = ['aaa', 'bbb', 'ccc', 'ddd','eeee']
del(lista[2:4])#excluindo da posicao 2 até 4
print(lista)

lista = ['aaa', 'bbb', 'ccc', 'ddd']
del(lista[::2])
print(lista)

#ORDENAMENTO LISTAS

lista = ['LUCAS', 'GABRIEL', 'SILVA', 'SOUZA', 'TAYNAH', 'COSTA', 'EVA', 'LIMA']
print(lista)

lista.reverse() #reverte a ordem dos itens da lista
print(lista)

lista.sort() #orderna a lista de itens de forma ascendente
print(lista)

lista.sort(reverse=True) #orderna a lista de itens de forma reversa
print(lista)

#QUANTIDADE DE ELEMENTOS EM UMA LISTA

lista = ['LUCAS', 'GABRIEL', 'SILVA', 'SOUZA', 'TAYNAH', 'COSTA', 'EVA', 'LIMA']

print(len(lista)) # retorna a quantidade de elementos da lista ia função len

print(lista[len(lista)-1]) # retorna o último elemento da lista ia função len

print(lista[-1]) # retorna o último elemento alternativa

lista = ['LUCAS', 'GABRIEL', 'SILVA', 'SOUZA', 'TAYNAH', 'COSTA', 'EVA', 'LIMA']

lista.insert(5, 'GABRIEL')
lista.append('GABRIEL')
print(lista)

print(lista.count('GABRIEL')) # retorna quantidade de vezes que 'GABRIEL' está contido na lista

print(lista.index('SILVA')) # retorna a posição do item em que está 'SILVA'


#ESTRUTURA DE DADOS TUPLA
    #exemplo 1
a = tuple('abc')
print(a)
print(type(a))
    #exemplo 2
b = ("aaa", 1, True)
print(b)
print(type(b))

#OPERADORES IN E NOT IN

a = 2 in (1,2,3,4,5,6) # VERIFICANDO SE O NÚMERO 2 ESTÁ CONTIDO NA TUPLA - TRUE
print(a)

a = 7 in (1,2,3,4,5,6) # VERIFICANDO SE O NÚMERO 2 ESTÁ CONTIDO NA TUPLA - FALSE
print(a)


a = 2 not in (1,2,3,4,5,6) # VERIFICANDO SE O NÚMERO 2 NÃO ESTÁ CONTIDO NA TUPLA - TRUE
print(a)

a = 7 not in (1,2,3,4,5,6) # VERIFICANDO SE O NÚMERO 2 NÃO ESTÁ CONTIDO NA TUPLA - FALSE
print(a)

a = 1 in range(1,6,) #TRUE
print(a)

a = 6 in range(1,6,) #FALSE
print(a)

x = range(1,6)
if 3 in x:
    print("O NÚMERO 3 ESTÁ CONTIDO NA LISTA 'X'")
else:
    print("O NÚMERO 3 NÃO ESTÁ CONTIDO NA LISTA")

if 0 in x:
    print("O NÚMERO 3 ESTÁ CONTIDO NA LISTA 'X'")
else:
    print("O NÚMERO 3 NÃO ESTÁ CONTIDO NA LISTA")

#EXEMPLO PRÁTICO SOBRE OPERADOR IN

a = 10
b = 20
c = 30

#EXEMPLO 1
x = int(input("DIGITE UM NÚMERO: "))

if(x == a or x == b or x ==c):
    print("Número está contido")
else:
    print("Número não está contido")

#EXEMPLO 2

x = int(input("DIGITE UM NÚMERO: "))

if(x in [a, b, c]):
    print("Número está contido")
else:
    print("Número não está contido")

#EXEMPLO 3

cores = ["AZUL" , "AMARELO", "VERMELHO", "PRETO"]

while True:
    cor = input("DIGITE O NOME DE UMA COR OU DIGITE 0 PARA ENCERRAR O PROGRAMA:")
    if (cor == '0'):
        break;
    elif (cor in cores):
        print("Está cor está contida")
    else:
        print("Essa cor não está contida")
        cores.append(cor)

print(cores)