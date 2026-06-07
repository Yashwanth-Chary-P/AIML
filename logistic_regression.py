import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, precision_score, recall_score

# Step 1: Load dataset from CSV file
data = pd.read_csv('StudentsPerformance.csv')

# Step 2: Clean column names (remove spaces, lowercase)
data.columns = data.columns.str.strip().str.lower().str.replace(' ', '_')

# Step 3: Create target column (1 = pass, 0 = fail)
data['target'] = (data['math_score'] >= 50).astype(int)

# Step 4: Separate features (X) and target (y)
X = data.drop(['target', 'math_score'], axis=1)
y = data['target']

# Step 5: Convert categorical data into numerical (encoding)
X = pd.get_dummies(X, drop_first=True)

# Step 6: Handle missing values (if any)
X = X.fillna(X.mean())

# Step 7: Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Step 8: Normalize/scale the data
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Step 9: Create Logistic Regression model
model = LogisticRegression(max_iter=1000)

# Step 10: Train the model
model.fit(X_train, y_train)

# Step 11: Predict on test data
y_pred = model.predict(X_test)

# Step 12: Evaluate performance
accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred, zero_division=0)
recall = recall_score(y_test, y_pred, zero_division=0)

# Step 13: Print results
print("Accuracy:", round(accuracy, 2))
print("Precision:", round(precision, 2))
print("Recall:", round(recall, 2))