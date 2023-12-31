import chess
import chess.engine
import chess.pgn
import os

folder = "D:/GitHub/tesi_745299/Tools/pgn/"
folder_space = "D:/GitHub/tesi_745299/Tools/pgn_space/"
player_white = "Berserk"
player_black = "RubiChess"
timeMove = 1
path = os.path.join(folder, f"{player_white}_{player_black}_{timeMove}.pgn")
path_space = os.path.join(folder_space, f"{player_white}_{player_black}_{timeMove}_space.pgn")
n=0

partite_crashate = 0
partite_salvate = 0

engine = chess.engine.SimpleEngine.popen_uci(r"D:\GitHub\tesi_745299\Engine\Modelli\stockfish-16\stockfish-windows-x86-64-modern.exe")
engine1 = chess.engine.SimpleEngine.popen_uci(r"D:\GitHub\tesi_745299\Engine\Modelli\4_engine\Berserk-11.1_Windows_x86-64.exe")
engine2 = chess.engine.SimpleEngine.popen_uci(r"D:\Download\RubiChess-20230918\windows\RubiChess-20230918_x86-64-avx2.exe")
'''
D:\GitHub\tesi_745299\Engine\Modelli\4_engine\RubiChess-20230918_x86-64-avx2.exe
D:\GitHub\tesi_745299\Engine\Modelli\4_engine\Koivisto_9.0-windows-avx2-pgo.exe
D:\GitHub\tesi_745299\Engine/Modelli/4_engine/lc0-v0.30.0-windows-cpu-dnnl/lc0.exe
D:\Download\RubiChess-20230918\windows\RubiChess-20230918_x86-64-avx2.exe

'''
#numero di partite che si vogliono simulare
for num in range(1, 51):
    #inizio con il try per vedere se la mossa è legale
    try:
        play_count = 0
        m=0
        n += 1
        print(f"Partita {n} in corso:")
        game = chess.pgn.Game()
        game.headers["Event"] = "*"
        game.headers["White"] = player_white
        game.headers["Black"] = player_black
        game.headers["TimeControl"] = str(timeMove)
#f"movetime: {str(timeMove)}"
        board = chess.Board()
        result = engine1.play(board, chess.engine.Limit(time=timeMove))

        node = game.add_variation(chess.Move.from_uci(str(result.move)))
        
        info = engine.analyse(board, chess.engine.Limit(time=1, depth=15))
        score = float(info["score"].relative.score())/100.0
        node.comment = str(score)
        print(f"bianco {score}")
        board.push(result.move)
        #print(str(n)+"------------")
        #print(board.unicode())
        #print(result.move)
        while not board.is_game_over():
            m += 1
            play_count += 1
            if board.turn == chess.WHITE:
                result = engine1.play(board, chess.engine.Limit(time=timeMove))
            else:
                result = engine2.play(board, chess.engine.Limit(time=timeMove))
        
            node = node.add_variation(chess.Move.from_uci(str(result.move)))
            #print(str(m)+"------------")
            #print(board.unicode())
            info = engine.analyse(board, chess.engine.Limit(time=1000, depth=5))
            try:
                score = float(info["score"].relative.score()/100.0)
            except:
                score = info["score"].relative.score()
            node.comment = str(score)
            print(score)
            board.push(result.move)
            
        print(board.result())
        
        print("finita la partita tra stockfish e berserk")

        game.headers["PlayCount"] = str(play_count)
        game.headers["Result"] = str(board.result())

        with open(path, "a") as pgn:
            pgn.write(str(game)+"\n")
            
        with open(path_space, "a") as pgn:
            pgn.write(str(game)+"\n\n")

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
    
    