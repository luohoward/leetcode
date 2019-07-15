# does not completely pass in the case when the data is too large

def pacificAtlantic(self, matrix):
    """
    :type matrix: List[List[int]]
    :rtype: List[List[int]]
    """
    positions = []
    
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if self.bfs(matrix, i, j):
                positions.append([i, j])
                
    return positions
    
def bfs(self, matrix, i, j):
    seen = set()
    
    seenPacific = False
    seenAtlantic = False
    
    queue = [[i, j]]
    
    while len(queue) != 0:
        m, n = queue.pop()
        
        if m - 1 < 0 or n - 1 < 0:
            seenPacific = True
            
        if m + 1 >= len(matrix) or n + 1 >= len(matrix[0]):
            seenAtlantic = True
            
        if m >= 0 and m < len(matrix) and n >= 0 and n < len(matrix[0]) and (m, n) not in seen:
            seen.add((m, n))
            
            if m - 1 >= 0 and matrix[m][n] >= matrix[m - 1][n]:
                queue.append([m - 1, n])

            if n - 1 >= 0 and matrix[m][n] >= matrix[m][n - 1]:
                queue.append([m, n - 1])
                
            if m + 1 < len(matrix) and matrix[m][n] >= matrix[m + 1][n]:
                queue.append([m + 1, n])
                
            if n + 1 < len(matrix[0]) and matrix[m][n] >= matrix[m][n + 1]:
                queue.append([m, n + 1])

            
        
    return seenPacific and seenAtlantic