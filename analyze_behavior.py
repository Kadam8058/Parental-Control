import pandas as pd
import joblib

# Load models
dt_model = joblib.load('decision_tree_model.pkl')
svm_model = joblib.load('svm_model.pkl')

# Example new data
new_data = pd.DataFrame({
    'Browsing_Time': [180],
    'App_Usage': [4],
    'Flagged_Words': [3]
})

# Predictions
dt_prediction = dt_model.predict(new_data)
svm_prediction = svm_model.predict(new_data)

print("Decision Tree Prediction:", "Risky" if dt_prediction[0] == 1 else "Safe")
print("SVM Prediction:", "Risky" if svm_prediction[0] == 1 else "Safe")
