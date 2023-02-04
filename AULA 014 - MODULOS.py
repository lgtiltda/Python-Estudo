#MODULOS SAO ARQUIVOS QUE CONTÉM CÓDIGO PYTHON EM EXTENSÃO .py
#UM CONJUNTO DE MODULOS PODEM DAR ORIGEM A UM PACOTE
#BIBLIOTECA PADRÃO É UM COJUNTO DE MÓDULOS CONTIDOS NA DISTRIBUIÇÃO OFICIAL

#ESCOPO DE TABELA DE SÍMBOLOS

#globals() resulta na tabela de simbolos globais do 'main' exibida como dicionário
#dir() outra forma de acessar tabgela de simbolos exibida como listaa
#__builtins__ resulta em todos os modulos nativo do python que não precisam ser importados, e podem ser usados em qualquer parte do código

a = 0

l = list()

for x in [1,2]:
    b = 0

c = 0

#print(varivavel_teste) # teste para variavel local


#IMPORTANDO MÓDULOS

#Importação de módulos é a maneira mais simples de reutilizar códigos

#modulo.attr (objeto e propriedade)

import math #importando a biblioteca matemática

x = 0

var_e = math.e
var_pi = math.pi

print(var_e)
print(var_pi)


#IMPORTAÇÃO DE SÍMBOLOS


def func_teste_fact():
    from math import factorial
    print(factorial(10))

func_teste_fact()

from math import pi, e #importando o símobolo 'e' e 'pi' dentro do modulo 'math'
from math import sqrt #square - importando a função dentro do modulo 'math'

print(pi)
print(e)
print(sqrt(9))

from math import * #importando todos os simbolos do modulo 'math'

math.e
math.cos(100)

#MODULO 'main'
#MARCAR PASTA COMO 'SOURCE'

import modulos_estudo

print("O programa acabou")

#LOCALIZAÇÃO DE MÓDULOS

'''
-DIRETORIO BASE
-DIRETORIO DA VARIAVEL PYTHONPATH
-DIRETÓRIO DA BIBLIOTECA PADRÃO
-DIRETÓRIO DEFINIDOS POR ARQUIVOS *.pth
'''
#exemplo 1 para exibir os diretório principal
from pprint import pprint
from sys import path as lpath

pprint(lpath)

#exemplo 1 para exibir os diretório principal
import sys

pprint(sys.path)


#exemplo para adicionar um diretório a path principal
sys.path.insert(0, "C:\\dev\\excript\\app-comerciais-kivy\\tmp")


#ETAPAS DE IMPORTAÇÃO

'''
-LOCALIZAÇÃO
-COMPILAÇÃO
-EXECUÇÃO
'''

#SÍMBOLOS PRIVADAOS

#print(_a) #simbolos de uso retristo do interpretador

#SÍMBOLOS PUBLICOS

from modulos import simbolos_publicos

pprint(globals())

#MODULO PRINCIPAL

from modulos import modulo_principal

print(__name__)

if __name__ == "__main__":
    print("O programa executou")

'''
Nomaclatura dos módulos
A nomeclatura dos módulos segue a mesma regra das variavéis e funções
'''
#import list - não é permitido nomear um módulo com mesmo nome dos modulos nativo do python

#RECARRECAGAMENTO DE MÓDULOS

import importlib
import recarregamento_modulo

recarregamento_modulo.q = 0
print(recarregamento_modulo.w)

del (recarregamento_modulo.w)

importlib.reload(recarregamento_modulo)
