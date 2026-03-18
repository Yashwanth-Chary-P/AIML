import math

# Minimax function
def minimax(curDepth, nodeIndex, maxTurn, scores, targetDepth):
    
    # Base case: If we reached leaf node
    if curDepth == targetDepth:
        return scores[nodeIndex]

    # If it's MAX player's turn
    if maxTurn:
        return max(
            minimax(curDepth + 1, nodeIndex * 2, False, scores, targetDepth),
            minimax(curDepth + 1, nodeIndex * 2 + 1, False, scores, targetDepth)
        )

    # If it's MIN player's turn
    else:
        return min(
            minimax(curDepth + 1, nodeIndex * 2, True, scores, targetDepth),
            minimax(curDepth + 1, nodeIndex * 2 + 1, True, scores, targetDepth)
        )


# Driver Code
if __name__ == "__main__":
    
    # Leaf node values
    scores = [3, 5, 2, 9, 12, 5, 23, 23]

    # Calculate tree depth
    treeDepth = int(math.log(len(scores), 2))

    # Call minimax
    optimal_value = minimax(0, 0, True, scores, treeDepth)

    print("The optimal value is:", optimal_value)