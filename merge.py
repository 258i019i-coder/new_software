import pandas as pd


def create_chicago():

    from crime import create_crime_summary
    from acs import create_acs_summary


    crime = create_crime_summary()

    acs = create_acs_summary()

    header = pd.read_csv(
        "header.csv"
    )


    chicago = pd.merge(
        header,
        crime,
        on=[
            "year",
            "community_area"
        ],
        how="left"
    )


    chicago = pd.merge(
        chicago,
        acs,
        on=[
            "year",
            "community_area"
        ],
        how="left"
    )


    return chicago