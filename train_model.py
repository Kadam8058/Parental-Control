import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, classification_report
import joblib

# Generate or load your dataset (replace this with your real dataset later)
data = {
    'Browsing_Time': [120, 45, 300, 90, 200],
    'App_Usage': [3, 1, 5, 2, 4],
    'Flagged_Words': [2, 0, 4, 1, 5],
    'Risky_Behavior': [1, 0, 1, 0, 1]
}

# Create DataFrame
df = pd.DataFrame(data)

# Features (X) and Target (y)
X = df[['Browsing_Time', 'App_Usage', 'Flagged_Words']]
y = df['Risky_Behavior']

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Decision Tree Model
dt_model = DecisionTreeClassifier()
dt_model.fit(X_train, y_train)
dt_preds = dt_model.predict(X_test)

# SVM Model
svm_model = SVC()
svm_model.fit(X_train, y_train)
svm_preds = svm_model.predict(X_test)

# Save models
joblib.dump(dt_model, 'decision_tree_model.pkl')
joblib.dump(svm_model, 'svm_model.pkl')

# Print model accuracy
print("Decision Tree Accuracy:", accuracy_score(y_test, dt_preds))
print(classification_report(y_test, dt_preds))

print("SVM Accuracy:", accuracy_score(y_test, svm_preds))
print(classification_report(y_test, svm_preds))
