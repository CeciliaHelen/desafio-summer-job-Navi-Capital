# Questão 01

#função responsável por realizar os testes de pares e múltiplos dentro do intervalo desejado
def conditionTest(limite_inferior, limite_superior):

  #atribuição dos valores da variável para uso no while
  i = limite_inferior

  #variáveis de iteração:
  j = k = l = 0

  #looping que analisará cada número dentro do limite de valores dado (1,500000)
  while (i <= limite_superior):
    #verifica se o número passado pela variável é par
    #se for par, itera +1 a cada número par e armazena o novo valor na variável j
    if (i % 2 == 0):
      j += 1
    #verifica se o número passado pela variável é múltiplo de 49
    #se for múltiplo de 49, itera +1 a cada número par e armazena o novo valor na variável j
    elif (i % 49 == 0):
      k += 1
    #verifica se o número passado pela variável é múltiplo de 37
    #se for múltiplo de 37, itera +1 a cada número par e armazena o novo valor na variável j
    elif (i % 37 == 0):
      l += 1
    #itera +1 a cada verificação
    i += 1
  #mostra os valores finais de cada variável
  print(j, k, l)

#função main que fará chamada da função de testagem das condicionais
def main():
  conditionTest(1, 500000)

if __name__ == "__main__":
  main()
