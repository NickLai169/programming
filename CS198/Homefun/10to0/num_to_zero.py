from generic_game import Game

class Num_to_zero(Game):
    primitive_position = [0]
    possible_moves = [1, 2]

    def __init__(self, p_moves):
        self.possible_moves = p_moves
