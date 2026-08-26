class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS = len(heights)
        COLS = len(heights[0])
        pacific = set()
        atlantic = set()

        def dfs(r,c,visit,prev):
            if ((r,c) in visit or r < 0 or c < 0 or r == ROWS or c == COLS or heights[r][c] < prev):
                return
            visit.add((r,c))
            dfs(r+1,c,visit,heights[r][c])
            dfs(r-1,c,visit,heights[r][c])
            dfs(r,c+1,visit,heights[r][c])
            dfs(r,c-1,visit,heights[r][c])

        for c in range(COLS):
            dfs(0,c,pacific,heights[0][c])
            dfs(ROWS-1,c,atlantic,heights[ROWS-1][c])
        
        for r in range(ROWS):
            dfs(r,0,pacific,heights[r][0])
            dfs(r,COLS-1,atlantic,heights[r][COLS-1])
        res = []
        for c in range(COLS):
            for r in range(ROWS):
                if (r,c) in pacific and (r,c) in atlantic:
                    res.append([r,c])
        
        return res