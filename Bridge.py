#Import neccecary utilities
from random import shuffle

#The main stochastic bridge class
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
        out+="Size "+str(self.size)+" stochastic Bridge:"
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
    #(int) verbose= Which level of "style" or "complexity" information has (verbose =0,1) more verbose=more complex
    #(str) title= An optinal title parameter for verbose=1 plotting
    #outs:
    #Verbose=0 (default)=>Terminal plot of data printed
    #Verbose=1 => Plot data full screen in Matplotlib
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
        
        #Verbose=1 =>
        if verbose==1:
            #Import matplotlib for plotting if neccecary
            #It is not imported earlier for optics reasons when not using this method
            import matplotlib.pyplot as plt

            #Plot the actual data in question
            plt.plot(self.body)
            #Place title if given, give default otherwise
            if title!=None:
                plt.title(title)
            else:
                plt.title("Size "+str(self.size)+" Stochastic Bridge")
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