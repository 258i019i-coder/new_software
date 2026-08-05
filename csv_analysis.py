import numpy as np
import pandas as pd
import matplotlib
import geopandas as gpd


# まずは，crime のデータに分類辞書を結合する

crime_dict = pd.read_csv(r"crime_dictionary.csv")

# まずは，各年のcrime.csvを縦結合し，5年分のデータを作る
dfs = {}

for year in range(2020, 2024+1):
    dfs[year] = pd.read_csv(rf"Crimes{year}.csv") 
    # dfs.append(df)

crime = pd.concat(dfs.values(), ignore_index=True)

col = crime.pop("year")
crime.insert(1, "year", col)


# 次に，crime のデータに分類辞書を結合する
crime_dict = pd.read_csv(r"crime_dictionary.csv")

crime_merge = pd.merge(crime, crime_dict, on = "primary_type", how = "left")
col = crime_merge.pop("crime_group1_prime")
crime_merge.insert(2, "crime_group1_prime", col)
crime_merge.rename(columns = {"crime_group1_prime" : "crimetype"}, inplace = True)


# 最後に，年別，コミュニティエリア別の集計表を作る
crime_summary = (
    crime_merge
    .groupby(["year", "community_area", "crimetype"])
    .size()
    .unstack(fill_value=0)
    .reset_index()
)


print(crime_summary)


