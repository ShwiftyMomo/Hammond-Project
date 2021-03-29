#Import neccecary utilities
from more_itertools import distinct_permutations
from scipy.special import binom
#Get the size we are testing
N=24

#This is the list of all possible sequences of -1s and 1s that can be permuted to get all bridges
possibleSlopes=[-1 for i in range(N//2)]+[1 for i in range(N//2)]
#This is the total amount of such bridges
total=binom(N,N//2)
#This is how we will keep track of how far we are in the computition
count=0
#Itterate through all possible bridges in an ordered way
for slope in distinct_permutations(possibleSlopes):
    #Generate the body from the slope
    body=[0]
    for s in slope[:-1]:
        body+=[body[-1]+s]
    #Make the bridge
    B=Bridge(size=N,body=body)
    #If 0 is down, it satisfies the first condition of the lemma
    if B.isDown(0):
        #Get all the downed verticies and upped verticies
        downs=[i for i in range(N) if B.isDown(i)]
        ups=[i for i in range(N) if (B.isUp(i) and (i!=1 and i!=N-1))]
        #Initialize the "base" probability of a flip
        prob1=0
        #Itterate through all pairs of upped and downed verticies
        for up in ups:
            for down in downs:
                #Check if the hypothesis of the lemma is satisfied
                if B.body[up]<=B.body[down]:
                    #If the base probability has not been computed, compute it
                    if prob1==0:
                        prob1=B.probFlip(0)

                    #Flip the two verticies
                    B.body[up]-=2
                    B.body[down]+=2

                    #Get the new probability
                    prob2=B.probFlip(0)

                    #Revert to how the bridge was before
                    B.body[up]+=2
                    B.body[down]-=2

                    #If the lemma does nnot hold print this result
                    if prob1<prob2:
                        print("--------------------")
                        print("FOUND ONE")
                        print(B)
                        print("Up: "+str(up))
                        print("Down: "+str(down))
                        print("Prob1: "+str(prob1))
                        print("Prob2: "+str(prob2))
                        print("--------------------")
    #Ittere how far we are in the computation
    count+=1
    #Regularly print how far we are in the computation
    if count%100==0:
        print(str(100*count/total)+"% complete")
    
print(str(100)+"% complete")
print("DONE!")
