import random
import time

board_state = [
    7, 7, 7, 7, 7, 7, 7, 7, 7, 7,
    7, 7, 7, 7, 7, 7, 7, 7, 7, 7,
    7, 53, 51, 52, 54, 50, 52, 51, 53, 7,
    7, 49, 49, 49, 49, 49, 49, 49, 49, 7,
    7, 0, 0, 0, 0, 0, 0, 0, 0, 7,
    7, 0, 0, 0, 0, 0, 0, 0, 0, 7,
    7, 0, 0, 0, 0, 0, 0, 0, 0, 7,
    7, 0, 0, 0, 0, 0, 0, 0, 0, 7,
    7, 57, 57, 57, 57, 57, 57, 57, 57, 7,
    7, 61, 59, 60, 62, 58, 60, 59, 61, 7,
    7, 7, 7, 7, 7, 7, 7, 7, 7, 7,
    7, 7, 7, 7, 7, 7, 7, 7, 7, 7
]

piece_codes = [
    53, 51, 52, 54, 50, 52, 51, 53,
    49, 49, 49, 49, 49, 49, 49, 49,
    57, 57, 57, 57, 57, 57, 57, 57,
    61, 59, 60, 62, 58, 60, 59, 61,
    0, 7, 0, 20, 19, 34, 62, -1, 1,
    -10, 10, -11, -9, 9, 11, 10, 20,
    -11, -9, -10, -20, -21, -19, -12,
    -8, 8, 12, 19, 21, 45, 39, 53, 43,
    39, 39, -32, 15, 10, 14, 13, 12, 11,
    -32, -32, 9, 4, 8, 7, 6, 5
]

board_size = 10
max_moves = 15
previous_position = 0
cell_position = previous_position
y = 0
u = 0

def render_board(board_state, board_size=10):
    unicode_pieces = {
        1: "\u2659",  # Pawn
        2: "\u2656",  # Rook
        3: "\u2658",  # Knight
        4: "\u2657",  # Bishop
        5: "\u2655",  # Queen
        6: "\u2654",  # King
        9: "\u265F",  # Opponent's Pawn
        10: "\u265C",  # Opponent's Rook
        11: "\u265E",  # Opponent's Knight
        12: "\u265D",  # Opponent's Bishop
        13: "\u265B",  # Opponent's Queen
        14: "\u265A",  # Opponent's King
        0: " "         # Empty square
    }

    print("+" + "---+" * board_size)
    for row in range(0, (board_size+1)):
        print("|", end=" ")
        for col in range(0, board_size):
            piece = board_state[row * board_size + col]
            symbol = unicode_pieces.get(piece & 15, " ")
            print(f"{symbol} ", end="")
        print("|")
        print("+" + "---+" * board_size)


def calculate_move(player_color, depth, last_position, max_depth, evaluation):
    global board_state, piece_codes, max_moves, board_size,previous_position,cell_position,y,u  # Use global variables
    board_index = 20
    max_score = -1e8
    forced_move = max_depth and calculate_move(player_color, 0, None, None, None) > 1e4
    player_color ^= 8
    evaluation_constant = (78 - depth) << 9
    move_direction = board_size if player_color else -board_size

    while board_index + 1 < 99:
        board_index += 1
        
        current_position = board_index
        current_piece = board_state[current_position]
        piece_type = current_piece & max_moves ^ player_color
        if current_piece and piece_type < 7:

            move_type = 8 if (piece_type & 2) else 4
            piece_type -= 1  # pieceType'ı bir azaltıyoruz
            piece_code = piece_codes[61 + piece_type] if (9 - current_piece & max_moves) else 49

            while True:
                current_position += piece_codes[piece_code]
                target_piece = board_state[current_position]
                move_adjustment = target_position = 0 if (piece_type | (current_position + move_direction - last_position)) else last_position

                if (
                    not target_piece and (piece_type or move_type < 3 or move_adjustment) or 
                    (1 + target_piece & max_moves ^ player_color) > 9 and piece_type | move_type > 2
                ):

                    if not (2 - (target_piece & 7)): 
                        return evaluation_constant

                    # Başlangıç kısmı for loop
                    next_move = valid_moves = (piece_type | board_state[current_position - move_direction] - 7) and (current_piece & max_moves) or (6 ^ player_color)

                    # Döngü
                    while next_move:
                        # moveAdjustment ve targetPosition hesaplamaları
                        move_adjustment = current_position
                        if current_position < board_index:
                            target_position = move_adjustment - 3
                        else:
                            target_position = move_adjustment + 2

                        # Koşul kısmı
                        if not next_move and not forced_move:
                            if not (board_state[target_position] < max_moves or
                                    board_state[target_position + board_index - current_position] or
                                    board_state[current_position] + (current_position - board_index)):
                                break
                        
                        # Iterasyon kısmı
                        next_move = not next_move and not forced_move and not (
                            move_adjustment := current_position, 
                            target_position := current_position < board_index and move_adjustment - 3 or move_adjustment + 2, 
                            board_state[target_position] < max_moves or 
                            board_state[target_position + board_index - current_position] or
                            board_state[current_position] + current_position - board_index
                        )

                        if target_piece:
                            move_score_part1 = piece_codes[(target_piece & 7) | 32] * 2 - depth - piece_type
                        else:
                            move_score_part1 = 0

                        if piece_type:
                            move_score_part2 = 0
                        else:
                            if valid_moves - current_piece & max_moves:
                                move_score_part2 = 110
                            else:
                                move_score_part2 = (14 if target_position else 0) + (1 if move_type < 2 else 0) + 1

                        move_score = move_score_part1 + move_score_part2

                        if max_depth > depth or (1 < max_depth and max_depth == depth and move_score > 2) or forced_move:
                            board_state[current_position] = valid_moves
                            board_state[move_adjustment] = board_state[target_position]
                            board_state[board_index] = 0 if target_position else 0

                            next_move = 0 if move_type > 1 else current_position
                            move_score -= calculate_move(player_color, depth + 1, next_move, max_depth, move_score - max_score)

                            if not (depth or (max_depth - 1) or (cell_position - board_index) or 
                                    (current_position - previous_position) or (move_score < -1e4)):
                                render_board(y=next_move)
                                if player_color:
                                    time.sleep(0.075)
                                    calculate_move(8, 0, next_move, 2)
                                    calculate_move(8, 0, next_move, 1)

                            next_move = 1 - piece_type | (move_type < 7) | target_position or not max_depth or target_piece or current_piece < max_moves or calculate_move(player_color, 0) > 1e4
                            board_state[board_index] = current_piece
                            board_state[current_position] = target_piece
                            board_state[target_position] = board_state[move_adjustment]
                            if target_position:
                                board_state[move_adjustment] = 0 if piece_type else (9 ^ player_color)
                            else:
                                board_state[move_adjustment] = 0

                        if move_score > max_score or (not depth and move_score == max_score and random.random() < 0.5):
                            if max_score == move_score and max_depth > 1:
                                if depth:
                                    if evaluation - move_score < 0:
                                        return max_score
                                else:
                                    cell_position = board_index
                                    previous_position = current_position
                                    return max_score

                        # Koşul sağlanmazsa döngüden çık
                        if not target_piece and piece_type > 2 or (
                            current_position == board_index and (piece_type | move_type > 2) or
                            (max_moves < current_piece and not target_piece and piece_code + 1 * (move_type - 1))
                        ):
                            break
    return -evaluation_constant + 768 < max_score or (forced_move and max_score)
