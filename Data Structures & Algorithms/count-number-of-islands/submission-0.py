class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        rows,cols = len(grid),len(grid[0])
        visited = set()
        q = deque()
        def bfs():
            directions = ((0,1),(1,0),(-1,0),(0,-1))

            while q:
                hold =q.popleft()
                if grid[hold[0]][hold[1]] == "1":
                    for r,c in directions:
                        row,col = hold[0]+r, hold[1]+c
                        if (row in range(rows) and
                            col in range(cols) and
                            grid[row][col]=="1" and 
                            (row,col) not in visited):
                            visited.add((row,col))
                            q.append((row,col))



        for i in range(rows):
            for j in range(cols):
                if (i,j) not in visited and grid[i][j]=="1":
                    visited.add((i,j))
                    q.append((i,j))
                    bfs()
                    islands+=1
        return islands
