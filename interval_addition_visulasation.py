#Import neccecary Bridge class and plotting class
from Bridge import Bridge
import matplotlib.pyplot as plt

#Initialize a bridges of size 30 with illustrative bodies
B1=Bridge(size=30,body=[0, 1, 2, 3, 4, 3, 2, 1, 2, 3, 2, 1, 0, -1, -2, -1, -2, -3, -2, -1, -2, -3, -4, -5, -4, -5, -4, -3, -2, -1])

B2=Bridge(size=30,body=[0, 1, 2, 3, 4, 5, 4, 3, 4, 5, 4, 3, 2, 1, 0, -1, -2, -1, 0, -1, -2, -3, -4, -5, -4, -3, -2, -1, 0, 1])

#find the minimmum value
minimum=min([B1.body[i]-B2.body[i] for i in range(B1.size)])

#Find the disjoint subsets
subsets=[]
i=0
while i<B1.size:
    #Detect collision and record the subset formed
    if B1.body[i]-B2.body[i]==minimum:
        #begin the new subset that will be formed
        A=[i]
        #End the itteration if this is a singleton
        if i==B1.size-1:
            subsets+=[A]
            break
        #move on to next value of i
        i+=1
        while B1.body[i]-B2.body[i]==minimum:
            #Add the new overlap point to the subset
            A+=[i]
            #Stop looking if we have reached the end of the bridge
            if i==B1.size-1:
                subsets+=[A]
                break
            #Move on to next value of i
            i+=1
        
        #Stop looking if we have reached the end of the bridge
        if i==B1.size-1:
            break
        #Add the formed subset to subsets
        subsets+=[A]
    #move on to next value of i
    i+=1

#Plot B1
plt.plot(B1.body+[0],label="$B_0$")
#Plot B2, normalised to simply touch B1
plt.plot([B2.body[i]+minimum for i in range(B1.size)]+[minimum],label="$B_1$")

#Make the subsets red
for A in subsets:
    plt.plot(A,[B1.body[i] for i in A],c="red")

#Add a title/legend
plt.title("Pushing $B_1$ and $B_2$ together for addition")
plt.legend(loc="top left")
#show the final plot
plt.show()