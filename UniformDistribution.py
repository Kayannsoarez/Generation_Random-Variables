import matplotlib.pyplot as plt

# inicialização das listas de valores e números aleatórios
valor = []
num = []

# parâmetros da distribuição uniforme
a = 3
b = 7

# inicialização da semente do gerador de números aleatórios e do módulo
m = 2**32
seed = 10

# laço para gerar 10000 variáveis aleatórias
for i in range(10000):
    # gerando um novo número aleatório utilizando a fórmula do congruente linear
    seed = (a*seed+b)%m
    r = seed/m
    X = a+(b-a)*r

    # adicionando o valor da variável aleatória na lista "valor"
    valor.append(X)
    
    # adicionando o número aleatório na lista "num"
    num.append(r)

# cálculo da média e variância teóricas da distribuição uniforme
E  = (max(valor) - min(valor))/2 + min(valor)
Var = ((max(valor) - min(valor))**2)/12

print("Media {}".format(E))
print("Variancia {}".format(Var))

# plotando o histograma das variáveis aleatórias geradas
plt.hist(valor,20)
plt.title("Histograma")
plt.show()

# plotando a função de distribuição acumulada (CDF)
plt.plot(valor,num)
plt.title("CDF")
plt.show()
