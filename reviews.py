import pandas as pd
pd.set_option("display.max_rows", 5)
reviews = pd.read_csv("data\winemag-data-130k-v2.csv.zip", index_col = 0)

count = reviews.country.value_counts()
avg_points = reviews.groupby('country')['points'].mean().round(1)
reviews_merged = pd.DataFrame.merge(count, avg_points, on = 'country', how = 'inner')

print(reviews_merged)

with open('data\\reviews-per-country.csv', 'w') as csv_file:
    reviews_merged.to_csv(path_or_buf = csv_file)

