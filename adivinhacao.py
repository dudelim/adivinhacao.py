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
  print ("Você errou!")
