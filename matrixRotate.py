def rotate(self, matrix):
    """
    :type matrix: List[List[int]]
    :rtype: None Do not return anything, modify matrix in-place instead.
    """
    
    for i in range(len(matrix) / 2):
        for j in range(i, len(matrix) - i - 1):
            temp = matrix[len(matrix) - 1 - j][i]
            
            matrix[len(matrix) - 1 - j][i] = matrix[len(matrix) - 1 - i][len(matrix) - 1 - j]
            matrix[len(matrix) - 1 - i][len(matrix) - 1 - j] = matrix[j][len(matrix) - 1 - i]
            matrix[j][len(matrix) - 1 - i] = matrix[i][j]
            matrix[i][j] = temp
                