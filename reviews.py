import pandas as pd
pd.set_option("display.max_rows", 10)
reviews = pd.read_csv("./data/winemag-data-130k-v2.csv.zip", index_col = 0)

count = reviews.country.value_counts()
avg_points = reviews.groupby('country')['points'].mean().round(1)
reviews_merged = pd.DataFrame.merge(count, avg_points, on = 'country', how = 'inner')
reviews_merged.to_csv('./data/reviews-per-country.csv')

print(reviews_merged)



