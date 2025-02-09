## 開発源
https://github.com/ShotaImamura/Proceedings-summarizer/blob/main

これを日本語のProceedingsでも利用可能にしたもの．  
文字コードをShift-JISに変更．  
モデルは好きなモデル使ってください．  

## システムの用途
ACM等の学会のプロシーディングスを各研究１ページの紹介スライドにまとめるコードです



## セットアップ

### 0. プロシーディングスのダウンロード
まずはACM DL等からプロシーディングスをダウンロードします。

ダウンロード元は  
CHIだと https://dl.acm.org/conference/chi/proceedings  
IUIだと https://dl.acm.org/conference/iui/proceedings  
UISTだと https://dl.acm.org/conference/uist/proceedings  
等に過去のプロシーディングス一覧がまとまっています。

他のACMの多くの学会も以下のように学会のacronymをパスを設定すると出てきます。
https://dl.acm.org/conference/****/proceedings

Parse_jp.py及びParse_en.pyについて，Proceedingsに併せて以下の箇所を変更する必要があります．

```bash
if any(keyword in text.lower() for keyword in ["ABSTRACT"]) or i == pdf.page_count - 1:
```
現在ABSTRACTとなっているところ，各論文につき必ず一つだけ入っている単語に変えてください．  
日本語だと概要，要約，辺りだとおもいます．  
ここを変更しないと，論文ごとにデータが分けられないので，うまく機能しません．  



続いて、以降のセットアップを用いてセットアップをしてください。

### 1. Python仮想環境の作成
Pythonの仮想環境を作成し、`requirements.txt`をインストールします。

```bash
python -m venv env
source env/bin/activate  # Windowsの場合は `env\Scripts\activate`
pip install -r requirements.txt
```

### 2. OpenAI APIキーの設定
OpenAIのAPIキーを環境変数`OPENAI_API_KEY`として設定します。

```bash
export OPENAI_API_KEY="your_openai_api_key"  # Windowsの場合は `set OPENAI_API_KEY=your_openai_api_key`
```

### 3. スクリプトの実行
以下の順にスクリプトを実行します。

```bash
# 3.1 parse.pyの実行
日本語のProceedingsを要約する場合，
python parse_jp.py <pdf file name>

英語のProceedingsを要約する場合
python parse_en.py <pdf file name>



# 3.2 keyvisual.pyの実行
python keyvisual.py

```

### 4. データベースの作成
`create_db.py`を実行して論文データベースを作成します。

```bash
python create_db.py
```

OpenAIの出力の揺らぎやJSONのパースの問題でデータベースの作成時にエラーが出る場合があります。
標準出力と、summarize/error/　にエラーが書き出されるようになっています。

```
Error in inserting data: Incorrect number of bindings supplied. 
```
というエラーが（新規に）ある場合にはcreate_db.pyを再実行してください。

すでに要約済みのものはスキップした上で、正常に完了していない研究についての要約をデータベースに追加します。

### 5. 論文要約PDFの作成
`make_pdf_jp.py`を実行して、論文の要約PDFを作成します。

```bash
python make_pdf_jp.py  # 日本語の要約PDFを作成する場合。日本語版はoutputディレクトリに、全論文を要約したPDFと（デフォルトでは）100ページ毎に分割したPDF群が出力されます。
```

### 追加機能
`merge_pdf.py`  
Proceedingsではなくいくつかのばらばらの論文をまとめてスライドにしたいとき，それらの論文をまとめて  
一つのpdfファイルにまとめている．論文誌がなく，それぞれが単体の論文が発行されている場合に利用する．  

```bash
python merge_pdf.py <folder_path>
```

### 現状の課題
- 毎回dataフォルダ，outputフォルダを削除する必要あり．
- 図やグラフの抽出はまだいまいち．




