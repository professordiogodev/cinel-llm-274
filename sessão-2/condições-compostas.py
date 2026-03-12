# Exemplo Simples
idade = 25
tem_bilhete = True
vip = False

# A pessoa só pode entrar no concerto se tiver 18 anos e tiver o bilhete
if idade >= 18 and tem_bilhete:
    print("Pode Entrar")

if vip or idade >= 65:
    print("Entrada Gratuita")

if not tem_bilhete:
    print("Compre o bilhete primeiro")