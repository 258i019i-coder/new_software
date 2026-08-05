import pandas as pd


def create_crime_summary(start_year=2020, end_year=2024):

    dfs = []

    for year in range(start_year, end_year + 1):
        df = pd.read_csv(f"Crimes{year}.csv")
        dfs.append(df)

    crime = pd.concat(dfs, ignore_index=True)

    crime_dict = pd.read_csv(
        "crime_dictionary.csv"
    )

    crime_merge = pd.merge(
        crime,
        crime_dict,
        on="primary_type",
        how="left"
    )

    crime_merge.rename(
        columns={
            "crime_group1_prime": "crimetype"
        },
        inplace=True
    )

    crime_summary = (
        crime_merge
        .groupby(
            [
                "year",
                "community_area",
                "crimetype"
            ]
        )
        .size()
        .unstack(fill_value=0)
        .reset_index()
    )

    return crime_summary