from ten_to_zero_game import ten_to_zero
from twentyfive_to_zero_game import twentyfive_to_zero
from num_to_zero import Num_to_zero
from tic_tac_toe import Tic_Tac_Toe
import copy
import solver
import random

def tester(game, position):
    for i in range(position, 0, -1):
        print(str(i) + ": " + solver.Solve(game, i))

def tic_tac_toe_tester(board, positions = {}, results = {}):
    height = len(board)
    width = len(board[0])

    generate_moves = game.GenerateMoves
    hashencode = game.hashencode
    DoMove = game.DoMove

    if results == {}:
        results = {"win": 0, "lose": 0, "tie": 0, "primitive win": 0, "primitive lose": 0, "primitive_tie": 0}

    for moves in generate_moves(position):
        board = game.DoMove(position)
        board_hash = hashencode(board)

def print_positions(game, dict):
    print_board = game.print_board
    hashdecode = game.hashdecode

    for keys in dict:
        print("result: " + dict[keys])
        print_board(hashdecode(keys))
        print("=============")

def fake_solver(game, board):
    game.print_board(board)
    prim_val = game.primitive_positions(board)
    print(prim_val)
    while not prim_val:
        board = game.DoMove(board, random.choice(game.GenerateMoves(board)))
        game.print_board(board)
        prim_val = game.primitive_positions(board)

    return "none"

# print(solver.Solve(ten_to_zero(), 10))
# tester(ten_to_zero(), 10)
# print("")
# tester(ten_to_zero(), 100)
# print("")
# tester(twentyfive_to_zero(), 25)

# tic_game = Tic_Tac_Toe()

# blank_board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
# board_1 = [[1, 0, 0], [2, 1, 1], [1, 0, 1]]
# board_2 = [[0, 2, 1], [1, 2, 1], [2, 2, 0]]
# board_3 = [[0, 1, 2], [2, 1, 2], [1, 1, 0]]
# board_4 = [[0, 2, 1], [1, 0, 1], [2, 2, 0]]


print(egcd(227*421, 13))

print("")

print(egcd(31*11, 31*11*12))
