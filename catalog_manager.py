import pandas as pd

print("VIDEO GAME CATALOG MANAGER")

# 1. Read the CSV file with Pandas (the original file is never modified)
df = pd.read_csv("video_games_raw.csv")

# Make sure Price and Rating are numbers (handles values like "$39.99")
df["Price"] = pd.to_numeric(df["Price"].astype(str).str.replace("$", "", regex=False), errors="coerce")
df["Rating"] = pd.to_numeric(df["Rating"], errors="coerce")

# 2. Ask the user for a row number to inspect
row_number = int(input("Enter a row number to inspect: "))

# 3. Use .iloc[] to access the row by position
game = df.iloc[row_number]

print("\nSelected Game:")
print(f"Title: {game['Title']}")
print(f"Platform: {game['Platform']}")
print(f"Genre: {game['Genre']}")
print(f"Rating: {game['Rating']}")
print(f"Current Status: {game['Status']}")

# 4. Ask for a new status
print("\nEnter a new status:")
new_status = input()

# 5. Use .at[] to update that one specific value
# (.at uses the index label; with the default index, label == position)
df.at[df.index[row_number], "Status"] = new_status

# 6. Add a Recommended column
# Start everyone at "No", then use .loc[] to change multiple rows to "Yes"
df["Recommended"] = "No"
df.loc[(df["Rating"] >= 8) & (df["Price"] <= 40), "Recommended"] = "Yes"

# 7. Use .query() to display the recommended games
print("\nRecommended Games:")
recommended = df.query("Recommended == 'Yes'")
print(recommended[["Title", "Platform", "Price", "Rating"]])

# 8. Save to a NEW file
df.to_csv("video_games_cleaned.csv", index=False)

print("\nThe catalog has been updated.")
print("Saved as video_games_cleaned.csv.")
