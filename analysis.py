# import pandas as pd
# import matplotlib.pyplot as plt
# import seaborn as sns

# # 1. Load data
# df = pd.read_csv('cleaned_student_data.csv')
# # print(df['study_hours'].max())
# # 2. Set the visual style using Seaborn
# sns.set_theme(style="whitegrid")

# # --- PLOT 1: Histogram for Study Hours ---
# plt.figure(figsize=(8, 5))
# # data = DATAF FRAME x = to the thing on x-axis and kde=smoothline on the bars bins  
# sns.histplot(data=df,x='study_hours' ,kde=True, color='blue', bins=30)
# plt.title('Distribution of Student Study Hours')
# plt.xlabel('Weekly Study Hours')
# plt.ylabel('Number of Students')
# plt.show()  # <--- You MUST close this popup window for the script to continue to Plot 2!

# # # --- PLOT 2: Scatter Plot for Screen Time vs CGPA ---
# # plt.figure(figsize=(8, 5))
# # sns.scatterplot(data=df, x='screen_time', y='cgpa', color='blue')
# # plt.title('Screen Time vs CGPA')
# # plt.xlabel('Screen Time')
# # plt.ylabel('CGPA')
# # plt.show()

# # # Catagorical graph study hour vs Grade catagory 
# # # Figure Size 1st Parameter WIDTH 2nd HEIGHT
# # plt.figure(figsize=(8, 5))
# # # violinplot graph that shows more width = more students 
# # # 1st DataFrame 2nd x like what on x-axis 3rd para what on y-axis 
# # # violinplot boxplot scatterplot histplot  
# # sns.violinplot(data=df,x='grade_category',y='study_hours')
# # # Settings title xlabel and ylabel plt.show() to run the graph like make the graph
# # plt.title("STUDY HOUR VS GRADE")
# # plt.xlabel("GRADE ")
# # plt.ylabel("STUDY HOURS/PER WEEK")
# # plt.show()

import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("cleaned_student_data.csv")
correlation_matrix = df.corr(numeric_only=True)

plt.figure(figsize=(5,4))

sns.heatmap(data=correlation_matrix,annot=True,cmap='coolwarm')
plt.title("THE HEAT GRAPH")
plt.tight_layout()
plt.show()
# correlation_matrix = df.corr(numeric_only=True)

# plt.figure(figsize=(5,4))

# sns.heatmap(data=correlation_matrix,cmap='coolwarm')
# plt.title("THE HEAT GRAPH")
# plt.tight_layout()
# plt.show()

# 222222
sns.set_theme(style="whitegrid")

# 1. Open a fresh canvas
plt.figure(figsize=(8, 5))

# 2. Draw the count plot
# 'x' is the group column you want to count!
sns.countplot(data=df, x='grade_category', palette='Set2')

# 3. Add titles and labels
plt.title("Number of Students in Each Grade Category")
plt.xlabel("Grade Category")
plt.ylabel("Number of Students")

# 4. Fit margins and show
plt.tight_layout()
plt.show()




sns.set_theme(style="whitegrid")

# 1. Open a fresh canvas
plt.figure(figsize=(8, 5))

# 2. Draw the line plot
# Shows how CGPA changes as study hours change!
sns.lineplot(data=df, x='study_hours', y='cgpa', color='green')

# 3. Add titles and labels
plt.title("Trend of CGPA over Study Hours")
plt.xlabel("Weekly Study Hours")
plt.ylabel("CGPA")

# 4. Fit margins and show
plt.tight_layout()
plt.show()