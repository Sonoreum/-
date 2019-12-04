import matplotlib.pyplot as plt
import numpy as np
import math
from mpl_toolkits import mplot3d


plt.style.use('classic')
x = np.linspace(-10, 10, 100)


def func(x,a,b):        #Функция, расчитывающая значение
    F = (x**b + a**b)/ x ** b
    np.seterr(all = 'ignore') # игнорирование всех исключений
    return F

fig = plt.figure(figsize = (13,13))     #Первая фигура Задание 1 (графики в одной системе координат)
plt.plot(x, func(x,1,1), color = 'g', label = 'a = 1, b = 1')
plt.plot(x, func(x,2,1), '--r', label = 'a = 2, b = 1')
plt.plot(x, func(x,1,2), ':k', label = 'a = 1, b = 2')
plt.plot(x, func(x,2,2), linestyle = 'dashdot', color = 'black', label = 'a = 2, b = 2')
plt.title('F = (x**b + a**b) / x**b')
plt.xlabel('x')
plt.ylabel('F')
plt.legend()
plt.show()


fig2 = plt.figure(figsize = (13,13)) # Вторая фигура задание 1 (графики в одной системе координат)
plt.plot(x, func(x,1,0.5), color = 'g', label = 'a = 1, b = 0.5')
plt.plot(x, func(x,1,-0), '--r', label = 'a = 2, b = -0')
plt.plot(x, func(x,1,-1.5), ':k', label = 'a = 1, b = -1.5')
plt.title('F = (x**b + a**b) / x**b')
plt.xlabel('x')
plt.ylabel('F')
plt.legend()
plt.show()


fig3 = plt.figure(figsize = (13,13)) # Первая фигура задание 2 (гистограммы)
data = np.random.normal(0, 10, 140)
plt.hist(data, histtype = 'step')
plt.show()


fig4 = plt.figure(figsize = (13,13)) # Вторая фигура задание 2 (гистограммы)
plt.hist(data, histtype = 'barstacked',orientation = 'horizontal', color = 'g')
plt.show()



x = np.linspace(-10,10, 100)

fig5 = plt.figure(figsize = (13,13))    # Первая фигура задание 3 (диграммы рассеяния)
y = 1/(1 + math.e**-x)
plt.plot(x, y, '--o', markersize = 15, linewidth = 3, markerfacecolor = 'r', markeredgecolor = 'blue', markeredgewidth = 2)
plt.show()


fig6 = plt.figure(figsize = (13,13)) # Вторая фигура задание 3 (диаграммы рассеяния)
y = np.random.rand(100)
y2 = np.random.gamma(2, size = 100)
y3 = np.random.gamma(3, size = 100)
plt.scatter(x,y, c ='deeppink', marker = 'd', s = 50)
plt.scatter(x,y2, c ='g', marker = 's', s = 40)
plt.scatter(x,y3, c ='b')
plt.show()


fig7 = plt.figure(figsize = (13,13)) #Первая фигура задание 4 (графики в 3-х мерной системе координат)
ax = plt.axes(projection = '3d')
xl = np.linspace(-10,10,10)
yl = np.linspace(-10,10,10)
xlg, ylg = np.meshgrid(xl,yl)
zl = np.sin(xlg)*np.cos(ylg)
ax.plot_surface(xlg, ylg, zl, cmap = plt.cm.Spectral)
plt.show()


fig8 = plt.figure(figsize = (13,13)) #Вторая фигура задание 4 (графики в 3-х мерной системе координат)
ax = plt.axes(projection = '3d')
xl = np.linspace(0,50,100)
yl = np.cos(xl)
zl = np.cos(yl)
ax.plot3D(xl,yl,zl, 'blue')
plt.show()