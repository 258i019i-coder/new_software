from main import main
import pandas as pd


def test_main_output():

    chicago = main()

    assert isinstance(chicago, pd.DataFrame)

    assert len(chicago) > 0

    assert "community_area" in chicago.columns