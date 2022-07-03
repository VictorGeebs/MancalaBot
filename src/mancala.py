import copy

default_mancala_board = [[4, 4, 4, 4, 4, 4],
                        [4, 4, 4, 4, 4, 4],
                        [0,0],
                        0]

class Mancala():
    def __init__(self, board=default_mancala_board):
        self.board = board

    def generate_states(self):
        player = self.board[3]
        legal_moves = [i for i, v in enumerate(self.board[player]) if v != 0]
        return [Mancala(move(copy.deepcopy(self.board), i)) for i in legal_moves]
    
    def get_gameover(self):
        if(self.board[3] == -1):
            return True
        return False

    def get_reward(self, player):
        if self.get_gameover():
            if self.board[2][player] > 24:
                return 1
            if self.board[2][player] < 24:
                return -1
        return 0
    
    def get_player(self):
        return self.board[3]

def display(board):
    print()
    print(f"Player {board[3]} to play")
    print(board[2][1], list(reversed(board[1])))
    print(" ", board[0], board[2][0])
    print()

def move(board, index):
    player = board[3]
    curr_player = player
    nb_stones = board[curr_player][index]
    
    # Selected index was empty
    if nb_stones == 0:
        return board

    # Empty selected index
    board[curr_player][index] = 0
    
    # Iterate through the board
    while nb_stones > 0:
        index += 1
        if index > 5: # reached end of row
            index = 0 # reset index
            if curr_player == player: # if own row, drop stone in endzone and check turn
                board[2][player] += 1
                nb_stones -= 1
                if nb_stones == 0:
                    if(all(v == 0 for v in board[0])):
                        nb_leftover = sum(board[1])
                        board[2][0] += nb_leftover
                        board[1] = [0 for x in range(6)]
                        board[3] = -1
                        return board
                    if(all(v == 0 for v in board[1])):
                        nb_leftover = sum(board[0])
                        board[2][1] += nb_leftover
                        board[0] = [0 for x in range(6)]
                        board[3] = -1
                        return board
                    return board
            
            curr_player = -curr_player + 1 # invert player index 0 -> 1 or 1 -> 0
        
        board[curr_player][index] += 1
        nb_stones -= 1
    
    # If landed in empty spot, empty and dump into corresponding player
    if board[curr_player][index] == 1:
        curr_player = -curr_player + 1
        board[2][player] += board[curr_player][5-index]
        board[curr_player][5-index] = 0
    
    # Check if game is over
    if(all(v == 0 for v in board[0])):
        nb_leftover = sum(board[1])
        board[2][0] += nb_leftover
        board[1] = [0 for x in range(6)]
        board[3] = -1
        return board
    if(all(v == 0 for v in board[1])):
        nb_leftover = sum(board[0])
        board[2][1] += nb_leftover
        board[0] = [0 for x in range(6)]
        board[3] = -1
        return board
    
    # Pass turn to other player
    board[3] = -player + 1
    return board

def startgame(board):
    while(board[3] != -1):
        display(board)
        i = int(input(f"Player {board[3]+1} to play, enter index to play in: "))
        move(board, i)
    display(board)
    print("Game over poggers")

#movelist = [2,3,5,1,0,2,1,0,5,4,2,4,2,4,1,0,3,0,2,3,0,1,1,4,2,2,3,4,5,4,4,5,3,5,0,2,1,1,2]
#startgame(board)
