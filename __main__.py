#Import neccecary Bridge class and plotting class
from Bridge import Bridge
import matplotlib.pyplot as plt

#Initialize a bridge of size 22
B=Bridge(size=22)

#Print the bridge to the terminal
print(B)

#Perform repeated addition 100 times
B.itter(reps=100)

#Print the updated bridge
print(B)