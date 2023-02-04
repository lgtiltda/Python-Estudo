#DICIONÁRIOS NA PRÁTICA

dic  = {} # DECLARAÇÃO DE UM DICIONÁRIO EM PYTHON

print(type(dic))

dic['aaa'] = 1000

print(dic)
print(type(dic))

dic['bbb'] = 2000

print(dic)

dic['ccc'] = 3000

print(dic)

print(dic['aaa'])


dic2 = {1.1:'TESTE1', 2.2:'TESTEaaa', 3:'TESTE3333'}
print(dic2)

print(dic2[1.1])
print(dic2[2.2])
print(dic2[3])

#FUNCOES DOS DICIONARIOS

tel = {}
tel = {
    5445454:'LUCAS GABRIEL',
    4123122:'TAYNAH COSTA',
    3123123:'EVA COSTA',
    2312312:'ARLETE'
}
print(tel)

len(tel) #retorna o numero de elementos do dicionario
del(tel[4123122]) #deleta o elemento do dicionario


print(tel.keys()) #retorna a lista de chaves
print(tel.values()) #retorna a lista de valores

print(tel.get(3123123)) #retorna o valor que esta associado a essa chave

tel = {
    5445454:'LUCAS GABRIEL',
    4123122:'TAYNAH COSTA',
    3123123:'EVA COSTA',
    2312312:'ARLETE'
}
print(tel.popitem()) #retorna o item aleatoriamento e exclui ele apos a consulta
print(tel)#dicionário já excluido

if(4123122 in tel):
    print("ESTÁ CONTIDO")

if(412312212 in tel):
    print("TRUE")
else:
    print("NÃO ESTÁ CONTIDO")

tel2 = {

    5445424: 'EXEMPLO 1',
    4123112: 'EXEMPLO 2',
    3123193: 'EXEMPLO 3',
    2312382: 'EXEMPLO 4'
}

tel.update(tel2) #ADICIONANDO NOVOS ELEMENTOS AO DICIONARIO

print(tel)

t = (10,10,10)

tel[t] = "Estudando Python"

print(tel)
