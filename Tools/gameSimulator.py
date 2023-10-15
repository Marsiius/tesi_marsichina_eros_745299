import chess
import chess.engine
import chess.pgn
import os

folder = "pgn_gameSim/"
player_white = "Berserk"
player_black = "Koivisto"
timeMove = 0.1
path = os.path.join(folder, f"{player_white}_{player_black}_{timeMove}.pgn")

engine = chess.engine.SimpleEngine.popen_uci(r"C:\Users\eros6\OneDrive\Documenti\GitHub\tesi_745299\Engine\Modelli\stockfish-16\stockfish-windows-x86-64-modern.exe")
engine1 = chess.engine.SimpleEngine.popen_uci(r"C:\Users\eros6\Downloads\Berserk-11.1_Windows_x64\Berserk-11.1_Windows_x86-64-avx2.exe")
engine2 = chess.engine.SimpleEngine.popen_uci(r"C:\Users\eros6\Downloads\Koivisto-9.0_Windows_x64\Koivisto_9.0-windows-avx2-pgo.exe")

#numero di partite che si vogliono simulare
for num in range(1, 2):
    n = 1
    game = chess.pgn.Game()
    game.headers["Event"] = "*"
    game.headers["White"] = "Berserk 11"
    game.headers["Black"] = "Koivisto 9"
    game.headers["Time"] = str(timeMove)

    board = chess.Board()
    result = engine1.play(board, chess.engine.Limit(time=timeMove))

    node = game.add_variation(chess.Move.from_uci(str(result.move)))
    board.push(result.move)
    info = engine.analyse(board, chess.engine.Limit(time=timeMove, depth=15))
    score = float(info["score"].relative.score())/100.0
    node.comment = str(score)
    print(str(n)+"------------")
    print(board.unicode())
    while not board.is_game_over():
        n += 1
        if board.turn == chess.WHITE:
            result = engine1.play(board, chess.engine.Limit(time=timeMove))
        else:
            result = engine2.play(board, chess.engine.Limit(time=timeMove))
        board.push(result.move)
        
        node = node.add_variation(chess.Move.from_uci(str(result.move)))
        print(str(n)+"------------")
        #print(board.unicode())
        info = engine.analyse(board, chess.engine.Limit(time=1, depth=5))
        #score = info["score"].relative.score()
        #sistemare questo if che non funziona
        #obiettivo: se lo score può essere convertito in float, allora mi stampa il numero/100.0
        #se invece non può essere un float(quindi è None), mi stampa il None senza dividere per 100.0
        #if float(info["score"].relative.score()):
        #    node.comment = str(float(score)/100.0)
        #else:
        #    node.comment = str(score)
        try:
            score = float(info["score"].relative.score()/100.0)
        except:
            score = info["score"].relative.score()
        node.comment = str(score)
    #stampo il risultato finale della partita (1-0, 0-1, 1/2-1/2)
    print(board.result())
    
    print("finita la partita tra stockfish e berserk")

    game.headers["Result"] = str(board.result())

    with open(path, "a") as pgn:
        pgn.write(str(game)+"\n")

    print(game)
    
engine1.quit()
engine2.quit()

def score(engine):
    board = chess.Board()
    info = engine.analyse(board, chess.engine.Limit(time=timeMove, depth=5))
    score = info["score"].relative.score()
    print(str(score))
    
    