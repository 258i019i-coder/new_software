import pandas as pd


def create_chicago(crime_summary, acs_summary):

    header = pd.read_csv(
        "header.csv"
    )

    chicago = pd.merge(
        header,
        crime_summary,
        on=[
            "year",
            "community_area"
        ],
        how="left"
    )

    chicago = pd.merge(
        chicago,
        acs_summary,
        on=[
            "year",
            "community_area"
        ],
        how="left"
    )

    return chicago