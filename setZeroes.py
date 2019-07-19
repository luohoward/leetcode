def setZeroes(self, matrix):
    """
    :type matrix: List[List[int]]
    :rtype: None Do not return anything, modify matrix in-place instead.
    """
    
    xCoords = []
    yCoords = []
    
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == 0:
                xCoords.append(i)
                yCoords.append(j)
                
    for i in range(len(xCoords)):
        for j in range(len(matrix[0])):
            matrix[xCoords[i]][j] = 0
            
    for i in range(len(yCoords)):
        for j in range(len(matrix)):
            matrix[j][yCoords[i]] = 0