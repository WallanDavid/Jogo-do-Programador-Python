# Desafio: Contar o número de tábuas soltas na ponte.

tabuas = ["solta", "firme", "firme", "solta", "firme", "solta"]
contagem_solta = 0

for tabua in tabuas:
    if tabua == "solta":
        contagem_solta += 1

# Imprima o número de tábuas soltas
print("Número de tábuas soltas:", contagem_solta)