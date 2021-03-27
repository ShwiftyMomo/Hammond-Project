#in this file I write the player class

def minI_Strategy(body):
    for i in range(len(body)):
        for j in range(len(body[i])):
            if body[i][j] == 0:
                return [i,j]
