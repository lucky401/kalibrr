class GFG:
    
    def __init__(self):
        self.R = None
        self.C = None
        self.dir = [[-1, 0], [1, 0], [1, 1], 
                    [1, -1], [-1, -1], [-1, 1],
                    [0, 1], [0, -1]]
                    
    # This function searches in all 8-direction 
    # from point(row, col) in grid[][]
    def search2D(self, grid, row, col, word):
        
        # If first character of word doesn't match 
        # with the given starting point in grid.
        if grid[row][col] != word[0]:
            return 0
            
        # Search word in all 8 directions 
        # starting from (row, col)
        total = 0
        for x, y in self.dir:
            
            # Initialize starting point 
            # for current direction
            rd, cd = row + x, col + y
            flag = True
            
            # First character is already checked, 
            # match remaining characters
            for k in range(1, len(word)):
                
                # If out of bound or not matched, break
                if (0 <= rd <self.R and 
                    0 <= cd < self.C and 
                    word[k] == grid[rd][cd]):
                    
                    # Moving in particular direction
                    rd += x
                    cd += y
                else:
                    flag = False
                    break
            
            # If all character matched, then 
            # value of flag must be false        
            if flag:
                total += 1
        
        return total
    
    # Searches given word in a given matrix
    # in all 8 directions    
    def patternSearch(self, grid, word):
        
        # Rows and columns in given grid
        self.R = len(grid)
        self.C = len(grid[0])
        
        # Consider every point as starting point 
        # and search given word
        total = 0
        for row in range(self.R):
            for col in range(self.C):
                tempTotalFound = self.search2D(grid, row, col, word)
                if tempTotalFound:
                    total += tempTotalFound
        return total


T = int(input())
output = []
for i in range(T):
    N, M = int(input()), int(input())
    grid = []
    for j in range(N):
        grid.append(input())
    word = input()
    gfg = GFG()
    output.append(gfg.patternSearch(grid, word))

for i in range(len(output)):
    print("Case %d: %d" % (i+1, output[i]))