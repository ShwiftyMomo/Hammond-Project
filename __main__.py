#Import neccecary Bridge class and plotting class
from Bridge import Bridge
import matplotlib.pyplot as plt

#Choose the size we want for our bridges
N=176
#Get a set of 100 random bridges of size N
B=Bridge(size=N)

B.graph(verbose=1)

B.itter(reps=1000000)

B.graph(verbose=1)






