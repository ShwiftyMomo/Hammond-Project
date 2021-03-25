#Import neccecary Bridge class and plotting class
from Bridge import Bridge
import matplotlib.pyplot as plt

#Choose the size we want for our bridges
N=176
#Get a set of 100 random bridges of size N
bridges=[Bridge(size=N) for i in range(100)]
#Give plot a snazzy title
plt.suptitle("Stochastic Bridges before repeated addition")

#Itterate through bridges and plot them
for num in range(100):
    #"cd" into the correct subplot
    plt.subplot(10,10,num+1)
    #Remove the (honestly distracting) numbers next to graphs
    plt.xticks([])
    plt.yticks([])
    #Plot the "bodies" (i.e actual numbers) of the bridges
    plt.plot(bridges[num].body)

#Finish this first graph by rendering it
plt.show()

#Go through each bridge and do the repeated addition algorithm 10,000 times
[bridge.itter(reps=10000) for bridge in bridges]

#Do the same process as before, just with this new data

plt.suptitle("Stochastic Bridges after repeated addition")
for num in range(100):
    plt.subplot(10,10,num+1)
    plt.xticks([])
    plt.yticks([])
    plt.plot(bridges[num].body)
plt.show()