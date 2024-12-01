import pandas as pd
import random

# Generate simulated data
data = {
    'Browsing_Time': [random.randint(10, 300) for _ in range(100)],  # Random browsing time in minutes
    'App_Usage': [random.randint(1, 10) for _ in range(100)],       # Number of apps used
    'Flagged_Words': [random.randint(0, 5) for _ in range(100)],    # Flagged words in keylogs
    'Risky_Behavior': [random.choice([0, 1]) for _ in range(100)]   # 1 = risky, 0 = safe
}

# Create DataFrame
df = pd.DataFrame(data)

# Save to CSV
df.to_csv('online_behavior_data.csv', index=False)
print("Simulated dataset saved as 'online_behavior_data.csv'")
