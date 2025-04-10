import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#data
df = pd.read_csv("C:\\Users\\EKANSH\\Downloads\\Allied_Cultural_Activities.csv")
print(df)

#column names
df.columns = df.columns.str.strip()

#Handle missing or bad data
df['Released Amount'] = pd.to_numeric(df['Released Amount']).fillna(0)

#Summary: total assistance per state
state_summary = df.groupby('State')['Released Amount'].sum()

#Print basic stats
print("Total Assistance by State:")
print(state_summary)

#Plot: Total assistance by state
plt.figure(figsize=(10, 5))
state_summary.plot(kind='bar', color='skyblue')
plt.title('Financial Assistance by State')
plt.xlabel('State')
plt.ylabel('Released Amount (INR)')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.grid(axis='y', linestyle='--', alpha=0.5)
plt.show()

#Optional: Find top 20 states
top_states = state_summary.head(20)
print("\nTop 20 States Receiving Financial Assistance:")
print(top_states)

