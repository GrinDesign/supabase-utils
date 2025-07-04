# supabase_utils

Supabase用のPythonユーティリティパッケージです。
複数プロジェクトで共通して使えるSupabase接続・データ操作の関数をまとめています。

## 使い方

1. 各プロジェクトで仮想環境を作成・有効化し、必要なパッケージをインストール
    ```sh
    python3 -m venv venv
    source venv/bin/activate
    pip install -e ../supabase-utils
    ```

2. 各プロジェクト直下に`.env`ファイルを作成し、以下を記載
    ```
    SUPABASE_URL=あなたのSupabaseプロジェクトURL
    SUPABASE_KEY=あなたのanonキー
    ```

3. テーブル作成やテストデータ追加は各プロジェクトで行ってください

4. テストスクリプト例（テーブル名を引数で指定可能）
    ```python
    from supabase_utils.test_connection import test_connection

    if __name__ == "__main__":
        result = test_connection("test_table")  # 任意のテーブル名
        if result:
            print("Supabase接続テスト：成功！")
        else:
            print("Supabase接続テスト：失敗！")
    ```
    または、コマンドラインから直接：
    ```sh
    python supabase_utils/test_connection.py test_table
    ```

## TODO

- [x] テーブル名を引数で指定できる接続テスト関数
- [ ] データ追加・取得・更新・削除関数の追加
- [ ] ドキュメントの充実

## ライセンス

MIT

