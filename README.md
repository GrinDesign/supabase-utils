
## 使い方

1. 仮想環境の作成・有効化
    ```sh
    python3 -m venv venv
    source venv/bin/activate
    ```

2. 必要なパッケージのインストール
    ```sh
    pip install -r requirements.txt
    ```

3. .envファイルの作成（DB接続情報などを記載）

4. テーブル作成
    ```sh
    python create_table.py azuma-insight/sql/quotes.sql
    python create_table.py azuma-insight/sql/users.sql
    python create_table.py azuma-insight/sql/impressions.sql
    ```

## TODO

- [x] テーブル作成用SQLの整備
- [ ] テーブル削除スクリプトの追加
- [ ] 初期データ投入スクリプトの追加
- [ ] ドキュメントの充実

## ライセンス

