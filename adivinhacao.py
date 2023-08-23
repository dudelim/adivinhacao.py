import random

print("------------------------------------")
print("Bem vindo(a) ao jogo de adivinhação!")
print("------------------------------------")

numero_random = random.randrange(1,101)
total_tentativas = 0

print("Selecione o nível de dificuldade")
print("(1) Fácil (2) Médio (3) Difícil")
nivel = int(input("Nível selecionado: "))

if (nivel == 1):
  total_tentativas = 20
elif(nivel == 2):
  total_tentativas = 10
elif(nivel == 3):
  total_tentativas = 5

for rodada in range(1, total_tentativas + 1):
  print("Tentativa {} de {}".format (rodada, total_tentativas))

  chute = int(input("Digite um número entre 1 e 100: "))
  print("Número digitado: ", chute)
  

  if(chute < 1 or chute > 100):
    print("Você deve digitar um número entre 1 e 100!")

  acertou = numero_random == chute
  maior = chute > numero_random
  menor = chute < numero_random

  if (acertou):
    print("Você acertou!")
    break
  else:
    if (maior):
      print("Você errou! O seu chute foi maior que o número secreto.")
    elif (menor):
      print("Você errou! O seu chute foi menor que o número secreto.")

print("Fim do jogo")

