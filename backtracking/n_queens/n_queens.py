arrangement_count = 0
arrangement_counts = []
sizes = [i for i in range(1, 12)]

def isSafe(current_board_state, N, i, j):
    # Same row
    for k in range(N):
        if current_board_state[i][k] == 1:
            return False

    # Same column
    for k in range(N):
        if current_board_state[k][j] == 1:
            return False

    # Same diagonal
    for k in range(N):
        for l in range(N):
            if (k + l == i + j) or (k - l == i - j):
                if current_board_state[k][l] == 1:
                    return False

    return True

def n_queens(current_board_state, N, row):
    if N < 4:
        return False

    if row == N:
        global arrangement_count
        arrangement_count += 1
        arrangement_counts.append(arrangement_count)

        # Uncomment the following lines to print the board configurations
        # for i in range(N):
        #     for j in range(N):
        #         if current_board_state[i][j] == 1:
        #             print("Q", end=" ")
        #         else:
        #             print("-", end=" ")
        #     print()

        # print()
        return True

    for i in range(N):
        if isSafe(current_board_state, N, row, i):
            current_board_state[row][i] = 1
            n_queens(current_board_state, N, row + 1)
            current_board_state[row][i] = 0

    return False


for N in sizes:
    arrangement_count = 0
    arrangement_counts = []
    current_board_state = [[0 for i in range(N)] for j in range(N)]
    n_queens(current_board_state, N, 0)
    print("N = {}, arrangement_count = {}".format(N, arrangement_count))

"""
N = 1, arrangement_count = 0
N = 2, arrangement_count = 0
N = 3, arrangement_count = 0
N = 4, arrangement_count = 2
N = 5, arrangement_count = 10
N = 6, arrangement_count = 4
N = 7, arrangement_count = 40
N = 8, arrangement_count = 92
N = 9, arrangement_count = 352
N = 10, arrangement_count = 724
N = 11, arrangement_count = 2680
"""
