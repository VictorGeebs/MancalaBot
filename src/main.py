import mancala, mcts, node, random

testboard = [[0, 0, 0, 0, 2, 2],
            [0, 0, 0, 0, 0, 1],
            [21,22],
            0]

def simulate_random_winrate(n_games=100):
    wins = 0
    losses = 0
    draws = 0
    for i in range(n_games):
        root = node.Node(state = mancala.Mancala())
        #mancala.display(root.state.board)

        while(root.state.get_gameover() is False):
            if root.state.get_player() == 0:
                root = random.choice(list(root.generate_states()))
            else:
                root = mcts.findMove(root)
            #mancala.display(root.state.board)
            root = node.Node(state = mancala.Mancala(board = root.state.board))
        #mancala.display(root.state.board)
        reward = root.state.get_reward(1)
        if reward == 1:
            wins += 1
            print("win")
        elif reward == -1:
            losses += 1
            print("loss")
        else:
            draws += 1
            print("draw")

    print(f"Wins: {wins}, Losses: {losses}, Draws: {draws}")

def AI_vs_AI_winrate(n_games=100):
    wins = 0
    losses = 0
    draws = 0
    for i in range(n_games):
        root = node.Node(state = mancala.Mancala())
        #mancala.display(root.state.board)

        while(root.state.get_gameover() is False):
            if root.state.get_player() == 1:
                root = mcts.findMove_avg(root, 20)
            else:
                root = mcts.findMove(root)
            #mancala.display(root.state.board)
            root = node.Node(state = mancala.Mancala(board = root.state.board))
        #mancala.display(root.state.board)
        reward = root.state.get_reward(0)
        if reward == 1:
            wins += 1
            print("win")
        elif reward == -1:
            losses += 1
            print("loss")
        else:
            draws += 1
            print("draw")

    print(f"Wins: {wins}, Losses: {losses}, Draws: {draws}")

def play_against_AI():
    root = node.Node(state = mancala.Mancala())
    mancala.display(root.state.board)
    while(root.state.get_gameover() is False):
        player = root.state.board[3]
        if(player == 0):
            print(f"AI to play:")
            root = mcts.findMove(root)
        elif(player == 1):
            i = int(input(f"Player {root.state.board[3]} to play, enter index to play in: "))
            resultboard = mancala.move(root.state.board, i)
            for child in root.children:
                if(child.state.board == resultboard):
                    root = child
        mancala.display(root.state.board)
    print("Game over poggers")
    
AI_vs_AI_winrate()