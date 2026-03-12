import random

numero = random.randint(1, 10) # [1,10]

while True:
    palpite = int(input("Adivinha o número que eu tenho aqui guardadinho (1-10) -> "))

    if palpite != numero:
        print("Errou xD. Tente outra vez.")
    else:
        print("Parabénsss!!!!!! Acertou!")
        break


