import chess

class MinimaxBot:
    def __init__(self, depth=2):
        self.depth = depth

    def minimax(self, board, depth, maximizing_player):
        """
        Minimax algorithm to calculate the best move.

        :param board: The current chess board.
        :param depth: The depth to search.
        :param maximizing_player: True if maximizing player's turn, else False.
        :return: A tuple of (evaluation, move).
        """
        if depth == 0 or board.is_game_over():
            return self.evaluate_board(board), None

        best_move = None

        if maximizing_player:
            max_eval = float('-inf')
            for move in board.legal_moves:
                board.push(move)
                eval, _ = self.minimax(board, depth - 1, False)
                board.pop()
                if eval > max_eval:
                    max_eval = eval
                    best_move = move
            return max_eval, best_move
        else:
            min_eval = float('inf')
            for move in board.legal_moves:
                board.push(move)
                eval, _ = self.minimax(board, depth - 1, True)
                board.pop()
                if eval < min_eval:
                    min_eval = eval
                    best_move = move
            return min_eval, best_move

    def evaluate_board(self, board):
        """
        A simple evaluation function for the board.

        :param board: The current chess board.
        :return: An integer evaluation of the board.
        """
        piece_values = {
            chess.PAWN: 1,
            chess.KNIGHT: 3,
            chess.BISHOP: 3,
            chess.ROOK: 5,
            chess.QUEEN: 9,
            chess.KING: 0
        }
        evaluation = 0
        for square in chess.SQUARES:
            piece = board.piece_at(square)
            if piece:
                value = piece_values.get(piece.piece_type, 0)
                if piece.color == chess.WHITE:
                    evaluation += value
                else:
                    evaluation -= value
        return evaluation

    def calculate_best_move(self, fen):
        """
        Calculate the best move using the minimax algorithm.

        :param fen: The FEN string representing the chessboard state.
        :return: A tuple containing the best move in UCI format and the new FEN notation.
        """
        board = chess.Board(fen)
        _, best_move = self.minimax(board, self.depth, board.turn)
        if best_move:
            board.push(best_move)
            return best_move.uci(), board.fen()
        else:
            raise ValueError("No legal moves available.")

if __name__ == "__main__":
    import sys

    if len(sys.argv) != 2:
        print("Usage: python bot.py <FEN>")
        sys.exit(1)

    fen = sys.argv[1]
    bot = MinimaxBot(depth=2)

    try:
        best_move, new_fen = bot.calculate_best_move(fen)
        print(f"Best move: {best_move}")
        print(f"New FEN: {new_fen}")
    except Exception as e:
        print(f"Error: {e}")

