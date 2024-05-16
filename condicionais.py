# Desafio: Responder corretamente à pergunta do dragão.

pergunta = "Qual é a cor do céu?"
opcao1 = "1. Vermelho"
opcao2 = "2. Azul"
opcao3 = "3. Verde"

print(pergunta)
print(opcao1)
print(opcao2)
print(opcao3)

resposta = input("Escolha a opção correta (1, 2 ou 3): ")

if resposta == "1":
    print("Resposta incorreta! Tente novamente.")
elif resposta == "2":
    print("Resposta correta! Você pode passar.")
else:
    print("Resposta incorreta! Tente novamente.")