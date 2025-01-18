import random

def generate_maze(rows, cols):
    """Generates a random maze using recursive backtracking."""

    maze = [[1] * cols for _ in range(rows)]  # Initialize maze with walls

    def backtrack(row, col):
        """Recursively creates paths in the maze."""

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # Right, Left, Down, Up
        random.shuffle(directions)

        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc

            # Check if the new cell is within bounds and a wall
            if 0 <= new_row < rows and 0 <= new_col < cols and maze[new_row][new_col] == 1:
                maze[row][col] = 0  # Remove wall between current and new cell
                maze[new_row][new_col] = 0
                backtrack(new_row, new_col)

    # Start from a random cell
    start_row, start_col = random.randint(0, rows - 1), random.randint(0, cols - 1)
    maze[start_row][start_col] = 0  # Make the starting cell a path
    backtrack(start_row, start_col)

    # Ensure start and end points
    maze[0][0] = 0  # Set entrance
    maze[rows - 1][cols - 1] = 0  # Set exit

    return maze


def solve_maze_dfs(maze, row, col):
    """Solves the maze using Depth-First Search."""

    if row == len(maze) - 1 and col == len(maze[0]) - 1:  # Reached the exit
        return True

    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # Right, Left, Down, Up

    for dr, dc in directions:
        new_row, new_col = row + dr, col + dc

        # Check if the new cell is within bounds, a path, and not visited
        if 0 <= new_row < len(maze) and 0 <= new_col < len(maze[0]) and maze[new_row][new_col] == 0:
            maze[new_row][new_col] = 2  # Mark as visited (you can use any value other than 0 or 1)
            if solve_maze_dfs(maze, new_row, new_col):
                return True
            maze[new_row][new_col] = 0  # Backtrack

    return False


def print_maze(maze):
    """Prints the maze in a text-based format."""

    for row in maze:
        print(''.join(['#' if cell == 1 else ' ' for cell in row]))


if __name__ == "__main__":
    rows, cols = 10, 15  # Adjust maze size as needed

    generated_maze = generate_maze(rows, cols)
    print_maze(generated_maze)  # Print the generated maze

    if solve_maze_dfs(generated_maze, 0, 0):
        print("Maze solved!")
        print_maze(generated_maze)  # Print the solved maze
    else:
        print("Maze is unsolvable.")


