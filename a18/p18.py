import sys
import pandas as pd

positive_keywords = [
    "love","fantastic", "intuitive",
    "powerful", "easy", "promising",
    "must-have", "5-star",
]

try:
    df = pd.read_excel('social_media_feed_raw.xlsx')
    print("File load successful")
    print(df)
except FileNotFoundError:
    print("Error: file not found. Make sure it is in the same directory.")
    sys.exit()

# create a duplicate of the original data so it can be printed later
df_original = df.copy()

# remove duplicate rows and rows with missing values
df.drop_duplicates(inplace = True)
df.dropna(inplace = True)

# filter to only rows within the specified range
start_d = "2025-01-01"
end_d = "2026-01-05"
date_range = pd.date_range(start = start_d, end = end_d)
df_date_cleaned = df[df["Date"].isin(date_range)]

# convert the 'Review' column to lowercase
df['Review'] = df['Review'].str.lower()

extracted_feedback_data = []
for i, review in enumerate(df['Review']):
    # Determine simplified sentiment
    # if any positive words are in the review,
    # the sentiment is positive
    # otherwise, the sentiment is neutral
    sentiment = "Neutral"
    if any(keyword in review for keyword in positive_keywords):
        sentiment = "Positive"
    extracted_feedback_data.append({
        "user": f"u{i+1:02d}",
        "original_feedback": review,
        "sentiment": sentiment,
    })

df_feedback = pd.DataFrame(extracted_feedback_data)

print("=" *80)
print("original data")
print("=" *80)
print(df_original)

print("=" *80)
print("cleaned data")
print("=" *80)
print(df)

print("=" *80)
print("reviews and computed sentiment")
print("=" *80)
print(df_feedback)