import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return np.square(np.sin(x-2))*np.exp(-1*np.square(x))

x1 = np.linspace(0,2,1024)

plt.plot(x1,f(x1))
plt.ylabel('y axis')
plt.xlabel('x axis')
plt.show()

