# You are presented with a map of a kingdom. Empty land on this map is depicted as ‘.’ (without the quotes), and mountains are depicted by ‘#’. This kingdom has factions whose armies are represented by lowercase letters in the map. Two armies of the same letter belong to the same faction. Armies can go up, down, left, and right, but cannot travel through mountains. A region is an area enclosed by mountains. From this it can be deduced that armies cannot travel between different regions. A region is said to be controlled by a faction if it’s the only faction with an army in that region. If there are at least two armies from different factions in a region, then that region is said to be contested. Your task is to determine how many regions each faction controls and how many contested regions there are.
# Input: The first line is the number of test cases T. Each test case will have two numbers N and M, each on their own line given in that order. Following that is N lines of M characters that represent the map.
# Output: For each test case, output one line of the form “Case C:” (without the quotes), where C is the case number (starting from 1). On the following lines, output the factions that appear in the grid in alphabetical order if the faction controls at least one region and how many regions that letter controls. Factions that don’t control any regions should not be in the output. After this, print one last line of the form “contested K” where K is the number of regions that contain at least two distinct letters. See the sample output below for details
import sys
sys.setrecursionlimit(999999999)

def main():
    # read input
    t = int(input())
    output = {}
    for iteration in range(t):
        # read input
        row, col = int(input()), int(input())

        # array to store input string to 2d array
        maps = []

        # array to store if the node is already visited
        visited = [[False for i in range(col)] for j in range(row)]

        # using set to store temp fraction
        tempFraction = set()

        # using tree map to store fraction by alphabetical order
        fraction = {}

        # init data
        for j in range(row):
            maps.append(input())

        Conquer = 0
        for j in range(row):
            for k in range(col):
                # clear temp fraction
                tempFraction.clear()

                # find the fraction
                findAndContest(maps, visited, tempFraction, row, col, j, k)

                # if set fraction > 1 there's a contested region
                if len(tempFraction) > 1:
                    Conquer += 1
                else:
                  for i in tempFraction:
                    if i in fraction:
                        fraction[i] += 1
                    else:
                        fraction[i] = 1
                  
        output[iteration+1] = [fraction, Conquer]

    # print output to text file
    with open('output.txt', 'w') as f:
        for i in range(1, t+1):
            f.write('Case ' + str(i) + ':\n')
            # sort fraction by alphabetical order
            for j in sorted(output[i][0].keys()):
                if output[i][0][j] > 0:
                    f.write(j + ' ' + str(output[i][0][j]) + '\n')
            f.write('contested ' + str(output[i][1]) + '\n')

    # for i in range(t):
    #     print("Case %d:" % (i+1))
    #     # sort fraction by alphabetical order
    #     for j in sorted(output[i+1][0].keys()):
    #         if output[i+1][0][j] > 0:
    #             print(j, output[i+1][0][j])
    #     print("contested %d" % output[i+1][1])


def findAndContest(maps, visited, tempFraction, row, col, x, y):
    # make sure not exceed the limit
    if x < 0 or x >= row:
        return
    if y < 0 or y >= col:
        return

    # make sure not visit before
    if visited[x][y]:
        return

    visited[x][y] = True

    # ignore #
    if maps[x][y] == '#':
        return
    
    # add fraction to the Set tempFraction
    if(maps[x][y] != '.'):
        tempFraction.add(maps[x][y])
    
    # move direction right, down, left, up
    findAndContest(maps, visited, tempFraction, row, col, x+1, y)
    findAndContest(maps, visited, tempFraction, row, col, x-1, y)
    findAndContest(maps, visited, tempFraction, row, col, x, y+1)
    findAndContest(maps, visited, tempFraction, row, col, x, y-1)

    return

if __name__ == "__main__":
    main()