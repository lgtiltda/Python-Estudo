#TOMADA DE DECISÃO ATRAVÉS DE PARÂMETRO ENVIADO PELO USUÁRIO
acao = int(input("Digite '1' para Sim e Digite '2' para não:"))
if(acao == 1):
    print ("Você disse que sim")
else:
    if(acao == 2):
        print ("Você disse que não")
    else:
        print ("O número digitado não é '1' e nem igual a '2'")
