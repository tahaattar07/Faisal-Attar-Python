import pandas as pd

df = pd.read_csv("students.csv")

print("Original Data:")
print(df)

print("\nMissing Values:")
print(df.isnull().sum())

subjects = ["Maths", "Physics", "Chemistry", "English", "Computer"]

for subject in subjects:
    df[subject] = df[subject].fillna(df[subject].mean())


df["Total"] = df[subjects].sum(axis=1)
df["Percentage"] = df["Total"] / len(subjects)

print("\nUpdated Data:")
print(df)


print("\nStatistics:")
print(df[subjects + ["Total", "Percentage"]].describe())
