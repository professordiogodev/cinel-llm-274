notas = []

# vamos pedir 5 vezes um número ao utilizador
for i in range(5):
    numero = int(input(f"Insere o número { i + 1 }: "))
    notas.append(numero)

media = sum(notas) / len(notas)

if media >= 10:
    print(f"Aprovou: {media}")
else:
    print(f"Reprovou: {media}")

print(f"Nota mais alta: {max(notas)}")
print(f"Nota mais baixa: {min(notas)}")