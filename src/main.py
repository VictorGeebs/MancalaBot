import mancala, mtcs

testboard = [[0, 0, 0, 0, 0, 1],
            [0, 0, 0, 1, 0, 0],
            [22,24],
            0]

#mancala.startgame(testboard)


root = mtcs.Node(state = mancala.Mancala())
mancala.display(root.state.board)

while(root.get_gameover() is False):
    player = root.state.board[3]
    if(player == 0):
        print(f"AI to play:")
        root = mtcs.findMove(root)
    elif(player == 1):
        i = int(input(f"Player {root.state.board[3]+1} to play, enter index to play in: "))
        resultboard = mancala.move(root.state.board, i)
        for child in root.children:
            if(child.state.board == resultboard):
                root = child
    mancala.display(root.state.board)
print("Game over poggers")