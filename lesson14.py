import pandas as pd

data = {
    "name": ["Juan", "Maria", "Carlos", "Ana"],
    "age": [45, 38, 29, 52],
    "city": ["Monterrey", "Guadalajara", "Monterrey", "CDMX"]
}

df = pd.DataFrame(data)
#print(df)
#print(df.head())          # first 5 rows (useful for big datasets)
#print(df.shape)            # (rows, columns)
#print(df.columns)          # column names
#print(df.info())           # data types + non-null counts per column
#print(df["age"])           # a single column
#print(df[["name", "age"]]) # multiple columns — note the double brackets

#print(df[df["city"] == "Monterrey"])  # filter rows by a condition
#print(df["age"].mean())          # mean of a column

# Sorting
#print(df.sort_values("age"))
#print(df.sort_values("age", ascending=False))

# Adding a new column
#df["is_senior"] = df["age"] > 50
#print(df)

# Grouping — genuinely one of the most powerful tools in pandas
#print(df.groupby("city")["age"].mean())

df["age_in_10_years"] = df["age"] + 10
print(df.groupby("city")["age_in_10_years"].mean().sort_values(ascending=False))