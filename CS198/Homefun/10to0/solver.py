from ten_to_zero_game import ten_to_zero

def no_turn_solver(game, position, prev_positions = {}, remoteness = []):
    """"Determines whether the current position is
    a winning position for the person who plays this
    move"""
    GenerateMoves = game.GenerateMoves
    DoMove = game.DoMove
    PrimitiveValue = game.PrimitiveValue
    my_remoteness = []

    if position in prev_positions:
        return prev_positions[position]

    result = PrimitiveValue(position)

    if result == "undecided":
        has_tie = False
        reset_remoteness = False
        for move in GenerateMoves(position):
            after_move_result = Solve(game, DoMove(position,  move), remoteness = my_remoteness)
            if after_move_result == "lose":
                prev_positions[position] = "win"
                result = "win"

                if len(remoteness) >= 1:
                    my_remoteness[0] = min(my_remoteness[0], remoteness[0] - 1)
                    remoteness[0] = my_remoteness[0] + 1
                else:
                    remoteness.append(my_remoteness[0] + 1)

            elif after_move_result == "tie":
                has_tie = True
        if has_tie and result != "win":
            prev_positions[position] = "tie"
            result = "tie"
            if len(remoteness) >= 1:
                remoteness[0] = min(my_remoteness[0] + 1, remoteness[0])
            else:
                remoteness.append(my_remoteness[0] + 1)
        else:
            prev_positions[position] = "lose"
            result = "lose"
            if len(remoteness) >= 1:
                remoteness[0] = min(my_remoteness[0] + 1, remoteness[0])
            else:
                print("I shouldn't be here")
                remoteness.append(my_remoteness[0] + 1)
        return result
    else:
        if result == "lose" and len(remoteness) == 0:
            remoteness.append(0)
        else:
            remoteness[0] = 0
        return result

def turn_based_solver(game, position, turn, prev_positions = {}, save_result_to = None, remoteness = []):
    print(position)
    """"Determines whether the current position is
    a winning position for the person who plays this
    move
    wins must be formatted as such: \"[turn] won\" """
    assert turn != None, "Turn cannot be left blank"
    GenerateMoves = game.GenerateMoves
    DoMove = game.DoMove
    PrimitiveValue = game.PrimitiveValue
    players = game.players
    opponent = game.opponent
    hashencode = game.hashencode
    hashdecode = game.hashdecode
    convert_piece = game.convert_piece
    my_remoteness = []

    if type(turn) is not str:
        turn = convert_piece(turn)
    if save_result_to == None:
        save_result_to = {"Primitive " + turn + " won": 0, "Primitive " + opponent(turn) + " won":  0,\
        "Primitive tie": 0, "X won" : 0, "O won": 0, "tie": 0}

    # print("=============")
    # game.print_board(position)
    # print("=============")
    a = prev_positions
    hash_position = hashencode(position)
    if hash_position in prev_positions:
        return prev_positions[hash_position]

    result = PrimitiveValue(position)

    if result == "undecided":
        has_tie = False
        has_win = False
        for moves in GenerateMoves(position, turn):
            after_move_result = Solve(game, DoMove(position, moves), \
                prev_positions, opponent(turn), save_result_to)


            if type(turn) is str:
                if after_move_result == turn + " won":
                    has_win = True
                elif after_move_result == "tie":
                    has_tie = True
            else:
                if after_move_result == convert_piece(turn) + " won":
                    has_win = True
                elif after_move_result == "tie":
                    has_tie = True

        if has_win:
            if type(turn) is str:
                prev_positions[hash_position] = turn + " won"
                save_result_to[turn + " won"] += 1
                return turn + " won"
            else:
                prev_positions[hash_position] = convert_piece(turn) + " won"
                save_result_to[convert_piece(turn) + " won"] += 1
                return convert_piece(turn) + " won"

        elif has_tie:
            prev_positions[hash_position] = "tie"
            save_result_to["tie"] += 1
            return "tie"

        else:
            if type(turn) is int:
                prev_positions[hash_position] = convert_piece(opponent(turn)) + " won"
                save_result_to[convert_piece(opponent(turn)) + " won"] += 1
                return convert_piece(opponent(turn)) + " won"
            else:
                prev_positions[hash_position] = opponent(turn) + " won"
                save_result_to[opponent(turn) + " won"] += 1
                return opponent(turn) + " won"
    else:
        prev_positions[hash_position] = result
        save_result_to["Primitive " + result] += 1
        return result

def Solve(game, position, prev_positions = {}, turn = None, save_result_to = None, remoteness = []):
    try:
        game.piece_based
    except AttributeError:
        game.piece_based = False

    if turn == None and not game.piece_based:
        return no_turn_solver(game, position, prev_positions, remoteness)
    else:
        return turn_based_solver(game, position, turn, prev_positions, save_result_to, remoteness)
