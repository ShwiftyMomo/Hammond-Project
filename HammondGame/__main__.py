import Board
from strategies import min_I_Strategy
from strategies import HammondStrategy

#this is the main file where games are played

def main(player1,player2,boardSize = 15,numGames = 20):

    avgScore = 0
    for i in range(numGames):
        testBoard = Board(boardSize)
        avgScore += testBoard.game(player1,player2)/numGames

    return avgScore

player1 = Player(min_I_Strategy)
player2 = Player(HammondStrategy)

main(player1,player2)
