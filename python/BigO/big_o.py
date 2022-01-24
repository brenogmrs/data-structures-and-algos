# O(n)
# se n = 10, a função tem 11 passos
# complexidade linear 
# quanto maior o input de dados, maior o tempo de execução.

def soma(n):
  soma = 0
  for i in range(n + 1):
    soma += i
  
  return soma

# O(1)
# sempre 3 passos
# complexidade constante 
# o tamanho do input não interfere no tempo de execução.
def soma_linear(n):
  return (n * (n + 1)) / 2