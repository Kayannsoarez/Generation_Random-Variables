import random
import math
import matplotlib.pyplot as plt

valor = []
num = []
a = 3
pi = math.pi

for i in range(10000):
    x = random.uniform(0, 1)
    w = 3*math.tan(x*pi - pi/2)

    valor.append(w)
    valor.sort(reverse=False)
    num.append(x)
    num.sort(reverse=False)

    print(x)

plt.hist(valor)
plt.title("Histograma")
plt.show()

plt.plot(valor, num)
plt.title("CDF")
plt.xlim(-50, 50)
plt.ylim(0, 1)
plt.show()
