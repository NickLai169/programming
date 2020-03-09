class Game:
    primitive_position = [0]
    possible_moves = []


    def primitive_positions(self, position):
        if position in self.primitive_position:
            return True
        else:
            return False

    def DoMove(self, position, move):
        if not move in self.possible_moves or position - move < 0:
            return "illegal move"

        if self.primitive_positions(position):
            return "lose"

        return position - move

    def GenerateMoves(self, position):
        "returns a list of possible moves"
        ret_moves = []
        for move in self.possible_moves:
            if self.DoMove(position, move) != "illegal move" and type(self.DoMove(position, move)) != "String":
                ret_moves.append(move)

        return ret_moves

    def PrimitiveValue(self, position):
        if self.primitive_positions(position):
            return "lose"
        else:
            return "undecided"
