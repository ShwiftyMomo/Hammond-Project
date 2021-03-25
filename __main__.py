#Import neccecary Bridge class and plotting class
from Bridge import Bridge
import matplotlib.pyplot as plt
import time


N=100
B=Bridge(size=N)
B.itter(reps=10000)
sampleSize=1000
maxes=0
for i in range(sampleSize):
    B.itter(reps=100)
    maxes+=B.maximum()

norm=maxes/sampleSize

print(norm)







