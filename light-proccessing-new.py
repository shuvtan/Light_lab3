import lightFunctions as j
import matplotlib.pyplot as plt
import numpy as np
from cycler import cycler

# Калибровка - получаем график интенсивности белого цвета под светом ртутной лампы и массив интенсивностей каждого пикселя

intensity = []
intensity.append(j.readIntensity("white-mercury.jpg", "white-mercury2.jpg", "Ртутная лампа", "белый лист"))
print(intensity[0])

#автоматизация
colorRu = ["белый", "красный", "жёлтый", "зелёный", "синий"]
colorEn = ["white", "red", "yellow", "green", "blue"]
#Получаем график интенсивности каждого цвета
for i in range(5):
    intensity.append(j.readIntensity(colorEn[i] + "-tungsten.jpg", colorEn[i] + "-tungsten2.jpg", "Лампа накаливания", colorRu[i] + " лист"))
    print(intensity[i + 1])
#удаляем массив интенсивности под светом ртутной лампы(сдвигаем)
intensity.pop(0)
#придаем цвет линиям
plt.rc('axes', prop_cycle = (cycler('color', ['w', 'r', 'y', 'g', 'b'])))
fig = plt.figure()

plt.title('Отражённая интенсивность\n излучения лампы накаливания')
plt.xlabel('Длина волны излучения, нм')
plt.ylabel('Яркость')
#серый фон, цена деления, сетка
plt.gca().set(facecolor = 'gray')    
plt.minorticks_on()
plt.grid(which = 'major')
plt.grid(which = 'minor', linestyle = '--')
#массив длин волн
waveLength = np.arange(380, 682.5, 0.55)
#график инртенсивности
labels = ['Белый лист', 'Красный лист', 'Жёлтый лист', 'Зелёный лист', 'Синий лист']
for i in range(5):
    plt.plot(waveLength, intensity[i], label = labels[i])

plt.legend()
    
plt.savefig('intensities.png')

#устанавливаем цвета для линий
plt.rc('axes', prop_cycle = (cycler('color', ['w', 'r', 'y', 'g', 'b'])))
fig = plt.figure()

plt.title('Альбедо поверхностей')
plt.xlabel('Длина волны излучения, нм')
plt.ylabel('Альбедо')
#сетка, серый фон
plt.gca().set(facecolor = 'gray')    
plt.minorticks_on()
plt.grid(which = 'major')
plt.grid(which = 'minor', linestyle = '--')


waveLength = np.arange(380, 682.5, 0.55)
#график альбедо
albedo = []
albedo.append(np.linspace(1, 1, 550)) #значения альбедо для белого листа
#значения альбедо для остальных цветов
for k in range(1, 5):
    albedo1 = []
    for i in range(550):
        if intensity[0][i] < 0.25:
            albedo1.append(intensity[k][i] / (intensity[0][i] + 0.5))
        elif intensity[0][i] <= intensity[k][i]:
            albedo1.append(1)
        else:
            albedo1.append(intensity[k][i] / intensity[0][i])
    albedo.append(albedo1)
#Строим пять графиков альбедо на одном листе
for i in range(5):
    plt.plot(waveLength, albedo[i], label = labels[i])

plt.legend()
    
plt.savefig('albedos.png')