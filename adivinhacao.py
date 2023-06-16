print("*********************************")
print("Bem vindo ao jogo de advinhação!")
print("*********************************")

numero_secreto = 42

chute_str = input("Digite seu número: ")
print("Você digitou ", chute_str)
chute = int(chute_str)

if (chute == numero_secreto):
    print("Parabéns você acertou!")
else:
    print("Você errou!")

