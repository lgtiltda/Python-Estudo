#INTRODUÇÃO AS FUNÇÕES

def minha_primeira_funcao():
    print("Bem-vindo a programação Python")

minha_primeira_funcao()

#PARAMETROS

def soma(x,y):
    total = x + y
    print ("O total da soma de x + y é: ", total)

param1 = 10 # int(input("Digite o Valor de X:"))
param2 = 40 # int(input("Digite o Valor de Y:"))

soma(param1, param2)

#PARAMETROS DEFAULT

def login(sistema, usuario="UsuarioLogin", senha="123123123"):
    print("O usuário digitado é: ", usuario)
    print("A senha digitada é: ", senha)
    if(sistema == 1):
        print("Sistema de Consulta")
    elif(sistema ==2):
        print("Sistema de Cadastrado")

login(2) #com parametros padrão
login(1, "LucasGabriel", "NovaSenha") #com todos os parametros

#ARGUMENTOS NOMEADOS

def dados_pessoais(nome, sobrenome, idade, sexo):
    print("Nome: {}\nSobrenome: {}\nIdade: {}\nSexo: {}"
          .format(nome, sobrenome, idade, sexo))

dados_pessoais("Lucas", "Gabriel", 30, True) #enviando os parametros de forma posicional

dados_pessoais(nome="Lucas",
               sobrenome="Gabriel",
               sexo=True,
               idade=30) #enviando os parametros de forma nomeada

#RETORNO DE VALORES

def multiplicando_valores(x,y):
    novo_valor = x*y
    return novo_valor

print(multiplicando_valores(10,20))

#RETORNO DE VALORES MULTIPLOS

def funcao():
    return 1, 2

a, b = funcao()

print(a)
print(b)


#numeros_testar = int(input("Digite um número e verifique quais são os pares em seu intervalo: "))
numeros_testar = 10
def funcao_teste(numeros): #funcao para retornar uma sequencia de numeros pares
    num_test = 0 #declracao de variaveis
    lista_par = [] #declaracao  de variaveis
    for num_test in range(1, numeros): #funcao para percorrer uma lista de 0 até o número inserido pelo usuario
        if(num_test%2==0): #verificação se o número é par
            lista_par.append(num_test) #adicionado resultado true a lista de números pares
    return lista_par #retornando lista de numeros pares
print(funcao_teste(numeros_testar)) #mostrando números pares

def potencia(x): # funcao para calcular potencia de um valor e retornar o quadrado e cubo
    quadrado=x**2 #calculo do quadrado
    cubo=x**3 #calculo do cubo
    return (quadrado,cubo) #retornando o resultado do calculo
q, c = potencia(10)
print(q)#valor do quadrado do parametro
print(c)#valor do cubo do parametro

#FUNÇÃO VARIÁDICA

#def func(*args, **kwargs):
#     pass

def lista_de_argumentos(*args): #declaração de uma função variádica argumentos
    print(args)

lista_de_argumentos(1,2,3,4,5,6,7,8)
lista_de_argumentos("um", "dois", "tres", "quatro")

def lista_de_argumentos_associativos(**kwargs): #declaração de uma função variádica dicionários
    print(kwargs)

lista_de_argumentos_associativos(a=1, b=2, c=3, d=4)
lista_de_argumentos_associativos(um=1, dois=2, tres=3, quatro=4)

def argumentos(*args, **kwargs):
    print(args)
    print(kwargs)

argumentos(1,2,3,4,5, um=1, dois=2, tres=3, quatro=4)

#DESEMPACOTAMENTO I

    #Extração dos elementos contidos em uma estrutura


lista = [10,20]

def funcao(a,b):
    print(a, b)

funcao(*lista)
funcao(10,20)
funcao(a=1, b=2)

    #Atribuição múltipla

lista2= [10,20]
x,y = lista2

def pessoa (nome, sobrenome, idade ):
    print(nome)
    print(sobrenome)
    print(idade)

tupla = ("LG TECNOLOGIA", "INOVAÇÃO", 2)
lista3 = ["LG TECNOLOGIA", "INOVAÇÃO", 2]
d = {
    "nome":"LG TECNOLOGIA", "sobrenome":"INOVAÇÃO","idade":2
}
pessoa(tupla[0], tupla[1], tupla[2])
pessoa(*tupla) #enviando uma tupla como parametro
pessoa(*lista3) #enviando uma lista como parametro
pessoa(**d) #enviando um dicionario como parametro


#DESEMPACOTAMENTO II

    #exemplo de desempacotamento

lista = [10, 11, 12]
tupla = (10, 5, 15)


def func (a, b, c):
    print(a)
    print(b)
    print(c)

lista.sort()
func(*lista)

l = [*tupla]
l.sort()
func(*l)

func (**dict(zip(("b", "a", "c"),lista)))

#FUNÇÕES ANINHADAS

def func_aninhadas():
    print("func")

    def func_interna(): #essa funcao somente podera ser evocada em dentro da funcao aninhadas
        print("func_interna")

    func_interna()

func_aninhadas()

#INTRUÇÃO NONLOCAL

#Instrução que permite acessar membros não globais e não locais, membros contidos no escopo externo

def func_nonlocal():
    var_local = 0
    def func_interna():
        nonlocal var_local
        var_local += 1
        print(var_local)

    func_interna()

func_nonlocal()

teste_global = "Teste para uma variavel global"

def funcX():
    global teste_global
    return teste_global

print(funcX())


#BLOCOS SEM CÓDIGO

pass #funcao usada para indicar ao python que nenhum código será executado no bloco de código

print("aaa")

def func_pass():
    pass



#INSTRUÇÃO GLOBAL

x_local = 10
print(x_local)

def func_teste_local():
    global x_local
    x_local = 50
    print(x_local)

func_teste_local()
print(x_local)