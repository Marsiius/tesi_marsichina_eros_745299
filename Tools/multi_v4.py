import multiprocessing
import time
import chess
import chess.engine
import chess.pgn
import os

folder = "D:/GitHub/tesi_745299/Tools/data"
folder_space = "D:/GitHub/tesi_745299/Tools/pgn_space/"
player_white = "Berserk"
player_black = "Koivisto"
timeMove = 1
path = os.path.join(folder, f"{player_white}_{player_black}_{timeMove}.pgn")
path_space = os.path.join(folder_space, f"{player_white}_{player_black}_{timeMove}.pgn")
n = 0
partite_crashate = 0
partite_salvate = 0

#engine = chess.engine.SimpleEngine.popen_uci(r"C:\Users\eros6\OneDrive\Documenti\GitHub\tesi_745299\Engine\Modelli\stockfish-16\stockfish-windows-x86-64-modern.exe")
#engine1 = chess.engine.SimpleEngine.popen_uci(r"C:\Users\eros6\Downloads\Berserk-11.1_Windows_x64\Berserk-11.1_Windows_x86-64-avx2.exe")
#engine2 = chess.engine.SimpleEngine.popen_uci(r"C:\Users\eros6\Downloads\Koivisto-9.0_Windows_x64\Koivisto_9.0-windows-avx2-pgo.exe")

def game_gen():
    for i in range(1,25):
        global n, partite_crashate, partite_salvate
        engine = chess.engine.SimpleEngine.popen_uci(r"D:\GitHub\tesi_745299\Engine\Modelli\stockfish-16\stockfish-windows-x86-64-modern.exe")
        engine1 = chess.engine.SimpleEngine.popen_uci(r"D:\GitHub\tesi_745299\Engine\Modelli\4_engine\Berserk-11.1_Windows_x86-64.exe")
        engine2 = chess.engine.SimpleEngine.popen_uci(r"D:\GitHub\tesi_745299\Engine\Modelli\4_engine\Koivisto_9.0-windows-avx2-pgo.exe")
        try:
            play_count = 0
            n += 1
            print(f"Partita {i} in corso:")
            game = chess.pgn.Game()
            game.headers["Event"] = "*"
            game.headers["White"] = "Berserk 11"
            game.headers["Black"] = "Koivisto 9"
            game.headers["TimeMoves"] = str(timeMove)

            board = chess.Board()
            
            result = engine1.play(board, chess.engine.Limit(time=timeMove))

            node = game.add_variation(chess.Move.from_uci(str(result.move)))
            info = engine.analyse(board, chess.engine.Limit(time=timeMove, depth=15))
            score = float(info["score"].relative.score())/100.0
            node.comment = str(score)
            board.push(result.move)
            
            while not board.is_game_over():
                play_count += 1
                
                if board.turn == chess.WHITE:
                    result = engine1.play(board, chess.engine.Limit(time=timeMove))
                    node = node.add_variation(chess.Move.from_uci(str(result.move)))
                    #print(str(n)+"------------")
                    #print(board.unicode())
                    info = engine.analyse(board, chess.engine.Limit(time=1, depth=5))
                    try:
                        score = float(info["score"].relative.score()/100.0)
                    except:       
                        score = info["score"].relative.score()
                    node.comment = str(score)
                else:
                    result = engine2.play(board, chess.engine.Limit(time=timeMove))
                    node = node.add_variation(chess.Move.from_uci(str(result.move)))
                    #print(str(n)+"------------")
                    #print(board.unicode())
                    info = engine.analyse(board, chess.engine.Limit(time=1, depth=5))         
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
                pgn.write(str(game) + "\n")
                
            with open(path_space, "a") as pgn:
                pgn.write(str(game) + "\n\n") 

            print(game)
            print(f"Partita {i}: Salvata")
            partite_salvate += 1
        except:
            print(f"Partita {i}: crashata")
            partite_crashate += 1

if __name__ == '__main__':
    p = multiprocessing.Process(target=game_gen)
'''    p1 = multiprocessing.Process(target=game_gen)
    p2 = multiprocessing.Process(target=game_gen)
    p3 = multiprocessing.Process(target=game_gen)'''
    #p4 = multiprocessing.Process(target=game_gen)
    #p5 = multiprocessing.Process(target=game_gen)

p.start()
''' p1.start()
        p2.start()
        p3.start()'''
    #p4.start()
    #p5.start()
    