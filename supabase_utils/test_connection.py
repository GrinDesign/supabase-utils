import os
from dotenv import load_dotenv
from supabase import create_client

def test_connection():
    # .envファイルを読み込む
    load_dotenv()
    url = os.getenv("SUPABASE_URL")
    key = os.getenv("SUPABASE_KEY")
    supabase = create_client(url, key)
    try:
        # quotesテーブルのデータを1件取得してみる
        res = supabase.table("quotes").select("*").limit(1).execute()
        print("データ例:", res.data)
        return True
    except Exception as e:
        print("接続エラー:", e)
        return False

if __name__ == "__main__":
    test_connection()