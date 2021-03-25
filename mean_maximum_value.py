#Import neccecary Bridge class and plotting class
from Bridge import Bridge
import matplotlib.pyplot as plt
from numpy import log

#Itterate through all the values of 2n wanting to be tested, and then compute their mean
for n in range(1,176):
    #Set the size of the SRB to be N=2n
    N=2*n
    #Generate the random bridge
    B=Bridge(size=N)
    #Perform repeated addition 10,000 times, to get to a "limiting bridge"
    B.itter(reps=10000)
    #Choose how many Bridges will be in the sample taken
    sampleSize=1000
    #Initialize the sum of maximums in the sample
    maxes=0
    for i in range(sampleSize):
        #Repeatedly add 100 times to get a new bridge
        B.itter(reps=100)
        #Add the maximum absolute value of this bridge to our running tally
        maxes+=B.maximum()
    #Make this an average by dividing by our sample size
    norm=maxes/sampleSize
    #Print out the mean obtained
    print(str(N)+": "+str(norm))


#Data I obtained after running this file
#data=[1.0,1.126,1.277,1.4,1.514,1.606,1.658,1.78,1.832,1.885,1.954,2.022,2.008,2.064,2.099,2.173,2.178,2.197,2.237,2.261,2.29,2.349,2.323,2.326,2.339,2.397,2.408,2.444,2.429,2.415,2.48,2.472,2.449,2.503,2.516,2.524,2.543,2.536,2.621,2.622,2.585,2.612,2.612,2.622,2.658,2.67,2.695,2.634,2.676,2.674,2.728,2.732,2.69,2.7,2.681,2.695,2.726,2.759,2.706,2.751,2.777,2.75,2.797,2.757,2.801,2.828,2.8,2.788,2.832,2.824,2.807,2.817,2.853,2.844,2.847,2.841,2.829,2.869,2.867,2.875,2.887,2.921,2.894,2.939,2.894,2.894,2.922,2.94,2.883,2.935,2.923,2.971,2.963,2.958,2.949,2.972,2.959,2.967,2.961,3.021,2.985,2.986,2.986,2.972,2.962,3.016,3.008,3.023,2.989,3.037,3.054,3.035,3.018,3.093,3.05,3.051,3.046,3.045,3.081,3.073,3.035,3.072,3.054,3.052,3.131,3.073,3.087,3.087,3.12,3.086,3.095,3.08,3.144,3.129,3.153,3.087,3.101,3.078,3.126,3.15,3.074,3.108,3.127,3.093,3.137,3.126,3.173,3.139,3.195,3.153,3.214,3.171,3.177,3.161,3.145,3.179,3.229,3.201,3.178,3.222,3.172,3.226,3.148,3.189,3.184,3.219,3.237,3.211,3.202,3.225,3.201,3.224,3.205,3.2,3.189]
#The code used to graph this data
"""xaxis=[2*(n+1) for n in range(len(data))]

logarithm=[0.460618*log(n)+.54 for n in xaxis]

plt.title("Mean Maximum Value in SRB versus Size")
plt.xlabel("Size of SRB")
plt.ylabel("Mean Maximum Value")
plt.plot(xaxis,data,label="Mean Maximum Value")
plt.plot(xaxis,logarithm,label="0.460618$\\ln(x)$+.54")
plt.plot([], [], ' ', label="$r^2=.995$")
plt.legend(loc="upper left")
plt.show()
"""