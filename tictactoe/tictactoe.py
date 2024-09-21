"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    n = 0
    for row in board:
        for i in row:
            if i == X:
                n+=1
            elif i == O:
                n-=1
    return X if n==0 else O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actions_set = set()
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == EMPTY:
                actions_set.add((i,j))
    return actions_set


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    new_board = copy.deepcopy(board)
    i, j = action
    if board[i][j] != EMPTY:
        raise Exception
    new_board[i][j] = player(board)
    return new_board

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for i in range(len(board)):
        if (board[i][0] == board[i][1] == board[i][2]) and board[i][0] != EMPTY:
            return board[i][0]
        elif (board[0][i] == board[1][i] == board[2][i]) and board[0][i] != EMPTY:
            return board[0][i]
    if (board[0][0] == board[1][1] == board[2][2]) and board[0][0] != EMPTY:
        return board[0][0]
    if (board[2][0] == board[1][1] == board[0][2]) and board[2][0] != EMPTY:
        return board[2][0]
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) != None: return True
    for row in board:
        for e in row:
            if e == EMPTY:
                return False
    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    result = winner(board)
    if result == X: return 1
    elif result == O: return -1
    else: return 0

def minimaxvalue(board):
    if terminal(board):
        return utility(board)
    
    if player(board) == X:
        value = -2
        for action in actions(board):
            value = max(value, minimaxvalue(result(board,action)))
        return value
    if player(board) == O:
        value = 2
        for action in actions(board):
            value = min(value, minimaxvalue(result(board,action)))
        return value 

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    actions_dict = {
        1: list(),
        0: list(),
        -1: list()
    }
    for action in actions(board):
        actions_dict[minimaxvalue(result(board, action))].append(action)
    print(board)
    if player(board) == X:
        if len(actions_dict[1]) != 0:
            return actions_dict[1][0]
        if len(actions_dict[0]) != 0:
            return actions_dict[0][0]
        return actions_dict[-1][0]
    else:
        if len(actions_dict[-1]) != 0:
            return actions_dict[-1][0]
        if len(actions_dict[0]) != 0:
            return actions_dict[0][0]
        return actions_dict[1][0]
    

