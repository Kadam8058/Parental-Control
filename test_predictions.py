import pandas as pd
import joblib

# Load trained models
dt_model = joblib.load('decision_tree_model.pkl')
svm_model = joblib.load('svm_model.pkl')

# Generate random test data
test_data = pd.DataFrame({
    'Browsing_Time': [120],  # Replace with actual or random values
    'App_Usage': [5],
    'Flagged_Words': [2]
})

# Make predictions
dt_prediction = dt_model.predict(test_data)
svm_prediction = svm_model.predict(test_data)

print("Decision Tree Prediction:", "Risky" if dt_prediction[0] == 1 else "Safe")
print("SVM Prediction:", "Risky" if svm_prediction[0] == 1 else "Safe")
