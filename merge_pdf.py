import PyPDF2 as pp2
import glob
import sys

def merge_pdfs(path):
    # フォルダ内の全PDFファイルを読み込み
    pdf_list = glob.glob(fr"{path}\*.pdf")

    # 結合機能を呼び出し
    merger = pp2.PdfMerger()

    # ループで全PDFファイルを結合機能へ格納
    for pdf in pdf_list:
        merger.append(pdf)

    # 結合して保存する
    merger.write(fr"{path}\merged.pdf")

    # 結合機能を閉じる←必要
    merger.close()

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python merge_pdf.py <path_to_pdf_folder>")
    else:
        merge_pdfs(sys.argv[1])