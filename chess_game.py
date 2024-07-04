
import chess
import chess.engine

def evaluate_board(board):
    # Simple evaluation function: Material count
    eval_value = 0
    for square in chess.SQUARES:
        piece = board.piece_at(square)
        if piece:
            value = get_piece_value(piece)
            eval_value += value if piece.color == chess.WHITE else -value
    return eval_value

def get_piece_value(piece):
    if piece.piece_type == chess.PAWN:
        return 1
    elif piece.piece_type == chess.KNIGHT or piece.piece_type == chess.BISHOP:
        return 3
    elif piece.piece_type == chess.ROOK:
        return 5
    elif piece.piece_type == chess.QUEEN:
        return 9
    elif piece.piece_type == chess.KING:
        return 0
    return 0

def main():
    board = chess.Board()
    while not board.is_game_over():
        print(board)
        print("Evaluation: ", evaluate_board(board))
        
        # Get user move
        user_move = input("Enter your move: ")
        try:
            move = chess.Move.from_uci(user_move)
            if move in board.legal_moves:
                board.push(move)
            else:
                print("Illegal move, try again.")
        except ValueError:
            print("Invalid move format, use UCI notation (e.g., e2e4).")

        # Check if game is over
        if board.is_game_over():
            break

        # Get AI move (random for simplicity)
        ai_move = chess.Move.from_uci(str(list(board.legal_moves)[0]))
        board.push(ai_move)
        print(f"AI move: {ai_move}")

    print("Game over!")
    print(board.result())

if __name__ == "__main__":
    main()
