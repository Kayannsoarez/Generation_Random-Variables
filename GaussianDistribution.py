import random
import math
import matplotlib.pyplot as plt

# inicialização das listas de valores e números aleatórios
valor = []
num = []
cdf = []

# parâmetros da distribuição normal
u = 2
g = 3
pi = math.pi
soma = 0
total = 0
n = 10000

# Gerador de números aleatórios a partir de uma distribuição normal padrão
def Gaussian():
    while True:
        x = random.uniform(0, 1)
        y = random.uniform(0, 1)
        w = math.sqrt(-2.0 * math.log(x)) * math.cos(2 * pi * y)
        z = math.sqrt(-2.0 * math.log(x)) * math.sin(2 * pi * y)
        yield w

# Instanciação do gerador de números aleatórios a partir da distribuição normal padrão
gaussian_gen = Gaussian()  

# laço para gerar 10000 variáveis aleatórias
for i in range(n):
    # Geração da amostra a partir da distribuição normal com média u e desvio padrão g
    k = next(gaussian_gen) * g + u

    # Adiciona a amostra na lista de valores
    valor.append(k)
    # ordenação das listas para plotagem da CDF
    valor.sort(reverse=False)

# Calcula a soma das amostras geradas
soma = sum(valor)
# Calcula a média das amostras
media = soma / n  
print("Média:", media)

# Laço para calcular a variância
for i in range(n):
    total += (valor[i] - media) ** 2

# Calcula a variância das amostras
variancia = math.sqrt(total / n)
print("Variância:", variancia)

# plotando o histograma das variáveis aleatórias geradas
plt.hist(valor, 20)
plt.title("Histograma")
plt.show()

# Laço para calcular a CDF
for v in valor:
    # Cálculo da probabilidade de ocorrência de cada amostra na distribuição e adição na lista
    cdf.append(sum([1 for i in valor if i <= v])/n)

# plotando a função de distribuição acumulada (CDF)
plt.plot(valor, cdf)
plt.title("CDF")
plt.show()
