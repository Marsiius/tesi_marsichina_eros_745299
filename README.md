# tesi_marsichina_eros_745299

### About thesis :chess_pawn:

## Linked repositories:
- https://github.com/Luca9862/tirocinio_lucacanali
- https://github.com/AtreusArtic/tesi_739088
- https://github.com/marikascalise/ThesisAIchess

## Repository Structure:
- Dataset
- Engine
- Tools

### Dataset
- The dataset folder contains all the available research data: PGN files, CSV files, graphs and everything related to data and analysis.

### Engine
- The engine folder contains all the engines used to simulate matches against each other:
The selected engines:
- Berserk 11.1 [Resource Code](https://github.com/jhonnold/berserk)
- Koivisto 9 [Resource Code](https://github.com/Luecx/Koivisto)
- Leela Chess Zero [Resource Code](https://github.com/LeelaChessZero/lc0)
- RubyChess [Resource Code](https://github.com/Matthies/RubiChess)

### Tools
The Tools folder contains all script useful to create, manage and analyze data.

### GameSimulator
GameSimulator can generate matches between 2 engines: 
There's 2 features:
- Create PGN of the match
- Calculate the score of the moves
Score is calculated with Stockfish 16

### 
is able to extract the score from each game of PGN, splitting up the score for each turn for black and white 

### External Tools
- Sim03 [Download here](https://komodochess.com/downloads.htm)

Sim03 estimate a loosely defined relation between (two) chess engines concerning their positional playing style, therefor mostly dependent on their evaluation features and weights

Below, similarity results of the Selected engine :shipit:




