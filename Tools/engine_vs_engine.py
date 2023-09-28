import chess
import chess.engine
import chess.pgn
import os

for num in range(1, 2):
    folder = "pgn/"
    #n = 1
    path = os.path.join(folder, f"{num})_Stockfish_vs_Berserk.pgn")

    engine1 = chess.engine.SimpleEngine.popen_uci(r"C:\Users\eros6\Downloads\stockfish\stockfish-windows-x86-64-modern.exe")
    engine2 = chess.engine.SimpleEngine.popen_uci(r"C:\Users\eros6\Downloads\Berserk-11.1_Windows_x64\Berserk-11.1_Windows_x86-64-avx2.exe")

    game = chess.pgn.Game()
    game.headers["Event"] = "*"
    #game.headers["Site"] = "*"
    #game.headers["Date"] = "*"
    #game.headers["Time"] = "*"
    #game.headers["Round"] = "*"
    game.headers["White"] = "Stockfish 16"
    game.headers["Black"] = "Berserk 11"

    n = 1
    vittorie_engine1 = 0
    vittorie_engine2 = 0
    pareggi = 0
    #ho solo aggiunto la prima mossa fuori dal while, così da avere 
    board = chess.Board()
    result = engine1.play(board, chess.engine.Limit(time=0.1))

    node = game.add_variation(chess.Move.from_uci(str(result.move)))
    board.push(result.move)
    print(str(n)+"------------")
    print(board.unicode())
    while not board.is_game_over():
        n = n+1
        if board.turn == chess.WHITE:
            result = engine1.play(board, chess.engine.Limit(time=0.1))
        else:
            result = engine2.play(board, chess.engine.Limit(time=0.1))
        board.push(result.move)
        #ho aggiunto la riga 35
        node = node.add_variation(chess.Move.from_uci(str(result.move)))
        print(str(n)+"------------")
        print(board.unicode())
    print(board.result())
    
    print("finita la partita tra stockfish e berserk")

    game.headers["Result"] = str(board.result())
    #game.headers["Termination"] = "*"
    #game.headers["ECO"] = "*"
    #game.headers["Opening"] = "*"
    #game.headers["TimeControl"] = "*"
    #game.headers["PlayCount"] = "*"

    with open(path, "w") as pgn:
        pgn.write(str(game))

    print(game)

    engine1.quit()
    engine2.quit()

    if board.result() == "1-0":
        vittorie_engine1 += 1
    elif board.result() == "0-1":
        vittorie_engine2 += 1
    else: pareggi += 1