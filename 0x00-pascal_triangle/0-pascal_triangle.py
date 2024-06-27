#!/usr/bin/python3

# Function to generate Pascal's Triangle
def pascal_triangle(n):
    # Initialize an empty list to store the triangle
    matrix = []

    # If n is less than or equal to 0, return an empty list
    if n <= 0:
        return matrix

    # The first row of Pascal's Triangle is always [1]
    matrix = [[1]]

    # Generate the remaining rows
    for i in range(1, n):
        # Initialize a temporary list to store the current row
        temp = [1]

        # Calculate the values for the current row
        for j in range(len(matrix[i - 1]) - 1):
            temp.append(matrix[i - 1][j] + matrix[i - 1][j + 1])

        # Append 1 to the end of the current row
        temp.append(1)

        # Append the current row to the triangle
        matrix.append(temp)

    # Return the generated Pascal's Triangle
    return matrix
