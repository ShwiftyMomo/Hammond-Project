#Import neccecary Bridge class and plotting class
from Bridge import Bridge
import matplotlib.pyplot as plt

#Make a random bridge of size 12
B=Bridge(size=12)

#print the bridge
print(B)

#update the bridge 20 times
B.itter(reps=20)

#print the updated bridge
print(B)
