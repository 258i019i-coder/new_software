from main import main
import pandas as pd


def test_main_output(monkeypatch):

    # visualization.py内のinput()に自動で値を渡す
    monkeypatch.setattr(
        "builtins.input",
        lambda _: "1"
    )

    chicago = main()

    # 戻り値がDataFrameであることを確認
    assert isinstance(chicago, pd.DataFrame)

    # データが1件以上あることを確認
    assert len(chicago) > 0

    # 必要な列が存在することを確認
    assert "community_area" in chicago.columns