import random

print("------------------------------------")
print("Bem vindo(a) ao jogo de adivinhação!")
print("------------------------------------")

numero_random = round(random.random() * 100)
int (numero_random)
total_tentativas = 3
rodada = 1

while (rodada <= total_tentativas):
  print("Tentativa {} de {}".format (rodada, total_tentativas))

  chute_str = input("Digite um número: ")
  print("Número digitado: ", chute_str)
  chute = int(chute_str)

  acertou = numero_random == chute
  maior = chute > numero_random
  menor = chute < numero_random

  rodada = rodada + 1

  if (acertou):
    print("Você acertou!")
    break
  else:
    if (maior):
      print("Você errou! O seu chute foi maior que o número secreto.")
    elif (menor):
      print("Você errou! O seu chute foi menor que o número secreto.")

print("Fim do jogo")

