#!/usr/bin/python3
"""Island Perimeter Module"""


def island_perimeter(grid):
    """returns the perimeter of the island described in grid"""
    if not grid:
        return 0

    # Determine the number of rows and columns in the grid
    rows = len(grid)
    cols = len(grid[0])
    perimeter = 0

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                perimeter += 4
                if j < cols - 1 and grid[i][j + 1] == 1:
                    perimeter -= 2
                if i < rows - 1 and grid[i + 1][j] == 1:
                    perimeter -= 2

    return perimeter
