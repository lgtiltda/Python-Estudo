#EXEMPLO DE DECLARAÇÃO DE STRINGS

string1 = 'EXEMPLO DE STRING 1'
string2 = "EXEMPLO DE STRING 2"
string3 = '''
    EXEMPLO DE STRING ONDE SERÁ DIGITADO UM TEXTO
    AAAAAA
    BBBBBB
    CCCCCC
    DDDDDD
    EEEEEE
'''

print(string1)
print(string2)
print(string3)


#FATIANDO STRING

s = "Para o Python toda string é uma lista imutável"
print(type(s))

print(s[0]) #PRIMEIRO CARACTER DA STRING
print(s[-1]) #ÚLTIMO CARACTER DA STRING


fatia = s[2::] #fatiando passando como parametro apenas o ponto de incio
print(fatia)

fatia = s[1:6:]#fatiando passando como parametro apenas o ponto de incio e final
print(fatia)

fatia = s[2:10:2]#fatiando passando como parametro apenas o ponto de incio, final e intervalo
print(fatia)

fatia = s[::-1]#fatiando passando e retornando a lista reversa
print(fatia)

#COMPARANDO STRING

'''
'a' > 'X' = true
'a' > '1' = true
'a' > '9' = true
'''

print(chr(100)) #retorna o caracter da tabela asc referente ao valor passado como parametro

print(ord("d")) #retorna o valor asc do caracter passado como parametro


for c in range(123):
    valorstring =  str(c)
    caracterasc =  chr(c)
    print(valorstring + ' - ' + caracterasc ) #STRING - VALOR EM ASC

#PROPRIEDADES DA STRING

s = "Lista de Caracteres"
print(len(s)) #retorna o numero de caracteres na STRING

#QUEBRANDO UMA STRINSG

lista = s.split(" ") #retorna a lista em uma nova lista

lista2 = s.replace("de", "") #substitui uma string por outra

print(lista)
print(lista2)


print(id(s))#UM DETERMINADO OBJETO
print(id(lista2)) #UM NOVO OBJETIVO

#INTERANDO STRING

    #exemplo 1
s = "Interando String"
for c in s:
    print(c)

    #exemplo 2
indice = 0
while indice < len(s):
    print(indice, s[indice])
    indice += 1

    #exemplo 3
for k,v in enumerate('Interando String'):
    print(k + ' - '  +  v)