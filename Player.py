class Player:
    def __init__(self,strategy): #strategy is a function that imports the board and outputs a move
        self.strategy = strategy

    def move(self,body):
        return self.strategy(body)
