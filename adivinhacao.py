print("------------------------------------")
print("Bem vindo(a) ao jogo de adivinhação!")
print("------------------------------------")

numero_secreto = 16
chute_str = input("Digite um número: ")

chute = int(chute_str)

print("Número digitado:", chute_str)
if (numero_secreto == chute):
  print ("Você acertou!")
else:
  if(chute > numero_secreto):
    print ("Você errou! O seu chute foi maior do que o número secreto.")
  else:
    print("Você errou! O seu chute foi menor do que o número secreto.")
