from os import system, name
from time import sleep

def gameoflife(x_cycle, origin):

    if isinstance(x_cycle, int):

        m2 = [[i for i in row] for row in origin]

        output2 = [[0] * len(m2[0]) for i in range(len(m2))]

        loopNum = int(x_cycle)
        count = 1

        rowCount = len(m2)
        colCount = len(m2[0])

        while count < loopNum + 1:
            for x in range(rowCount):
                for y in range(colCount):
                    if rowCount > 1:  # more than one sublist
                        if x == 0:  # first row
                            if y == 0:  # first col
                                nexy = m2[x][y+1] + m2[x+1][y] \
                                    + m2[x+1][y+1]
                            elif y == colCount - 1:  # last column
                                nexy = m2[x][y-1] + m2[x+1][y-1] \
                                    + m2[x+1][y]
                            else:  # other column
                                nexy = m2[x][y-1] + m2[x+1][y-1] \
                                    + m2[x+1][y] + m2[x+1][y+1] \
                                    + m2[x][y+1]
                        elif x == rowCount-1:  # last row
                            if y == 0:  # first col
                                nexy = m2[x-1][y] + m2[x-1][y+1] \
                                    + m2[x][y+1]
                            elif y == colCount - 1:  # last column
                                nexy = m2[x][y-1] + m2[x-1][y-1] \
                                    + m2[x-1][y]
                            else:  # other column
                                nexy = m2[x][y-1] + m2[x-1][y-1] \
                                    + m2[x-1][y] + m2[x-1][y+1] \
                                    + m2[x][y+1]
                        else:  # other rows
                            if y == 0:  # first col
                                nexy = m2[x-1][y] + m2[x-1][y+1] \
                                    + m2[x][y+1] + m2[x+1][y+1] \
                                    + m2[x+1][y]
                            elif y == colCount - 1:  # last column
                                nexy = m2[x-1][y] + m2[x-1][y-1] \
                                    + m2[x][y-1] + m2[x+1][y-1] \
                                    + m2[x+1][y]
                            else:  # other column
                                nexy = m2[x][y-1] + m2[x-1][y-1] \
                                    + m2[x-1][y] + m2[x-1][y+1] \
                                    + m2[x][y+1] + m2[x+1][y+1] \
                                    + m2[x+1][y] + m2[x+1][y-1]
                    else:  # only one sublist
                        if y == 0:  # first col
                            nexy = m2[x][y+1]
                        elif y == colCount - 1:  # last column
                            nexy = m2[x][y-1]
                        else:  # other column
                            nexy = m2[x][y-1] + m2[x][y+1]

                    if (m2[x][y] == 1) and (nexy == 2 or nexy == 3):
                        output2[x][y] = 1
                    elif (m2[x][y] == 0) and (nexy == 3):
                        output2[x][y] = 1
                    else:
                        output2[x][y] = 0

            m2 = [[i for i in row] for row in output2]
            clear_screen()
            print_grid(m2)
            print("cycle ", count)
            count = count + 1
        return m2
    else:
        return "Invalid iteration!"


def print_grid(grid):
    for i in grid:
        for j in i:
            if j == 1:
                print("\033[42m 1 \033[0m", end="")
            else:
                print(" 0 ", end="")
        print()


def clear_screen():
    sleep(1)
    # for windows
    if name == 'nt':
        _ = system('cls')
 
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

# ============================================================================
# 
# ============================================================================
def test_pulsar():
    pulsar = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
    
    gameoflife(10, pulsar)

def test_pentadecathlon():
    pentadecathlon = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0],
        [0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
    
    gameoflife(15, pentadecathlon)

if __name__ == "__main__":
    test_pulsar()
    # test_pentadecathlon()