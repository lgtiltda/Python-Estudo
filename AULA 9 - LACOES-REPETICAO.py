#EXEMPLO 1
x = 0
while (x<10):
    print(x)
    x+= 1

#LAÇOS DE REPETIÇÃO WHILE ELSE
x = 0
print ("While")
while (x<5):
    print(x)
    x = x + 1;
else:
    print ("Else")
print ("Fim")

#LAÇOS DE REPETIÇÃO FOR LOOP:
for i in "eXscrip":
    print(i)

#LAÇOS DE REPETIÇÃO FOR LOOP - FUNÇÃO RANGE:
# range([star], stop[, step])

for i in range(10):
    print(i)

print(list(range(0, 100, 3)))

print(list(range(1, 10)))

print(list(range(10)))

print(list(range(100, 1, -3)))

print(list(range(-100, 1, 3)))

#LAÇO FOR E FUNÇÃO RANGE

for i in range(1, 10, 2):
    print(i)

#INSTRUÇÃO BREAK
print("Antes de entrar no Laço")
for item in range(10):
    print(item)
    if(item==6):
        break
print("Depois de entrado no Laço")

#INSTRUÇÃO CONTINUE

print()
print("inicio")
i = 1
while(i<10):
    i += 1
    if(i%2==0):
        continue
    print(i)
else:
    print("Else")
print("Fim")
