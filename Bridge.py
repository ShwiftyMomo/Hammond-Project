#Import neccecary utilities
from random import shuffle
from scipy.special import binom
from copy import deepcopy

#The main simple random bridge class
class Bridge:
    #ins:
    #(int) size=order of cyclic group brige operates over
    #(list) body=the heights of each point on the curve, normalised so body[0]=0
    #outs:
    #Initializes all internal parameters 
    def __init__(self,size=None,body=None):
        
        #Intialised personal size attribute (length of body if not given)+type check
        if size!=None:

            #Make sure size given was an int
            if type(size)!=int:
                raise Exception("Size not an int in Bridge initialization")

            self.size=size

        
        else:
            #Make sure body and size aren't both empty
            if body==None:
                raise Exception("Size and body are empty in Bridge initialization")
            
            else:
                #Make sure body given is an int
                if type(body)!=list:
                    raise Exception("Body is not a list in Bridge initialization")

                self.size=len(body)
        
        #Make sure size is not odd
        if self.size%2==1:
            raise Exception("Size is not even in Bridge initialization")
        

        #Set up body if given, otherwise generate randomly
        if body!=None:
            if type(body)!=list:
                raise Exception("Body is not a list in Bridge initialization")

            self.body=body

    
        else:
            #Random generation done first by generating equal amounts of 1s/0s (slopes)
            slopes=[-1 for i in range(self.size//2)]+[1 for i in range(self.size//2)]
            #Permute slopes randomly to generate our bridge
            shuffle(slopes)
            #Generate self.body reccurcively
            self.body=[0]
            for value in slopes[:-1]:
                self.body+=[self.body[-1]+value]
    
    #ins: None
    #outs:
    #Prints all relevant data to Bridge in an easily readable format
    def __str__(self):
        #Intialalize the string that will be repeatedly acted upon then returned
        out=""
        #Adding verbal descriptions of Bridge
        out+="Size "+str(self.size)+" Simple Randome Bridge:"
        out+="\n \t -Body: "+str(self.body)
        out+="\n"

        #Generate terminal plot of data (details not important)
        top = max(self.body) + 1
        bot = min(self.body)

        arr = ["|" + " "*self.size for _ in range(bot, top + 1)]

        for i in range(self.size):
            isDown = self.body[i] > self.body[(i + 1) % self.size]
            char = "\\" if isDown else "/"
            line = self.body[i] - bot + (1 if not isDown else 0)
            arr[line] = arr[line][0:i+1] + char + arr[line][i+2:]

        arr.reverse()

        for i in range(self.size):
            if arr[top - 1][i+1] == " ":
                arr[top - 1] = arr[top - 1][0:i+1] + "_" + arr[top - 1][i+2:]
        #Add generated terminal graph to output
        out += "\n".join(arr)

        #return string after it has been properly formatted
        return out
    
    #ins:
    #(Bridge) other=another Bridge
    #outs:
    #A Boolean stating whether or not self and other are the same, up to rotation
    def __eq__(self,other):
        #Check if they are the same size, for taking modulo to be well defined
        if self.size!=other.size:
            return False
        #Go through each rotation and check if they are equivilant up to this rotation
        for rot in range(self.size):
            #Define value to be true if equivilance holds, false otherwise
            equiv=True
            #They are equivilant if self.body[i+rot]=other.body+constant, so we define the constant
            const=self.body[rot]-other.body[0]
            #Check to make sure that the difference is always this constant
            for i in range(self.size):
                if self.body[(i+rot)%self.size]-other.body[i]!=const:
                    equiv=False
            #Return true on equivilance, continue otherwise
            if equiv:
                return True
        #Return false if they are equivilant under no rotations
        return False

    #ins:
    #(int) i=An index in the body array (mod self.size, possibly)
    #outs:
    #(bool) True or False depending on whether or not self.body[i] is "down" or "up"
    def isDown(self,i):
        #get point and surrounding values mod self.size
        point=self.body[i%self.size]
        surrounding=min(self.body[(i-1)%self.size],self.body[(i+1)%self.size])
        #check if point<surrounding (i.e i is minimal)
        if point<surrounding:
            return True
        else:
            return False

    #ins:
    #(Bridge) other=Bridge that will be "added" to self in the canoncial way
    #outs:
    #The internal paramaters of self are adjusted to perform addition of self to other
    #This addition is done by finding all minimal intersection points of other to self and inverting self
    #(Bridge) Self, after having made the adjustments
    def add(self,other):
        #First, we make sure that lengths match up so addition makes sense
        if self.size!=other.size:
            raise Exception("Attempting to add Bridges of different sizes in add method")

        #We work by noting that intersection points happen when self.body[i]-other.body[i] is minimal
        #Here, we itterate through all i and see at what indicies self.body[i]-other.body[i] is minimzed and down
        #This list of minimal down verticies is stored here as "minValues"
        minValues=[]
        minimum=min([self.body[i]-other.body[i] for i in range(self.size)])
        for i in range(self.size):
            if self.body[i]-other.body[i]==minimum:
                if self.isDown(i):
                    minValues+=[i]
        #If 0 is in minValues, instead of pushing it up we push everything else down to keep normalization
        if 0 in minValues:
            for i in range(self.size):
                if i not in minValues:
                    self.body[i]-2
        #Otherwise, we can just push up the targetted points
        else:
            for i in minValues:
                self.body[i]+=2
        #return properly updated self
        return self

    #ins:
    #(int) reps=The amount of times randome bridges will be added to self before the graph is made
    #(bool) change=Whether or not the internal paramaters should change after this addition
    #outs:
    #(Bridge) the result of the addition of the bridge
    #If change is true, the internal state of the bridge is also changed by the addition
    #The graph of the result of the addition is shown, with red regions where the change occured
    def addGraph(self,reps=1,change=True):
        #Duplicate the current bridge so that it will not be altered under the itterative addition
        B=deepcopy(self)
        #Perform the desired repeated addition
        B.itter(reps=reps)
        #Import matplotlib.pyplot for plotting, as well as a neccecary helper function for pretty colors
        import matplotlib.pyplot as plt
        from helper_functions import adjust_lightness
        #Choose a snazzy title for the plot
        plt.title("Graph of SRB, along with change after "+str(reps)+" rounds of addition")
        #Plot the SRB pre and post addition
        plt.plot(B.body+[0],label="Post-addition",c=adjust_lightness("pink",0.8))
        plt.plot(self.body+[0],label="Pre-addition")
        plt.fill_between(range(self.size+1),self.body+[0],B.body+[0],facecolor="pink")
        #Set up the legend and show the graph
        plt.legend(loc="upper left")
        plt.show()
        #update self if change is true
        if change:
            self=B

    #ins:
    #(int) verbose= Which level of "style" or "complexity" information has (verbose =0,1,2) more verbose=more complex
    #(str) title= An optinal title parameter for verbose=1 plotting
    #outs:
    #Verbose=0 (default)=>Terminal plot of data printed
    #Verbose=1 => Plot data full screen in Matplotlib
    #Verbose=2 => Plot data full screen in Matplotlib with weight coloring
    def graph(self,verbose=0,title=None):
        #Verbose=0 => Terminal plot of data
        if verbose==0:
            #Generate terminal plot of data as in __str__ method (details not important)
            top = max(self.body) + 1
            bot = min(self.body)

            arr = ["|" + " "*self.size for _ in range(bot, top + 1)]

            for i in range(self.size):
                isDown = self.body[i] > self.body[(i + 1) % self.size]
                char = "\\" if isDown else "/"
                line = self.body[i] - bot + (1 if not isDown else 0)
                arr[line] = arr[line][0:i+1] + char + arr[line][i+2:]

            arr.reverse()

            for i in range(self.size):
                if arr[top - 1][i+1] == " ":
                    arr[top - 1] = arr[top - 1][0:i+1] + "_" + arr[top - 1][i+2:]
            #Add generated terminal graph to output
            print("\n".join(arr))
        
        #Verbose=1 => Plot data in Matplotlib
        if verbose==1:
            #Import matplotlib for plotting if neccecary
            import matplotlib.pyplot as plt
            #Plot the actual data in question
            plt.plot(self.body+[0])
            #Place title if given, give default otherwise
            if title!=None:
                plt.title(title)
            else:
                plt.title("Size "+str(self.size)+" Simple Random Bridge")
            #Render the plot
            plt.show()

        #Verbose=2 => Plot data in Matplotlib with weight coloring
        if verbose==2:
            #Import matplotlib for plotting if neccecary
            #It is not imported earlier for optics reasons when not using this method
            import matplotlib.pyplot as plt

            #Plot the actual data in question
            plt.plot(self.body+[0])
            #Place title if given, give default otherwise
            if title!=None:
                plt.title(title)
            else:
                plt.title("Size "+str(self.size)+" Simple Random Bridge with weight coloring")
            #Add properly colored points at down verticies
            for i in range(self.size):
                if self.isDown(i):
                    pr=self.probFlip(i)
                    plt.scatter(i,self.body[i],c=(pr,0.1,1-pr))
            #Render the plot
            plt.show()
    
    #ins:
    #(int) reps= How many times random Bridges should be added to self
    #outs:
    #(Bridge) Self, after having been interanally updated
    #Internal data changed to simulate having added random Bridges to self reps times
    def itter(self,reps=1):
        #Generate a list of 1s and -1s that will be shuffled to produce each bridge we will be adding to self
        newSlopes=[-1 for i in range(self.size//2)]+[1 for i in range(self.size//2)]

        #Add new bridges to self reps times
        for rep in range(reps):
            #Shuffle the slopes to make a new bridge profile
            shuffle(newSlopes)
            #Set up the new bridge using the reccursive definition as in __init__
            newBridge=[0]
            for value in newSlopes[:-1]:
                newBridge+=[newBridge[-1]+value]

            #Go through the addition algorithm exactly as in .add, using this new bridge
            minValues=[]
            minimum=min([self.body[i]-newBridge[i] for i in range(self.size)])
            for i in range(self.size):
                if self.body[i]-newBridge[i]==minimum:
                    if self.isDown(i):
                        minValues+=[i]
            if 0 in minValues:
                for i in range(self.size):
                    if i not in minValues:
                        self.body[i]=self.body[i]-2
            else:
                for i in minValues:
                    self.body[i]+=2
        #Return the now update self
        return self

    #ins: none
    #outs:
    #(int) The maximum absolute value in self.body
    def maximum(self):
        #Get the absolute value of each element then take the maximum
        return max([abs(self.body[i]) for i in range(self.size)])

    #ins:
    #(int) i=An index in the body array (mod self.size, possibly)
    #outs:
    #(Bridge) The same SRB rotated such that index i goes into the 0 spot
    def rot(self,i):
        #Get the new body of the Bridge by rotating elementwise, and normalizing so that self.body[0]=0
        newBody=[self.body[(index+i)%self.size]-self.body[i] for index in range(self.size)]
        #Return a new bridge with this given body
        return Bridge(size=self.size,body=newBody)

    #ins:
    #(int) i=An index in the body array (mod self.size, possibly)
    #outs:
    #(float) A real number 0<output<1 that is the probability that index i will flip in an addition
    def probFlip(self,i):
        #If i is not down, then it cannot be flipped
        if not self.isDown(i):
            return 0
        #The algorith used will be by counting the amount of bridges that flip i, then dividing by the total number of bridges
        #Get a rotated version of the bridge so that the target index gets put first
        newBridge=self.rot(i)
        #Since the placement of the +s determines the placement of the -s, there are (n choose n/2) total bridges
        return newBridge.probFlipHelper(index=0,height=0)/binom(self.size,self.size//2)

    #ins:
    #(int) index=the index that search is starting at
    #(int) height=the current height at index of the SRB
    #outs:
    #The amount of SRBs there are that stay under self starting at index "index" and height "height"
    def probFlipHelper(self,index,height):
        #Check if there is enough time to return home to 0, eliminate branch if not
        if self.size-index<abs(height):
            return 0
        #Return the bridge if it has been completed
        if index==self.size:
            return 1
        #Check to make sure the trial bridge not passing the state bridge, eliminate branch if not
        if height>self.body[index]:
            return 0
        #Split into two cases for next value of bridge, and add together the possibilities
        return self.probFlipHelper(index+1,height+1)+self.probFlipHelper(index+1,height-1)

    #ins:
    #(Bridge) other=Bridge that will be added by ther interval method to self
    #outs:
    #(Bridge) self, with its interval paramaters changed
    #As suggested above, the internal paramaters will change to reflect the addition
    def intervalAdd(self,other):
        #First, we make sure that lengths match up so addition makes sense
        if self.size!=other.size:
            raise Exception("Attempting to add Bridges of different sizes in add method")
        #Get the minimum value that all values are being tested against
        minimum=min([self.body[i]-other.body[i] for i in range(self.size)])
        #Intitialise the collection of disjoint subsets
        subsets=[]
        #Initialise the indexing variable that will be updated in a non-linear fashion
        i=0
        while i<self.size:
            #Detect collision and record the subset formed
            if self.body[i]-other.body[i]==minimum:
                #begin the new subset that will be formed
                A=[i]
                #End the itteration if this is a singleton
                if i==self.size-1:
                    subsets+=[A]
                    break
                #move on to next value of i
                i+=1
                while self.body[i]-other.body[i]==minimum:
                    #Add the new overlap point to the subset
                    A+=[i]
                    #Stop looking if we have reached the end of the bridge
                    if i==self.size-1:
                        subsets+=[A]
                        break
                    #Move on to next value of i
                    i+=1
                
                #Stop looking if we have reached the end of the bridge
                if i==self.size-1:
                    break
                #Add the formed subset to subsets
                subsets+=[A]
            #move on to next value of i
            i+=1
        #Work on each subset with the helper method
        for A in subsets:
            self.intervalAddHelper(A)
        
        #Return the updated bridge
        return self

    #ins:
    #(int) reps=The amount of times randome bridges will be added to self before the graph is made
    #(bool) change=Whether or not the internal paramaters should change after this addition
    #outs:
    #(Bridge) the result of the addition (using interval algorithm) of the bridge
    #If change is true, the internal state of the bridge is also changed by the addition
    #The graph of the result of the addition is shown, with red regions where the change occured      
    def intervalAddGraph(self, reps=1, change=True):
        #Duplicate the current bridge so that it will not be altered under the itterative addition
        B=deepcopy(self)
        #Perform the desired repeated addition
        B.intervalItter(reps=reps)
        #Import matplotlib.pyplot for plotting, as well as a neccecary helper function for pretty colors
        import matplotlib.pyplot as plt
        from helper_functions import adjust_lightness
        #Choose a snazzy title for the plot
        plt.title("Graph of SRB, along with change after "+str(reps)+" rounds of interval addition")
        #Plot the SRB pre and post addition
        plt.plot(B.body+[0],label="Post-addition",c=adjust_lightness("pink",0.8))
        plt.plot(self.body+[0],label="Pre-addition")
        plt.fill_between(range(self.size+1),self.body+[0],B.body+[0],facecolor="pink")
        #Set up the legend and show the graph
        plt.legend(loc="upper left")
        plt.show()
        #update self if change is true
        if change:
            self=B
    
    #ins:
    #(int) reps= How many times random Bridges should be added to self
    #outs:
    #(Bridge) Self, after having been interanally updated
    #Internal data changed to simulate having added using interval algorithm to random Bridges to self reps times
    def intervalItter(self,reps=1):
        #Add random SRBs to bridge reps times
        for i in range(reps):
            self.intervalAdd(other=Bridge(size=self.size))
        #Return self at the end
        return self

    #ins:
    #(list) A=A subset of consecutive indicies of self
    #outs:
    #(Bridge) self, with its interval paramaters changed
    #The interval A in self.body will be replaced with a random bridge with the same endpoints
    def intervalAddHelper(self,A):
        #find out how many more +1s/-1s will be needed in the random bridge
        delta=self.body[A[0]]-self.body[A[-1]]
        #create the sample of +1s/-1s appropriately
        slopes=[1 for i in range((len(A)-delta-1)//2)]+[-1 for i in range((len(A)+delta-1)//2)]
        #shuffle to create a random assortment of 1s and -1s
        shuffle(slopes)
        #Update the chosen region of body
        for i in range(len(A)-1):
            self.body[A[i+1]]=self.body[A[i]]+slopes[i]

