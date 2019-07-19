def spiralOrder(self, matrix):
    """
    :type matrix: List[List[int]]
    :rtype: List[int]
    """
    
    if not matrix:
        return []
    
    row, col = len(matrix), len(matrix[0])
    seen = [[False for j in range(col)] for i in range(row)]
    
    spiralList = []
    
    r = c = direction = 0
    
    rowDir = [0, 1, 0, -1]
    colDir = [1, 0, -1, 0]
    
    
    for _ in range(row * col):
        spiralList.append(matrix[r][c])
        seen[r][c] = True
        
        nextRow = r + rowDir[direction]
        nextCol = c + colDir[direction]
        
        if 0 <= nextRow < row and 0 <= nextCol < col and not seen[nextRow][nextCol]:
            r, c = nextRow, nextCol
    
        else:
            direction = (direction + 1) % 4
            r, c = r + rowDir[direction], c + colDir[direction]
            
    return spiralList