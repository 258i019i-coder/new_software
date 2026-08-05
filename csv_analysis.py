import numpy as np
import pandas as pd
import matplotlib
import geopandas as gpd
import subprocess
import re
import os

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


### 次に，ACSのデータをcommunity_areaごとに集計

# データセットの読み込み，リポジトリよりファイルを抽出
# Git管理されている _2020-2024.csv ファイルを取得
files = subprocess.check_output(
    ["git", "ls-files", "*_2020-2024.csv"],
    text=True
).splitlines()

# ACS_ と _2020-2024.csv の間を抽出
acs_list = [
    re.search(r"ACS(.*?)_2020-2024\.csv", f).group(1)
    for f in files
    if re.search(r"ACS(.*?)_2020-2024\.csv", f)
]

acs_summary = None

for dataset in acs_list:

    # 読み込み
    df1 = pd.read_csv(f"ACS{dataset}_2020-2024.csv")
    
    # 後ろ10列を除外
    sum_cols = df1.columns[:-10]

    # グループキーを除外
    sum_cols = [
        col for col in sum_cols
        if col not in ["year", "community_area"]
    ]

    # year × community_areaで集計
    result = (
        df1.groupby(
            ["year", "community_area"],
            as_index=False
        )[sum_cols]
        .sum()
    )


    # 横結合
    if acs_summary is None:
        acs_summary = result
    else:
        acs_summary = pd.merge(
            acs_summary,
            result,
            on=["year", "community_area"],
            how="outer"
        )

# print(acs_summary)
# print(crime_summary)

header = pd.read_csv("header.csv")






