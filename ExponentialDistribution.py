import math
import matplotlib.pyplot as plt

# inicialização das listas de valores e números aleatórios
valor = []
num = []

# parâmetros da distribuição exponencial
h = 4
a = 3
b = 7

# inicialização da semente do gerador de números aleatórios e do módulo
seed = 10
m = 2**32

# laço para gerar 10000 variáveis aleatórias
for i in range(10000):
   # gerando um novo número aleatório utilizando a fórmula do congruente linear
   seed = (a * seed + b) % m
   r = seed / m

   # cálculo do valor da amostra com distribuição exponencial
   w = math.log(1-r)/h*(-1)

   # adição da amostra e número aleatório às listas
   valor.append(w)
   num.append(r)

   # ordenação das listas para plotagem da CDF
   valor.sort(reverse=False)
   num.sort(reverse=False)

# cálculo da média e variância teóricas
U = float('%g' % max(valor))
O = float('%g' % max(num))
lb = (-1)*math.log(1-O)/U

E = 1/lb
print("Media {}".format(E))
Var = 1/lb**2
print("Variancia {}".format(Var))

# plotando o histograma das variáveis aleatórias geradas
plt.hist(valor,20)
plt.title("Histograma")
plt.show()

# plotando a função de distribuição acumulada (CDF)
plt.plot(valor,num)
plt.title("CDF")
plt.show()
