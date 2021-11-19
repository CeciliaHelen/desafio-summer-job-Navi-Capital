#Questão 02
import math

#função de preenchimento do vetor x
def fillVector(vector):
  #criação
  for i in range (0,10):
    if(i % 2 == 0):
      pair = (3**i) + (7*math.factorial(i))
      vector.append(pair)
    else:
      odd = (2**i) + (4*math.log(i))
      vector.append(odd)

#função de cálculo da média
def average(vector):
  averageValue = (math.fsum(vector))/10
  print("Average: %.2f" % averageValue)

#função para encontrar o maior número dentro do vetor x
def positionHighestNumber(vector):
  higherNumber = max(vector)
  positionNumber = vector.index(higherNumber)
  print(f"Maximum index: {positionNumber}")


def main():
  #criação do vetor x
  x = []
  #passagem de x pelas funções desejadas
  fillVector(x)
  average(x)
  positionHighestNumber(x)

if __name__ == "__main__":
  main()