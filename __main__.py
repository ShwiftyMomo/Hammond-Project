#Import neccecary Bridge class and plotting class
from Bridge import Bridge
import matplotlib.pyplot as plt

#Make a random bridge of size 12
B=Bridge(size=12)

#Print the bridge
print(B)

#Update the bridge with 20 rounds of repeated addition
B.itter(reps=20)

#Print the updated bridge
print(B)