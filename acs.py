import pandas as pd
import glob


def create_acs_summary():

    files = glob.glob(
        "*_2020-2024.csv"
    )

    acs_summary = None

    for file in files:

        df = pd.read_csv(file)

        sum_cols = [
            col for col in df.columns[:-10]
            if col not in [
                "year",
                "community_area"
            ]
        ]

        result = (
            df.groupby(
                [
                    "year",
                    "community_area"
                ],
                as_index=False
            )[sum_cols]
            .sum()
        )

        if acs_summary is None:
            acs_summary = result

        else:
            acs_summary = pd.merge(
                acs_summary,
                result,
                on=[
                    "year",
                    "community_area"
                ],
                how="outer"
            )

    return acs_summary