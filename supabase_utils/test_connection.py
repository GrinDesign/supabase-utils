import os
from dotenv import load_dotenv
from supabase import create_client
import sys

def test_connection(table_name="quotes"):
    # .envファイルを読み込む
    load_dotenv()
    url = os.getenv("SUPABASE_URL")
    key = os.getenv("SUPABASE_KEY")
    print("URL:",url)
    print("Key:",key)
    supabase = create_client(url, key)
    try:
        # 指定されたテーブルのデータを1件取得してみる
        res = supabase.table(table_name).select("*").limit(1).execute()
        print(f"{table_name}テーブルのデータ例:", res.data)
        return True
    except Exception as e:
        print("接続エラー:", e)
        return False

if __name__ == "__main__":
    # コマンドライン引数でテーブル名を指定できるようにする
    table_name = sys.argv[1] if len(sys.argv) > 1 else "quotes"
    test_connection(table_name)