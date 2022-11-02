import random

def jogar():

  print("***********************************")
  print("Bem vindo ao jogo de adivinhação!")
  print("***********************************")

  numero_secreto = random.randrange(1,51) #(50) de 1 a 50 da mesma forma que está escrito.
  total_de_tentativas = 0
  pontos = 100

  print(numero_secreto)
  print("Qual o nível de dificuldade?\n[1]-Fácil [2]-Médio [3]-Difícil\n")

  nivel = int(input("Defina o nível: "))

  if(nivel == 1):
    total_de_tentativas = 15
  elif(nivel == 2):
    total_de_tentativas = 8
  else:
    total_de_tentativas = 4


  for rodada in range(1, total_de_tentativas + 1):
      # print("Tentativa: ", rodada, "de", total_de_tentativas)
      print("Tentativa {} de {} ".format(rodada, total_de_tentativas)) #String interpulation
      
      chute_str = input("Digite um número de 1 a 50: ")
      print("Você digitou: ", chute_str)
      chute = int(chute_str)

      if(chute < 1 or chute > 50):
        print("Você deve digitar um número entre 1 e 50!")
        continue

      acertou = chute == numero_secreto
      maior = chute > numero_secreto
      menor = chute < numero_secreto

      if (acertou):
          print("Você acertou! Sua pontuação foi de {} ." .format(pontos))
          break
      else:
          if(maior):
            print("O seu chute foi maior do que o número secreto.")
            if(rodada == total_de_tentativas):
              print("O número era {}. Você fez {}pts!" .format(numero_secreto, pontos))
          
          elif(menor):
            print("O seu chute foi menor do que o número secreto.")
            if(rodada == total_de_tentativas):
              print("O número era {}. Você fez {}pts!" .format(numero_secreto, pontos))
          
          pontos_perdidos = abs(numero_secreto - chute)
          pontos = pontos - pontos_perdidos
        
      

  print("\nFim do jogo")

if(__name__ == "__main__"):
  jogar()