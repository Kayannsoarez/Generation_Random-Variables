import random
import math
import matplotlib.pyplot as plt

# inicialização das listas de valores e números aleatórios
valor = []
num = []

# parâmetros da distribuição uniforme
alpha = 3
pi = math.pi

# laço para gerar 10000 variáveis aleatórias
for i in range(10000):
    # gerando um número aleatório uniforme no intervalo (0,1)
    u = random.uniform(0, 1)

    # aplicando a transformação inversa para obter uma amostra da distribuição de Cauchy
    x = alpha * math.tan(pi * (u - 0.5))

    # adição da amostra e número aleatório às listas
    valor.append(x)
    num.append(u)

    # ordenação das listas para plotagem da CDF
    valor.sort()
    num.sort()

# plotando o histograma das variáveis aleatórias geradas
plt.hist(valor, bins=50)
plt.title("Histograma")
plt.show()

# plotando a função de distribuição acumulada (CDF)
plt.plot(valor, num)
plt.title("CDF")
plt.xlim(-50, 50)
plt.ylim(0, 1)
plt.show()
