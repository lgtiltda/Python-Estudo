#PRIMEIRA CLASSE
class Estudo1:
    pass

#NOMECLATURA DE CLASSES:
    #CamelCase é a prática de escrever palavras ou frases compostas de tal
    # forma que cada palavra comece com letra maiuscúla
    #Exemplo: MinhaClasse(): ConexaoDBMySQL: LeJSON();
    #Exemplo função: faz_isso() / Exemplo Classe: FazIsso()

#CRIAÇÃO DE OBJETOS
    #INSTÂNCIA É CADA UM DOS OBJETOS CRIADOS DURANTE A EXECUÇÃO DO PROGRAMA

class Pessoa():
    pass

p1 = Pessoa()
p2 = Pessoa()

print(id(p1))
print(id(p2))

#MEMBROS DE CLASSE
    #É todo atributo ou função declarada no escopo do bloco da classe
    #PROPRIEDADES: são variáveis que armazenam característica
    #MÉTODOS: são as funções, as ações que o projeto pode realizar
    #EXEMPLO Acessando um Membro: obs.membro

#MÉTODO CONSTRUTOR
    #É invocado automaticamente pelo Python a cada novo objeto criado

class A:
    def __init__(self):
        print(id(self))
A()

    #criando uma nova classe para trabalhar nas propriedades de uma classe
class Retangulo():
    def __init__(self):
        self.a = 0;
        self.l = 0;
    def area(self):
        return  self.a * self.l

r1 = Retangulo()
r1.a = 10;
r1.l = 5;

print(r1.area())

#DECLARAÇÃO DE MEMBROS
    #membros podem ser adicionados a objetos de forma interna ou externa na classe

class Retangulo():
    def area(self):
        return  self.a * self.l

def membros_retangulo(r):
    r.a = 0;
    r.l = 0;

r1 = Retangulo()
membros_retangulo(r1)
r1.a = 10;
r1.l = 5;

print(r1.area())

#PERSONALIZANDO O MÉTODO CONSTRUTOR

class RetanguloExemplo2:
    def __init__(self, altura, largura):
            self.l = largura
            self.a = altura

    def area(self):
        return self.l * self.a

r4 = RetanguloExemplo2(7,5)
print(r4.area())