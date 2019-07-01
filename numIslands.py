def numIslands(self, grid):
    """
    :type grid: List[List[str]]
    :rtype: int
    """
    seen = [[False for j in range(len(grid[i]))] for i in range(len(grid))]
    count = 0
    
    
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == '1' and not seen[i][j]:
                queue = [(i, j)]
                while len(queue) != 0:
                    m, n = queue.pop()
                    
                    if m < 0 or m > len(grid) - 1 or n < 0 or n > len(grid[i]) - 1:
                        continue

                    if seen[m][n] or grid[m][n] == '0':
                        continue

                    seen[m][n] = True
                    queue.insert(0, (m + 1, n))
                    queue.insert(0, (m - 1, n))
                    queue.insert(0, (m, n + 1))
                    queue.insert(0, (m, n - 1))
                    
                count += 1
                
    return count