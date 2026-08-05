# new_software
# Chicago Crime Analysis

## 概要
Chicagoの犯罪データとACS人口統計データを結合し、
community area × year単位の分析用データを作成する。


## ユーザーの皆様へ(For all users)
### 以下のコマンドを手順に従ってターミナルに入力，実行の上，使用してください。(Before using this application, please input codes below to your terminal end execute.)

#### インストール手順

##### 1. リポジトリのクローン化(ユーザー名はご自身のものに置き換えてください。)

```bash
git clone https://github.com/ユーザー名/ChicagoCrime.git

cd ChicagoCrime
```

##### 2. 仮想環境の構築
```bash
uv venv
```
##### 3. 仮想環境の有効化
```bash
.venv\Scripts\activate
```

##### 4. 依存環境のインストール
```bash
uv pip install -r requirements.txt
```
##### 5. プログラムの実行
```bash
uv run python main.py
```

