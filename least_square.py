import numpy as np

# Input data
X = np.array([
    [1, 1],
    [1, 2],
    [1, 3],
    [1, 4],
    [1, 5]
])

# Output values
y = np.array([3, 5, 7, 9, 11])


# Least Squares Function
def least_squares(X, y):

    # Step 1: Transpose of X
    X_transpose = X.T

    # Step 2: Multiply Xᵀ and X
    XTX = X_transpose.dot(X)

    # Step 3: Find inverse of (XᵀX)
    XTX_inv = np.linalg.inv(XTX)

    # Step 4: Multiply Xᵀ and y
    XTy = X_transpose.dot(y)

    # Step 5: Final formula
    theta = XTX_inv.dot(XTy)

    return theta


# Train model
theta = least_squares(X, y)

print("Least Squares Theta:", theta)