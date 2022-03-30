
import matplotlib.pyplot as plt
import numpy as np

# birinci seçenek

x=[1,2,3,4]
y=[1,4,9,16]
plt.plot(x,y,color="red",linewidth="5")

plt.axis([0,6,0,20])

plt.title("Grafik Başlığı")
plt.xlabel("x label")
plt.ylabel("y label")

# ikinci seçenek

plt.plot(x,x,label="linear",color="red")
plt.plot(x,x**2,label="quadratic",color="yellow")
plt.plot(x,x**3,label="cubic",color="green")

plt.title("Basit Plot Kullanımı")
plt.xlabel("x çizgisi")
plt.ylabel("y çizgisi")

plt.legend()
plt.show()

# üçüncü seçenek
x=np.linspace(0,2,100)
fig,axs=plt.subplots(2)
axs[0].plot(x,x,color="red")
axs[0].set_title("linear tip")

axs[1].plot(x,x**2,color="green")
axs[1].set_title("quadratic tip")

axs[2].plot(x,x**3,color="yellow")
axs[2].set_title("cubic tip")
# Burada tek bir figur üstüne 3 tane grafik çizmiş olduk

plt.tight_layout()

plt.show()