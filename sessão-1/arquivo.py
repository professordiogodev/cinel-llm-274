# calculadora.py
a = float(input("Primeiro número: "))
b = float(input("Segundo número: "))
operacao = input("Operação (+, -, *, /): ")

if operacao == "+":
    resultado = a + b
elif operacao == "-":
    resultado = a - b
elif operacao == "*":
    resultado = a * b
elif operacao == "/":
    resultado = a / b if b != 0 else "Erro: divisão por zero"
else:
    resultado = "Operação inválida"

print(f"Resultado: {resultado}")