import numpy as np
from sklearn.preprocessing import PolynomialFeatures

# Input data (Hours Studied)
X = np.array([[1],
              [2],
              [3],
              [4],
              [5]])

# Output data (Marks)
y = np.array([2, 4, 6, 8, 10])

# Polynomial Regression Function
def polynomial_regression(X, y, degree):

    # Step 1: Generate polynomial features
    poly = PolynomialFeatures(degree)
    X_poly = poly.fit_transform(X)

    # Step 2: Apply Least Squares (Normal Equation)
    theta = np.linalg.inv(X_poly.T.dot(X_poly)).dot(X_poly.T).dot(y)
 
    return theta

# Degree of polynomial
degree = 2

# Train model
theta = polynomial_regression(X, y, degree)

print("Theta:", theta)

# Display equation
print("\nPolynomial Equation:")
print(f"y = {theta[0]:.4f} + {theta[1]:.4f}x + {theta[2]:.4f}x²")