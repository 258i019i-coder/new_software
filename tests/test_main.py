from main import main
import pandas as pd
from pathlib import Path


def test_main_output(monkeypatch, tmp_path):

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

    # jpgファイルが作成されたことを確認
    jpg_file = Path("chicago_trend.jpg")

    assert jpg_file.exists()

    # jpgファイルが空でないことを確認
    assert jpg_file.stat().st_size > 0