"""1. Initialise the maze and set number of rows and cols"""
wall_symbol = '#'
person_symbol = 'k'
free_space = ' '
number = int(input())
maze = []
for _ in range(number):
    ll = list(input())
    maze.append(ll)

row_number = len(maze)
col_number = len(maze[0])

"""2. Check if you are already at the maze exit"""

start_at_exit = False
for i in range(row_number):
    for j in range(col_number):
        if maze[i][j] == person_symbol:
            if i == 0 or i == row_number - 1 or j == 0 or j == col_number - 1:
                start_at_exit = True
                break

"""3. Fill all dead ends - the matrix should be larger thant 2x2"""


def fill_dead_ends(matrix):
    cycle_changes = 0
    rows = len(matrix)
    cols = len(matrix[0])

    for x in range(rows):
        for y in range(cols):
            if matrix[x][y] == wall_symbol:
                continue
            elif matrix[x][y] == person_symbol:
                continue
            else:
                if x == 0 and y == 0:
                    if matrix[x + 1][y] == wall_symbol or matrix[x][y + 1] == wall_symbol:  # check if we are at upper left corner
                        matrix[x][y] = wall_symbol
                        cycle_changes += 1
                elif x == 0 and y == cols - 1:
                    if matrix[x + 1][y] == wall_symbol or matrix[x][y - 1] == wall_symbol:  # check if we are at upper right corner
                        matrix[x][y] = wall_symbol
                        cycle_changes += 1
                elif x == rows - 1 and y == 0:   # check if we are at lower left corner
                    if matrix[x - 1][y] == wall_symbol or matrix[x][y + 1] == wall_symbol:
                        matrix[x][y] = wall_symbol
                        cycle_changes += 1
                elif x == rows - 1 and y == cols - 1:   # check if we are at lower right corner
                    if matrix[x - 1][y] == wall_symbol or matrix[x][y - 1] == wall_symbol:
                        matrix[x][y] = wall_symbol
                        cycle_changes += 1
                else:
                    wall_number = 0
                    if x == 0:  # check if we are at first row (corners already excluded)
                        if matrix[x][y - 1] == wall_symbol:
                            wall_number += 1
                        if matrix[x][y + 1] == wall_symbol:
                            wall_number += 1
                        if matrix[x + 1][y] == wall_symbol:
                            wall_number += 1
                        if wall_number > 1:
                            matrix[x][y] = wall_symbol
                            cycle_changes += 1
                    elif x == rows - 1: # check if we are at last row (corners already excluded)
                        if matrix[x][y - 1] == wall_symbol:
                            wall_number += 1
                        if matrix[x][y + 1] == wall_symbol:
                            wall_number += 1
                        if matrix[x - 1][y] == wall_symbol:
                            wall_number += 1
                        if wall_number > 1:
                            matrix[x][y] = wall_symbol
                            cycle_changes += 1
                    elif y == 0:  # check if we are at first col (corners already excluded)
                        if matrix[x][y + 1] == wall_symbol:
                            wall_number += 1
                        if matrix[x - 1][y] == wall_symbol:
                            wall_number += 1
                        if matrix[x + 1][y] == wall_symbol:
                            wall_number += 1
                        if wall_number > 1:
                            matrix[x][y] = wall_symbol
                            cycle_changes += 1
                    elif y == cols - 1:  # check if we are at last col (corners already excluded)
                        if matrix[x][y - 1] == wall_symbol:
                            wall_number += 1
                        if matrix[x - 1][y] == wall_symbol:
                            wall_number += 1
                        if matrix[x + 1][y] == wall_symbol:
                            wall_number += 1
                        if wall_number > 1:
                            matrix[x][y] = wall_symbol
                            cycle_changes += 1
                    else:   # we are not in the first/last cols/rows
                        if matrix[x - 1][y] == wall_symbol:
                            wall_number += 1
                        if matrix[x + 1][y] == wall_symbol:
                            wall_number += 1
                        if matrix[x][y - 1] == wall_symbol:
                            wall_number += 1
                        if matrix[x][y + 1] == wall_symbol:
                            wall_number += 1
                        if wall_number > 3:
                            matrix[x][y] = wall_symbol
                            cycle_changes += 1

    if cycle_changes != 0:
        fill_dead_ends(matrix)

    return matrix


filled_maze = fill_dead_ends(maze)


def proper_printing(nested_list):
    for i in range(len(nested_list)):
        separator = '\n'
        print(separator)
        for j in range(len(nested_list[0])):
            print(nested_list[i][j], end=' ')


print(proper_printing(maze))
print(proper_printing(filled_maze))
