# ESCOPO 1 - GLOBAL
a = 50
b = 100

def soma_num (var1, var2):
    # ESCOPO 2 - LOCAL
    s = var1 + var2
    return s

def imprime (x_vezes):
    # ESCOPO 3 - LOCAL
    for i in range (x_vezes):
        # ESCOPO 4 - LOCAL 
        print(i)

print (soma_num(a,b))
imprime(5)