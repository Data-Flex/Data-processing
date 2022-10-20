import numpy as np
import matplotlib.pyplot as plt
with open("settings.txt", "r") as settings:
    tmp = [float(i) for i in settings.read().split('\n')]
    
data = np.loadtxt("data.txt", dtype = int)
data = data*tmp[0]
#chargetime = np.where(data == data.max())
chargetime = np.argmax(data)*tmp[1]
dechargetime = data.size*tmp[1] - chargetime
print(chargetime)
time = [i*tmp[1] for i in range(data.size)]

fig, ax = plt.subplots(figsize = (16, 10),dpi = 400)
ax.plot(time, data, label = "V(t)", color = 'green', marker = "s", markevery = 30)
ax.set_title("Процесс заряда и разряда конденсатора в RC-цепочке")
ax.set_xlabel("Время, с")
ax.set_xlim([0, 10])
ax.set_ylabel("Напряжение, В")
ax.set_ylim([0, 3.5])
ax.minorticks_on()
ax.grid(which = 'both')
ax.text(8, 2.5, "Время зарядки = " + str(chargetime) + " с")
ax.text(8, 2, "Время разрядки = " + str(dechargetime) + " с")
ax.legend(fontsize = 20)
fig.savefig("data.svg")