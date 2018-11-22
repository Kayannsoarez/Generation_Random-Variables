import matplotlib.pyplot as plt

valor = []
num = []

a = 3
b = 7
m = 2**32
seed = 10

for i in range(10000):
    seed = (a*seed+b)%m
    r = seed/m
    X = a+(b-a)*r

    valor.append(X)
    num.append(r)

E  = (max(valor) - min(valor))/2 + min(valor)
Var = ((max(valor) - min(valor))**2)/12

print("Media {}".format(E))
print("Variancia {}".format(Var))

plt.hist(valor,20)
plt.title("Histograma")
plt.show()

plt.plot(valor,num)
plt.title("CDF")
plt.show()
