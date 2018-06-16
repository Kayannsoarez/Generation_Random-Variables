import math
import matplotlib.pyplot as plt

valor = []
num = []

a=3
b=7
h = 4
seed = 10
m = 2**32

for i in range(10000):
   seed = (a * seed + b) % m
   r = seed / m
   w = math.log(1-r)/4*(-1)

   valor.append(w)
   num.append(r)
   valor.sort(reverse=False)
   num.sort(reverse=False)

U = float('%g' % max(valor))
O = float('%g' % max(num))
lb = (-1)*math.log(1-O)/U

E = 1/lb
print("Media {}".format(E))
Var = 1/lb**2
print("Variancia {}".format(Var))

plt.hist(valor,20)
plt.title("Histograma")
plt.show()

plt.plot(valor,num)
plt.title("CDF")
plt.show()
