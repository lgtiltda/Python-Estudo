#OPERADORES PARA VERIFICAR CONDIÇÕES E JULGAREM SE ELAS SÃO VERDADEIRAS OU FALASAS

'''
MAIOR QUE >
MENOR QUE <
MAIOR OU IGUAL >=
MENOR OU IGUAL <=

'''
idade = int (input("Digite sua idade:"));

if (idade <=0):
    print("A sua idade não pode ser menor que 0!");
elif (idade >=150):
    print("A sua idade não pode ser maior que 150 anos!");
elif(idade<18):
    print("Você precisa ser maior de 18 anos!");


