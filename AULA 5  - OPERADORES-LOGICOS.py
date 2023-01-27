'''
and - e
or - oi
not - negação
is - é
is not - não é
in - está contido
in not - não está contido
'''
if(2<4 and 2==4):
    print("APENAS UMA DAS CONDIÇÕES É VERDADEIRA, ENTÃO O RESULTADO É TRUE")
else:
    print("APENAS UMA DAS CONDIÇÕES É VERDADEIRA, ENTÃO O RESULTADO É FALSE")

if(2<4 or 2==4):
    print("SENDO UMA DAS CONDIÇÕES É VERDADEIRA, ENTÃO O RESULTADO É TRUE")
else:
    print("SENDO UMA DAS CONDIÇÕES É VERDADEIRA, ENTÃO O RESULTADO É FALSE")

if(not(2<4 or 2==4)):
    print("SENDO UMA DAS CONDIÇÕES É VERDADEIRA E O OPERADOR LOGICO DE NEGAÇÃO, ENTÃO O RESULTADO É TRUE")
else:
    print("SENDO UMA DAS CONDIÇÕES É VERDADEIRA E O OPERADOR LOGICO DE NEGAÇÃO, ENTÃO O RESULTADO É FALSE")

if(2 is 2):
    print("SENDO A CONDIÇAO É VERDADEIRA, ENTÃO O RESULTADO É TRUE")
else:
    print("SENDO A CONDIÇÃO É VERDADEIRA, ENTÃO O RESULTADO É FALSE")

if(type(2) is int):
    print("SENDO A CONDIÇAO É VERDADEIRA, ENTÃO O RESULTADO É TRUE")
else:
    print("SENDO A CONDIÇÃO É VERDADEIRA, ENTÃO O RESULTADO É FALSE")
