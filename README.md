# Chicago Crime Analysis

## 概要
　米国Illinois州Chicago市の犯罪認知件数データとACS人口統計データ(2020-2024)を結合し、Chicago市内77のcommunity area × year単位の時系列データセットおよび折れ線グラフを自動作成するものである。折れ線グラフの作成時，ユーザーは最大5つの変数を選択可能である。

　犯罪は暴力犯`violent1`，財産犯`property1`，風紀犯`public_order1`，その他`other1`の4類型である。

　また，人口統計データはコミュニティエリア人口`comm_pop`，男性人口`malepop`，15~19歳男性人口`male15_19pop`，15~24歳男性人口`male15_24pop`，15~29歳男性人口`male15_29pop`，白人人口`allwhitepop`，黒人(アフリカ系アメリカ人)人口`allblackpop`が含まれる。
　

　なお，この人口統計は米国国勢調査区単位のデータをChicago市`Community Area`ごとに，独自に再集計したものである。

## ユーザーの皆様へ(For all users)
### 以下のコマンドを手順に従ってターミナルに入力，実行の上，使用してください。(Before using this application, please input codes below to your terminal end execute.)

#### インストール手順

##### 1. リポジトリのクローン化(ユーザー名はご自身のものに置き換えてください。)

```bash
git clone https://github.com/ユーザー名/ChicagoCrime.git

cd ChicagoCrime
```

##### 2. 仮想環境の構築
本ソフトウェアでは、`uv` を用いて仮想環境を構築し、その環境内でプログラムおよび `pytest` によるテストを実行できます。

```bash
uv venv
```
##### 3. 仮想環境の有効化
Windowsの場合
```bash
.venv\Scripts\activate
```
macOS, Linuxの場合
```bash
source .venv/bin/activate
```


##### 4. 依存環境のインストール
```bash
uv pip install -r requirements.txt
```
##### 5. プログラムの実行
```bash
uv run python main.py
```

### pytestの実行手順
前出の手順4までを終えていただいた後，以下のコマンドをターミナルに入力の上，実行してください。
```bash
uv run pytest tests/test_main.py
```