#Import neccecary Bridge class and plotting class
from Bridge import Bridge
import matplotlib.pyplot as plt
import time


t0=time.time()
B=Bridge(size=500)
B.itter(reps=10000)
t1=time.time()






