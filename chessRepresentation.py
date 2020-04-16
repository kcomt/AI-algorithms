
class piece:
    def __init__(self,posx,posy,value,name,color):
        self.posx = posx
        self.posy = posy
        self.value = value
        self.name = name
        self.color = color

    def validMove(self,posyFrom,posxFrom,posyTo,posxTo,typeOf):
        #validate move of pawn
        if self.name == "pawn":
            if self.color == "black":
                if typeOf == "move":
                    if posyTo == posyFrom + 1 and posxTo == posxFrom:
                        return True
                    if posyFrom == 1 and posyTo == posyFrom  + 2 and posxTo == posxFrom:
                        return True
                else:
                    if (posyTo == posyFrom + 1 and posxTo + 1 == posxFrom) or (posyTo == posyFrom + 1 and posxTo - 1 == posxFrom):
                        return True
            else:
                if typeOf == "move":
                    if posyTo + 1 == posyFrom and posxTo == posxFrom:
                        return True
                    if posyFrom == 6 and posyTo + 2 == posyFrom and posxTo == posxFrom:
                        return True
                else:
                    if (posyTo + 1 == posyFrom and posxTo + 1 == posxFrom) or (posyTo + 1 == posyFrom and posxTo - 1 == posxFrom):
                        return True
            return False

        #validating if position where bishop or queen wants to go is legal
        if self.name == "bishop" or self.name == "queen":
            #validate if bishop will go NORTHWEST Diagnollay
            if posxFrom > posxTo and posyFrom > posyTo:
                if posxFrom - posxTo == posyFrom-posyTo:
                    return True
                else:
                    return False
            #validate if bishop will go SOUTHEAST Diagnollay
            if posxFrom < posxTo and posyFrom < posyTo:
                if posxTo - posxFrom == posyTo-posyFrom:
                    return True
                else:
                    return False
            #validate if bishop will go NORTHEAST Diagnollay
            if posxFrom < posxTo and posyFrom > posyTo:
                if posxTo - posxFrom == posyFrom-posyTo:
                    return True
                else:
                    return False
            #validate if bishop will go SOUTHWEST Diagnollay
            if posxFrom > posxTo and posyFrom < posyTo:
                if posxFrom - posxTo == posyTo-posyFrom:
                    return True
                else:
                    return False
            
    #validate tower and queen towerish movement    
        if self.name == "tower" or self.name == "queen":
            if posxFrom == posxTo and posyFrom != posyTo:
                return True
            if posxFrom != posxTo and posyFrom == posyTo:
                return True
            return False

    #validate horse movement    
        if self.name == "horse":
            if posxFrom + 1 == posxTo and posyFrom + 3 == posyTo:
                return True
            if posxFrom + 3== posxTo and posyFrom + 1== posyTo:
                return True
            if posxFrom + 3 == posxTo and posyFrom == posyTo + 1:
                return True
            if posxFrom + 1 == posxTo and posyFrom == posyTo + 3:
                return True
            if posxFrom == posxTo + 1 and posyFrom == posyTo + 3:
                return True
            if posxFrom == posxTo + 3 and posyFrom == posyTo + 1:
                return True
            if posxFrom == posxTo + 3 and posyFrom + 1 == posyTo:
                return True
            if posxFrom == posxTo + 1 and posyFrom + 3 == posyTo:
                return True
            return False

    #validate king movement    
        if self.name == "king":
            #validate down
            if posxFrom == posxTo and posyFrom + 1 == posyTo:
                return True 
            #validate up
            if posxFrom == posxTo and posyFrom == posyTo + 1:
                return True 
            #validate left
            if posxFrom == posxTo + 1 and posyFrom == posyTo:
                return True 
            #validate right
            if posxFrom + 1 == posxTo and posyFrom == posyTo:
                return True 
            #validate upright
            if posxFrom + 1 == posxTo and posyFrom + 1 == posyTo:
                return True 
            #validate downright
            if posxFrom + 1 == posxTo and posyFrom == posyTo + 1:
                return True 
            #validate upleft
            if posxFrom == posxTo + 1 and posyFrom + 1 == posyTo:
                return True 
            #validate downright
            if posxFrom== posxTo +1  and posyFrom == posyTo + 1:
                return True 
            return False
    
        return False

