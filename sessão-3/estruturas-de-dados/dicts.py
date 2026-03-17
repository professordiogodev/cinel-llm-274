

cadeira = {
    "tipo_madeira": "cerejeira",
    "pernas": 4
}

print(f"Esta cadeira tem { cadeira["pernas"] } perninhas.")

# Adicionar propriedades ao dicionário
cadeira["altura"] = 1.2
cadeira["largura"] = 0.9
cadeira["comprimento"] = 1.1

# 2. Calcular o volume da cadeira
volume = cadeira["altura"] * cadeira["largura"] * cadeira["comprimento"]
print(f"Volume da cadeira: {round(volume, 2)} m3.")
