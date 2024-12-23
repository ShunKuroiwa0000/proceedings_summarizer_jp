import sqlite3

# データベースファイルのパス
db_path = "C:\shun\Visual_Studio_Code\Proceedings-summarizer-main\summaries.db"

# データベース接続
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# SQLクエリの実行
query = "SELECT japanese_title FROM pdf_summaries;"
cursor.execute(query)

# 結果を取得
japanese_titles = cursor.fetchall()

# 結果を表示
for title in japanese_titles:
    print(title[0])

# データベース接続を閉じる
conn.close()
