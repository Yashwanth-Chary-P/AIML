MAX, MIN = 1000, -1000

# Alpha-Beta Minimax function
def minimax(depth, nodeIndex, maximizingPlayer, values, alpha, beta):

    # Base case: leaf node
    if depth == 3:
        return values[nodeIndex]

    # MAX player
    if maximizingPlayer:
        best = MIN

        for i in range(2):
            val = minimax(depth + 1, nodeIndex * 2 + i,
                          False, values, alpha, beta)

            best = max(best, val)
            alpha = max(alpha, best)

            # Pruning condition
            if beta <= alpha:
                break

        return best

    # MIN player
    else:
        best = MAX

        for i in range(2):
            val = minimax(depth + 1, nodeIndex * 2 + i,
                          True, values, alpha, beta)

            best = min(best, val)
            beta = min(beta, best)

            # Pruning condition
            if beta <= alpha:
                break

        return best


# Driver Code
if __name__ == "__main__":

    values = [3, 5, 6, 9, 1, 2, 0, -1]

    print("The optimal value is:",
          minimax(0, 0, True, values, MIN, MAX))