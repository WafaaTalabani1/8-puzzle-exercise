import random
import heapq
import numpy as np


def get_random_state():
    # Create a NumPy array of integers from 1 to 9, shuffled randomly
    tiles = np.random.permutation(9) + 1
    # Replace the last element (9) with 0 to represent the empty tile
    tiles[-1] = 0
    # Reshape the array into a 3x3 grid
    initial_state = tiles.reshape((3, 3))
    return initial_state


board = get_random_state()
print(board)


def manhattan_distance(initial_state):
    distance = 0
    for i in range(len(initial_state)):
        for j in range(len(initial_state[0])):
            # Calculate the target position for the current tile
            target_i, target_j = get_target_position(initial_state[i][j])
            # Calculate the horizontal and vertical distances
            distance += abs(i - target_i) + abs(j - target_j)
    return distance


def get_target_position(tile):
    # Determine the target row and column for the given tile value
    target_i = (tile - 1) // 3
    target_j = (tile - 1) % 3
    return target_i, target_j


def solve_8puzzle(initial_state):
    # Create a priority queue to store the nodes to be explored
    queue = []
    # Add the initial board configuration to the queue
    heapq.heappush(queue, (manhattan_distance(initial_state), initial_state))
    # Create a set to store the board configurations that have already been visited
    visited = set()

    while queue:
        # Get the board configuration with the lowest Manhattan distance from the queue
        distance, current_state = heapq.heappop(queue)
        # Check if the current board is the goal state
        if current_state == [[1, 2, 3], [4, 5, 6], [7, 8, 0]]:
            return current_state
        # Add the current board to the visited set
        visited.add(tuple(map(tuple, current_state)))
        # Find the position of the empty tile (represented by 0)
        i, j = get_empty_tile_position(current_state)
        # Generate the next possible board configurations by moving the empty tile
        next_boards = get_next_states(current_state, i, j)
        for next_board in next_boards:
            # Check if the next board has already been visited
            if tuple(map(tuple, next_board)) not in visited:
                # Add the next board to the queue with the updated Manhattan distance
                heapq.heappush(queue, (manhattan_distance(next_board), next_board))


def get_empty_tile_position(current_state):
    # Find the position of the empty tile (represented by 0)
    for i in range(len(current_state)):
        for j in range(len(current_state[0])):
            if current_state[i][j] == 0:
                return i, j


def get_next_states(state, i, j):
    # Generate the next possible state configurations by moving the empty tile
    next_boards = []
    if i > 0:
        # Move the empty tile up
        next_board = [row[:] for row in state]
        next_board[i][j], next_board[i - 1][j] = next_board[i - 1][j], next_board[i][j]
        next_boards.append(next_board)
    if i < 2:
        # Move the empty tile down
        next_board = [row[:] for row in state]
        next_board[i][j], next_board[i + 1][j] = next_board[i + 1][j], next_board[i][j]
        next_boards.append(next_board)
    if j > 0:
        # Move the empty tile left
        next_board = [row[:] for row in state]
        next_board[i][j], next_board[i][j - 1] = next_board[i][j - 1], next_board[i][j]
        next_boards.append(next_board)
    if j < 2:
        # Move the empty tile right
        next_board = [row[:] for row in state]
        next_board[i][j], next_board[i][j + 1] = next_board[i][j + 1], next_board[i][j]
        next_boards.append(next_board)
    return next_boards
