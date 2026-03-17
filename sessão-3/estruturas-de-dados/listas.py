# Começar com uma lista
numeros = [5, 6, 7, 8]

# Adicionar um elemento
numeros.append(20)

# [5, 6, 7, 8, 20]

# Imprimir o primeiro elemento: numeros[0]
# Imprimir o segundo elemento: numeros[1]
# Imprimir o último elemento: numeros[-1]

# Imprimir os elementos todos
print(numeros)

# Imprimir o primeiro e o segundo número
print(numeros[1:3]) # Imprimir o segundo e o terceiro elemento
print(numeros[2:]) # Imprimir tudo a partir do terceiro elemento
print(numeros[:2]) # Imprimir tudo até ao segundo elemento


for numero in numeros:
    print(numero * 2)

# Exercício (apenas utilizando fors e listas):
# 1. Imprimir apenas os números maiores ou iguais a sete
# 2. Imprimir a média de todos os números
# 3. Imprimir apenas os números ímpares


