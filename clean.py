import pandas as pd

# 1. Load the raw messy dataset
df = pd.read_csv('messy_student_data.csv')
print(f"--- 1. INITIAL LOAD ---")
print(f"Total rows: {len(df)}")
print(df.info())

# 2. TODO: Handle Duplicates
# Hint: Look up how to drop duplicate rows in a DataFrame

df = df.drop_duplicates()


# 3. TODO: Handle Text Inconsistency in 'grade_category'
# Hint: You need to access string methods using .str, strip whitespace, and make everything uppercase.
df['grade_category'] = df['grade_category'].str.strip().str.upper()

# print(df['grade_category'])

# 4. TODO: Handle Outliers (Logical Impossibilities)
# Hint: Filter out rows where sleep_hours > 24 or cgpa > 4.0 using boolean masking (& operator)
valid_mask = (df['sleep_hours'] <= 24 ) & (df['cgpa'] <= 4.0 )
df = df.loc[valid_mask]


# 5. TODO: Handle Missing Values (NaN)
# Hint: Check .isnull().sum(), then use .fillna() with the median of each column for study_hours and sleep_hours.
df['study_hours'] = df['study_hours'].fillna(df['study_hours'].median())
df['sleep_hours'] = df['sleep_hours'].fillna(df['sleep_hours'].median())
print(df.info())
# Save your pristine, cleaned dataset
df.to_csv('cleaned_student_data.csv', index=False)
print("\nData cleaning complete! Saved as 'cleaned_student_data.csv'.")