#Import neccecary Bridge class and plotting class
from Bridge import Bridge
import matplotlib.pyplot as plt
import time


for n in range(1,1000):
    N=2*n
    B=Bridge(size=N)
    B.itter(reps=10000)
    sampleSize=1000
    maxes=0
    for i in range(sampleSize):
        B.itter(reps=100)
        maxes+=B.maximum()

    norm=maxes/sampleSize

    print(str(N)+": "+str(norm))







