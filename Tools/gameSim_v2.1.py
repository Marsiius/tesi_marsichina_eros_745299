import chess
import chess.engine
import chess.pgn
import os

folder = "D:/GitHub/tesi_745299/Tools/pgn_gameSim_v2/"
player_white = "Berserk"
player_black = "Koivisto"
timeMove = 0.1
path = os.path.join(folder, f"{player_white}_{player_black}_{timeMove}_fix.pgn")
n=0

partite_crashate = 0
partite_salvate = 0


engine = chess.engine.SimpleEngine.popen_uci(r"D:\GitHub\tesi_745299\Engine\Modelli\stockfish-16\stockfish-windows-x86-64-modern.exe")
engine1 = chess.engine.SimpleEngine.popen_uci(r"D:\GitHub\tesi_745299\Engine\Modelli\4_engine\Berserk-11.1_Windows_x86-64.exe")
engine2 = chess.engine.SimpleEngine.popen_uci(r"D:\GitHub\tesi_745299\Engine\Modelli\4_engine\Koivisto_9.0-windows-avx2-pgo.exe")

#numero di partite che si vogliono simulare
for num in range(1, 5):
    #inizio con il try per vedere se la mossa è legale
    try:
        play_count = 0
        m=0
        n += 1
        print(f"Partita {n} in corso:")
        game = chess.pgn.Game()
        game.headers["Event"] = "*"
        #game.headers["Site"] = "*"
        #game.headers["Date"] = "*"
        #game.headers["Time"] = "*"
        #game.headers["Round"] = "*"
        game.headers["White"] = "Berserk 11"
        game.headers["Black"] = "Koivisto 9"
        game.headers["TimeControl"] = f"movetime: {str(timeMove)}"

        board = chess.Board()
        result = engine1.play(board, chess.engine.Limit(time=timeMove))

        node = game.add_variation(chess.Move.from_uci(str(result.move)))
        
        info = engine.analyse(board, chess.engine.Limit(time=timeMove, depth=15))
        score = float(info["score"].relative.score())/100.0
        node.comment = str(score)
        board.push(result.move)
        print(f"bianco {score}")
        #print(str(n)+"------------")
        #print(board.unicode())
        #print(result.move)
        while not board.is_game_over():
            m += 1
            play_count += 1
            if board.turn == chess.WHITE:
                result = engine1.play(board, chess.engine.Limit(time=timeMove))
                print(f"bianco {score}")
            else:
                result = engine2.play(board, chess.engine.Limit(time=timeMove))
                print(f"nero {score}")
        
            node = node.add_variation(chess.Move.from_uci(str(result.move)))
            #print(str(m)+"------------")
            print(board.unicode())
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
            board.push(result.move)
            
        print(board.result())
        
        print("finita la partita tra stockfish e berserk")

        game.headers["PlayCount"] = str(play_count)
        game.headers["Result"] = str(board.result())

        with open(path, "a") as pgn:
            pgn.write(str(game)+"\n")

        print(game)
        print(f"Partita {n}: Salvata")
        partite_salvate += 1
    except:
        print(f"Partita {n}: crashata")
        partite_crashate += 1
    
engine1.quit()
engine2.quit()

print(f"Partite salvate: {partite_salvate}, partite crashate: {partite_crashate}")

def score(engine):
    board = chess.Board()
    info = engine.analyse(board, chess.engine.Limit(time=1, depth=5))
    score = info["score"].relative.score()
    print(str(score))
    
    