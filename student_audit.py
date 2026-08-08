import numpy as np
import pandas as pd

# Set a random seed so our data is identical every time we run it
np.random.seed(42)

n_rows = 1000

# Generate synthetic data
student_ids = np.arange(1001, 1001 + n_rows)
study_hours = np.random.normal(loc=15, scale=5, size=n_rows)  # Weekly hours
sleep_hours = np.random.normal(loc=7, scale=1.5, size=n_rows)  # Daily hours
screen_time = np.random.normal(loc=5, scale=2, size=n_rows)   # Daily hours
cgpa = np.random.normal(loc=3.2, scale=0.4, size=n_rows)      # CGPA out of 4.0

# Create DataFrame
df = pd.DataFrame({
    'student_id': student_ids,
    'study_hours': study_hours,
    'sleep_hours': sleep_hours,
    'screen_time': screen_time,
    'cgpa': cgpa,
    'grade_category': np.random.choice(['A', 'B', 'C', ' D ', 'b', 'A'], size=n_rows)
})

# --- INJECTING REAL-WORLD MESSINESS ---
# 1. Inject missing values (NaN) randomly into study hours and sleep
df.loc[np.random.choice(n_rows, 50, replace=False), 'study_hours'] = np.nan
df.loc[np.random.choice(n_rows, 30, replace=False), 'sleep_hours'] = np.nan

# 2. Inject duplicate rows
df = pd.concat([df, df.sample(20, random_state=42)], ignore_index=True)

# 3. Inject physical impossibilities (Outliers)
df.loc[10, 'sleep_hours'] = 26.0  # Nobody sleeps 26 hours a day
df.loc[15, 'cgpa'] = 5.2          # CGPA cannot exceed 4.0

# Save to CSV
df.to_csv('messy_student_data.csv', index=False)
print("Messy dataset generated and saved as 'messy_student_data.csv'!")
print(f"Total rows in raw file: {len(df)}")