class player:
    def __init__(self,color):
        self.points = 0
        self.pieces = []
        self.color = color

    def initializeBasedOnColor(self):
        if self.color == "white":
            #add pawns
            for i in range(0,8):
                aux = piece(i,6,10,"pawn","white")
                self.pieces.append(aux)

            #add towers
            for i in range(0,8,7):
                aux = piece(i,7,50,"tower","white")
                self.pieces.append(aux)

            #add horses
            for i in range(1,8,5):
                aux = piece(i,7,30,"horse","white")
                self.pieces.append(aux)

            #add bishops
            for i in range(2,8,3):
                aux = piece(i,7,31,"bishop","white")
                self.pieces.append(aux)

            #add queen
            aux = piece(3,7,90,"queen","white")
            self.pieces.append(aux)
            
            #add king
            aux = piece(4,7,1000,"king","white")
            self.pieces.append(aux)

        if self.color == "black":
            #add pawns
            for i in range(0,8):
                aux = piece(i,1,10,"pawn","black")
                self.pieces.append(aux)

            #add towers
            for i in range(0,8,7):
                aux = piece(i,0,50,"tower","black")
                self.pieces.append(aux)

            #add horses
            for i in range(1,8,5):
                aux = piece(i,0,30,"horse","black")
                self.pieces.append(aux)

            #add bishops
            for i in range(2,8,3):
                aux = piece(i,0,31,"bishop","black")
                self.pieces.append(aux)

            #add queen
            aux = piece(3,0,90,"queen","black")
            self.pieces.append(aux)
                
            #add king
            aux = piece(4,0,1000,"king","black")
            self.pieces.append(aux)

class board:
    board = [["00","00","00","00","00","00","00","00"], #0
             ["00","00","00","00","00","00","00","00"], #1
             ["00","00","00","00","00","00","00","00"], #2
             ["00","00","00","00","00","00","00","00"], #3
             ["00","00","00","00","00","00","00","00"], #4
             ["00","00","00","00","00","00","00","00"], #5
             ["00","00","00","00","00","00","00","00"], #6
             ["00","00","00","00","00","00","00","00"]] #7
            #0,     1,   2,   3,    4,  5,    6,  7

    boardOfObjects = [["00","00","00","00","00","00","00","00"], #0
             ["00","00","00","00","00","00","00","00"], #1
             ["00","00","00","00","00","00","00","00"], #2
             ["00","00","00","00","00","00","00","00"], #3
             ["00","00","00","00","00","00","00","00"], #4
             ["00","00","00","00","00","00","00","00"], #5
             ["00","00","00","00","00","00","00","00"], #6
             ["00","00","00","00","00","00","00","00"]] #7


    def __init__(self,playerWhite,playerBlack):
        #initializes 2 board, one for printing and the other for keeping track of the pieces
        for i in playerWhite.pieces:
            self.board[i.posy][i.posx] = i.name[0] + i.color[0]
            self.boardOfObjects[i.posy][i.posx] = i

        for i in playerBlack.pieces:
            self.board[i.posy][i.posx] = i.name[0] + i.color[0]
            self.boardOfObjects[i.posy][i.posx] = i

    def printBoard(self):
        for i in self.board:
            print(i)

    #Transform chess lingo (e5 to h1) to array positions
    def transformToPos(self,string):
        #find pos x
        if string[0] == "a":
            posx = 0
        if string[0] == "b":
            posx = 1
        if string[0] == "c":
            posx = 2
        if string[0] == "d":
            posx = 3
        if string[0] == "e":
            posx = 4
        if string[0] == "f":
            posx = 5
        if string[0] == "g":
            posx = 6
        if string[0] == "h":
            posx = 7

        #find pos y
        if string[1] == "8":
            posy = 0
        if string[1] == "7":
            posy = 1
        if string[1] == "6":
            posy = 2
        if string[1] == "5":
            posy = 3
        if string[1] == "4":
            posy = 4
        if string[1] == "3":
            posy = 5
        if string[1] == "2":
            posy = 6
        if string[1] == "1":
            posy = 7

        return posx,posy

    def checkToSeeIfPieceInWay(type,posyFrom,posxFrom,posyTo,posxTo):

    def validateMove(self,turn,stringFrom,stringTo):
        posxFrom, posyFrom = self.transformToPos(stringFrom)
        posxTo, posyTo= self.transformToPos(stringTo)

        #validates if position from From is a piece that is the same color of the turn and the piece
        if self.boardOfObjects[posyFrom][posxFrom] != "00" and self.boardOfObjects[posyFrom][posxFrom].color == turn:
            #validates if positions of TO is empty or has a piece of different color
            if self.boardOfObjects[posyTo][posxTo] == "00" or self.boardOfObjects[posyTo][posxTo].color != turn:
                print("funciona")




human = player("white")
computer = player("black")

human.initializeBasedOnColor()
computer.initializeBasedOnColor()

chessboard = board(human,computer)
chessboard.printBoard()

chessboard.validateMove("white","c1","c2")