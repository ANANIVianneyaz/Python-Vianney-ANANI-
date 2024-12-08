#Vianney ANANI
import matplotlib.pyplot as plt

fig,ax=plt.subplots()
rayon=int(input("Tapez le rayon :"))

cercle=plt.Circle((5,5),rayon,color="red",fill=True)

ax.add_artist(cercle)

ax.set_xlim(0, 10)
ax.set_ylim(0, 10)

ax.set_xticks(range(0,10,1))
ax.set_yticks(range(0,10,1))


plt.show()

