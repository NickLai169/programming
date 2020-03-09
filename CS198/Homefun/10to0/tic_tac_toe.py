from generic_game import Game
import copy

class Tic_Tac_Toe(Game):
    primitive_position = None
    possible_moves = []
    players = ["X", "O"]
    piece_based = True

    def hashencode(self, position, turn = None):
        """creates a hash for the game state in the format:
        \"[turn (? if undefined)][y dimension][x dimension][the board pieces in numbers]"""
        code = ""
        if turn != None:
            code += turn
        else:
            code += "?"
        code += str(len(position))
        code += str(len(position[0]))

        for y in range(len(position)):
            for x in range(len(position[y])):
                code += str(position[y][x])

        return code

    def hashdecode(self, hashcode):
        position = []
        index = 3
        print(hashcode)
        for y in range(int(hashcode[1])):
            position.append([])
            for x in range(int(hashcode[2])):
                position[y].append(int(hashcode[index]))
                index += 1

        return position

    def convert_piece(self, piece):
        if piece == "X":
            return 1
        elif piece == "O":
            return 2
        elif piece == 1:
            return "X"
        elif piece == 2:
            return "O"
        else:
            return "?"

    def primitive_positions(self, board):
        "Checks to see if there is connected row"
        for i in range(len(board)):
            if board[i][0] != 0:
                temp = True
                first_val = board[i][0]
                for i2 in range(len(board[i])):
                    if board[i][i2] != first_val:
                        temp = False
                        break;
                if temp:
                    return True
                else:
                    temp = True

        "Checks to see if there is a connected column"
        for i in range(len(board[0])):
            if board[0][i] != 0:
                temp = True
                first_val = board[0][i]
                for i2 in range(len(board[i])):
                    if board[i2][i] != first_val:
                        temp = False
                        break;
                if temp:
                    return True
                else:
                    temp = True

        "Checks for a connected top-left to bottom-right"
        if board[0][0] != 0:
            temp = True
            first_val = board[0][0]

            for i in range(len(board)):
                if board[i][i] != first_val:
                    temp = False
                    break;

            if temp:
                return True

        "Checks for a connected diagonal top-right to bottom-left"
        if board[-1][0] != 0:
            temp = True
            first_val = board[-1][0]
            for i in range(len(board)):
                if board[-(i + 1)][i] != first_val:
                    temp = False
                    break;

            if temp:
                return True

        return False

    def print_board(self, board):
        for i in board:
            print("|", end =" ")
            for i2 in i:
                if i2 == 0:
                    print("  ", end ="")
                elif i2 == 1:
                    print("X ", end ="")
                elif i2 == 2:
                    print("O ", end ="")
                else:
                    print("? ", end ="")
            print("|")

    def winner(self, board):
        "Checks to see if there is connected row"
        for i in range(len(board)):
            if board[i][0] != 0:
                temp = True
                first_val = board[i][0]
                for i2 in range(len(board[i])):
                    if board[i][i2] != first_val:
                        temp = False
                        break;
                if temp:
                    return first_val
                else:
                    temp = True

        "Checks to see if there isa  connected column"
        for i in range(len(board[0])):
            if board[0][i] != 0:
                temp = True
                first_val = board[0][i]
                for i2 in range(len(board[i])):
                    if board[i2][i] != first_val:
                        temp = False
                        break;
                if temp:
                    return first_val
                else:
                    temp = True

        "Checks for a connected top-left to bottom-right"
        if board[0][0] != 0:
            temp = True
            first_val = board[0][0]

            for i in range(len(board)):
                if board[i][i] != first_val:
                    temp = False
                    break;

            if temp:
                return first_val

        "Checks for a connected diagonal top-right to bottom-left"
        if board[len(board) - 1][0] != 0:
            temp = True
            first_val = board[len(board) - 1][0]
            for i in range(len(board)):
                if board[len(board) - 1][i] != first_val:
                    temp = False
                    break;

            if temp:
                return first_val

        return None

    def opponent(self, turn):
        if turn == "X":
            return "O"
        elif turn == "O":
            return "X"
        elif turn == 1:
            return 2
        else:
             return 1

    def DoMove(self, position, move):
        "Note that \"moves\" are formatted as: [pieceName, [ypos, xpos]]"
        if position[move[1][0]][move[1][1]] != 0:
            return "illegal move"


        if move[0] == "X":
            piece = 1
        elif move[0] == "O":
            piece = 2
        else:
            piece = move[0]
        new_position = copy.deepcopy(position)
        new_position[move[1][0]][move[1][1]] = piece

        return new_position

    def GenerateMoves(self, position, turn= None):
        "returns a list of possible moves"
        if turn == None:
            num_x = 0
            num_o = 0
            for y in range(len(position)):
                for x in range(len(position[y])):
                    if position[y][x] == 1:
                        num_x += 1
                    elif position[y][x] ==  2:
                        num_o += 1

            if num_x > num_o:
                turn = "O"
            else:
                turn = "X"

        ret_moves = []
        for y in range(len(position)):
            for x in range(len(position[y])):
                if position[y][x] == 0:
                    ret_moves.append([turn, [y, x]])

        return ret_moves

    def PrimitiveValue(self, board):
        "Checks to see if there is connected row"
        for i in range(len(board)):
            if board[i][0] != 0:
                temp = True
                first_val = board[i][0]
                for i2 in range(len(board[i])):
                    if board[i][i2] != first_val:
                        temp = False
                        break;
                if temp:
                    return self.convert_piece(first_val) + " won"
                else:
                    temp = True

        "Checks to see if there is a connected column"
        for i in range(len(board[0])):
            if board[0][i] != 0:
                temp = True
                first_val = board[0][i]
                for i2 in range(len(board[i])):
                    if board[i2][i] != first_val:
                        temp = False
                        break;
                if temp:
                    return self.convert_piece(first_val) + " won"
                else:
                    temp = True

        "Checks for a connected top-left to bottom-right"
        if board[0][0] != 0:
            temp = True
            first_val = board[0][0]

            for i in range(len(board)):
                if board[i][i] != first_val:
                    temp = False
                    break;

            if temp:
                return self.convert_piece(first_val) + " won"

        "Checks for a connected diagonal top-right to bottom-left"
        if board[len(board) - 1][0] != 0:
            temp = True
            first_val = board[len(board) - 1][0]
            for i in range(len(board)):
                if board[len(board) - 1][i] != first_val:
                    temp = False
                    break;

            if temp:
                return self.convert_piece(first_val) + " won"

        contains_0 = False
        for i in range(len(board)):
            for i2 in range(len(board)):
                if board[i][i2] == 0:
                    contains_0 = True
                    break;
            if contains_0:
                break;

        if contains_0:
            return "undecided"

        return "tie"
