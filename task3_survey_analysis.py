import pandas as pd

# Sample Survey Responses (5 Employees)
data = {
    "Work Environment": [4, 5, 3, 4, 5],
    "Salary Satisfaction": [3, 4, 3, 4, 2],
    "Management Support": [5, 4, 4, 3, 5],
    "Work-Life Balance": [4, 3, 4, 5, 4]
}

df = pd.DataFrame(data)

# Calculate Average
average_scores = df.mean()

print("Survey Analysis Summary:")
print(average_scores)

# Save to CSV
df.to_csv("Employee_Survey_Responses.csv", index=False)
