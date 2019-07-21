def exist(self, board, word):
    """
    :type board: List[List[str]]
    :type word: str
    :rtype: bool
    """
    seen = [[False for i in range(len(board[0]))] for j in range(len(board))]
    
    for i in range(len(board)):
        for j in range(len(board[i])):
            if self.dfs(board, word, i, j, 0, seen):
                return True
            
    return False

def dfs(self, board, word, i, j, index, seen):
    if i < 0 or j < 0 or i > len(board) - 1 or j > len(board[0]) - 1:
        return False
    
    elif seen[i][j]:
        return False
    
    elif board[i][j] != word[index]:
        return False
    
    elif board[i][j] == word[index] and index == len(word) - 1:
        return True
    
    else:
        seen[i][j] = True
        
        valid = self.dfs(board, word, i + 1, j, index + 1, seen) or \
            self.dfs(board, word, i - 1, j, index + 1, seen) or \
            self.dfs(board, word, i, j - 1, index + 1, seen) or \
            self.dfs(board, word, i, j + 1, index + 1, seen)
            
        seen[i][j] = False
        
        return valid