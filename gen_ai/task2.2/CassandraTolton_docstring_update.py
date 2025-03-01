
"""
Check if the current player has won the game.

This method checks all the possible winning conditions for the current player:
- All cells in any row are the same (and not empty).
- All cells in any column are the same (and not empty).
- All cells in the two diagonals are the same (and not empty).

The method will return `True` if the current player has achieved any of these conditions,
indicating that they have won the game. If no winning condition is met, the method returns `False`.

Returns:
    bool: `True` if the current player has won, otherwise `False`.
"""
def checkWinner(board):
    """Check if the current player has won."""
    # Check rows, columns, and diagonals
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != '':
            return True
        if board[0][i] == board[1][i] == board[2][i] != '':
            return True
    
    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] != '':
        return True
    if board[0][2] == board[1][1] == board[2][0] != '':
        return True

    return False