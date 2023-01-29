# O VALOR AO LADO DIREITO SERÁ ATRIBUÍDO A VARIVÉL DO LADO ESQUERDO
# ATRIBUIÇÃO É '='
# COMPARAÇÃO É '=='


a = 1
z = y = x = a

d = z == z == x == y == a

type (d)


x = 1
x = (x + 1)
x += 1

print (x)

#OPERADORES DE ATRIBUIÇÃO

x = 9
y = 3

x += y
print (x)
x -= y
print (x)

x *= y
print (x)

x /= y
print (x)

x %= y
print (x)

# ATRIBUIÇÃO MULTIPLA

c = 1
d = 2

c, d = d, c

print (c, d)

f, g, h = 4, 5, 6

print (f, g, h)

a, b, c = f*2, f+g, f*g*h
print (a, b, c)

# ATRIBUIÇÃO CONDICIONAL

x = 10;
texto = "Sim" if x == 10 else "Não"

print (texto)

#Testando se um número é PAR

num1 = int(input("Digite uma número!: "))

s = "Par" if num1 % 2 == 0 else "Impar"

print (s)
