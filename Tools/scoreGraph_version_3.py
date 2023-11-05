import csv
import matplotlib.pyplot as plt

avg_score_player_1 = []
avg_score_player_2 = []
# Apre il file CSV in modalità di lettura

for i in range (0,27):
    
    with open("Tools/score/new/AllScores_v2_5.csv", "r") as f:
        lines = csv.reader(f)
        
        avg_player_1_temp = 0
        avg_player_2_temp = 0
        # Inizializza un contatore per tener traccia delle righe
        numero_riga = 0.0

        for line in lines:
            # Incrementa il contatore di riga
            numero_riga += 1

            # Verifica se il numero di riga è pari o dispari
            if numero_riga % 2 == 0:
                # Questa è una riga pari
                avg_player_2_temp += float(line[i])
                print(f"Player 2: {line[1]}")
            else:
                # Questa è una riga dispari
                avg_player_1_temp += float(line[i])
                print(f"player 1: {line[i]}")
                    
            tot_lines = float(numero_riga/2)
            
        avg_score_player_1.append(avg_player_1_temp/tot_lines)
        avg_score_player_2.append(avg_player_2_temp/tot_lines)

    print(avg_score_player_1)
    print(avg_score_player_2)
    
    n = len(avg_score_player_1)
    player_1_score_n = [i for i in range(1, n + 1)]
    m= len(avg_score_player_2)
    player_2_score_n = [i for i in range(1, m + 1)]
    
plt.figure(figsize=(8, 6))
plt.plot(player_1_score_n, avg_score_player_1, label='Giocatore 1')
plt.plot(player_2_score_n, avg_score_player_2, label='Giocatore 2')
#plt.plot(score_2_sorted, label='Giocatore 2')

# Etichette degli assi
plt.xlabel('Numero di mosse')
plt.ylabel('Punteggio')

# Legenda
plt.legend()

# Titolo del grafico
plt.title('Grafico dei punteggi')

# Visualizza il grafico
plt.grid()
plt.show()
    
