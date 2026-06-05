import numpy as np

# Sample dataset
# X = input feature matrix
X = np.array([
    [1, 1],
    [1, 2],
    [1, 3],
    [1, 4],
    [1, 5]
])

# Target values
y = np.array([3, 5, 7, 9, 11])

# Gradient Descent Function
def gradient_descent(X, y, alpha=0.01, iterations=100):

    m, n = X.shape          # m = number of samples, n = features

    # Initialize parameters (weights)
    theta = np.zeros(n)

    # Perform Gradient Descent
    for i in range(iterations):

        # Predicted values
        predictions = X.dot(theta)

        # Error
        errors = predictions - y

        # Gradient calculation
        gradient = (1 / m) * X.T.dot(errors)

        # Update weights
        theta = theta - alpha * gradient

    return theta


# Call Gradient Descent
theta_gd = gradient_descent(X, y)

print("Gradient Descent Theta:", theta_gd)