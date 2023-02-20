#INTRODUÇÃO A EXCEÇÕES

'''
Tratamento de exceções: é todo código de identifica erros e implementa uma solução
evitando que a implementação seja finalizada

Levantamento de exceções: é todo código que ao perceber um problema cria um exceção
avisando o programador

'''

try:
    a = 10 / 0
    print(a)
except ZeroDivisionError:
    print("Não e possível dividir um número por zero")


#VALORES INVÁLIDOS

def input_float(msg):
    while True:
        try:
            return float(input(msg))
        except ValueError:
            print("Número Inválido")

num1 = input_float("Digite o primeiro número:")
num2 = input_float("Digite o segundo número:")

try:
    print(num1 / num2)
except ZeroDivisionError:
    print("Não é possível dividir um número por zero")

#TRATAMENTO DE EXCEÇÕES MÚLTIPLAS I

def erro(x):
    try:
        eval(x)
    except TypeError:
        print("TypeError")
    except NameError:
        print("NameError")
    except ValueError:
        print("ValueError")
    except ZeroDivisionError:
        print("ZeroDivisionError")
#TypeError
erro("int+int")
#NameError
erro("NError+BError")
#ValueErro
erro("int('a')")
#ZeroDivisionError
erro("10/0")

erro("10+10")

print(eval("10+10"))


#TRATAMENTO DE EXCEÇÕES MÚLTIPLAS II


def erro(x):
    try:
        eval(x)
    except (TypeError, NameError):
        print("TypeError ou NameError")
    except ValueError:
        print("ValueError")
    except ZeroDivisionError:
        print("ZeroDivisionError")
#TypeError
erro("int+int")
#NameError
erro("NError+BError")
#ValueErro
erro("int('a')")
#ZeroDivisionError
erro("10/0")


#BLOCO DE EXCEÇÃO ELSE


def erro(x):
    try:
        eval(x)
    except (TypeError, NameError):
        print("TypeError ou NameError")
    except ValueError:
        print("ValueError")
    except ZeroDivisionError:
        print("ZeroDivisionError")
    else:
        print("Nenhuma exceção ocorreu")

#TypeError
erro("int+int")
#NameError
erro("NError+BError")
#ValueErro
erro("int('a')")
#ZeroDivisionError
erro("10/0")

#BLOCO DE EXCEÇÃO FINALLY

def erro(x):
    try:
        eval(x)
    except (TypeError, NameError):
        print("TypeError ou NameError")
    except ValueError:
        print("ValueError")
    except ZeroDivisionError:
        print("ZeroDivisionError")
    finally:
        print("Esse bloco de execução sempre será executado ao final do 'try'")

#TypeError
erro("int+int")
#NameError
erro("NError+BError")
#ValueErro
erro("int('a')")
#ZeroDivisionError
erro("10/0")

