import matplotlib.pyplot as plt
#instala la libreria señalada

plt.close()

days = [1,2,3,4,5]
temps = [23.5, 23.5, 23.7, 23.5, 23.5,]
#ejes
sizes = [23.5, 23.5, 23.7, 23.5, 23.5,]
#tamaño asociado
plt.scatter(x=days, y=temps, s=sizes)

plt.show()
#muestra el grafico