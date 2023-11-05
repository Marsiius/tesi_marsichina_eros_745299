import chess.pgn
import io


def _readPGN(pgn_path):
    """
    The function creates a list that contains all the games in the PGN file.

    Args:
        a: PGN path

    Returns:
        A list that contains chess.pgn.game objects.
    """
    pgn_file = open(pgn_path)
    pgn_content = pgn_file.read()
    pgn_file.close()
    pgn_games = []
    pgn = io.StringIO(pgn_content)
    while True:
        game = chess.pgn.read_game(pgn)
        if game is None:
            break
        pgn_games.append(game)

    return pgn_games

partita_numero = 0
# Apri il file PGN
with open("Tools\data\Berserk_Koivisto_0.1.pgn") as pgn:
    # Leggi la partita dal file PGN
    game = chess.pgn.read_game(pgn)
    #cartella e
    games = _readPGN("Tools\data\Berserk_Koivisto_0.1.pgn")
    for game in games:
        player_bianco = ""
        player_nero = ""
        print("Partita numero: "+str(partita_numero))
        partita_numero += 1
        n=1
        # Ottieni il nodo radice della partita
        node = game
        # Itera attraverso tutte le mosse della partita
        while node is not None:
            comment = node.comment
            if comment:
                if n % 2 == 0:
                    #print(str(n)+ " - "+comment + " - Nero")
                    player_nero += comment+","
                else:
                    #print(str(n)+ " - "+comment + " - Bianco")
                    player_bianco += comment+","
                n += 1
                #print(str(n)+ " - "+comment)
                game = chess.pgn.read_game(pgn)
            # Passa al nodo successivo
            node = node.variations[0] if node.variations else None
        with open("Tools/score/new/prova.csv", "a") as file:
            file.write(player_bianco+"\n")
            file.write(player_nero+"\n")
        #print(player_bianco)
        #print(player_nero)
                
