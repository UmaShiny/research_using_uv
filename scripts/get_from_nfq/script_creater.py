import re
import pandas as pd

path_to_src_nfq = "data/nfq/nfq_src/AutoRun_sample.nfq" # このnfqファイルを参照して，必要な修正を実施後，dst_nfqに出力する
# path_to_dst_nfq = ".\\dst_nfq\\AutoRun_Allitem.nfq" # src_nfqを修正した内容を蓄積して，最終的に全社分のデータを取得できる自動実行スクリプトを作成する
path_to_datasrc_csv = "data/tickers/result/Tickers_with_Nikkei_copy.csv" # データを取得したい企業を一意に特定するための基本データが入ってるcsvファイル

src_csv_encoding = "shift_jis"
src_nfq_encoding = "utf-8"

dst_TickerHead_Memory:int = 1

datasrc_csv = pd.read_csv(path_to_datasrc_csv, encoding=src_csv_encoding)
dst_nfq_nikkeiList:list[str] = datasrc_csv["nikkei"].tolist()
dst_nfq_tickerList:list[str] = datasrc_csv["ticker"].tolist()
dst_nfq_JpNameList:list[str] = datasrc_csv["ja"].tolist()
dst_nfq_EnNameList:list[str] = datasrc_csv["eng"].tolist()
zipped_dst_nfq_Ticker_JpName_EnName_List = list(zip(dst_nfq_nikkeiList, dst_nfq_tickerList, dst_nfq_JpNameList, dst_nfq_EnNameList))

# src_nfqの置き換え対象を変数として定義する
src_nfq_Nikkei:str = "Ticker"
src_nfq_JpName:str = "JpName"
src_nfq_EnName:str = "EnName"

SRC_PATTERN_TUPLE_INEDX, DST_REPLACE_TUPLE_INEDX = 0, 1
for dst_nfq_nikkei, dst_nfq_ticker, dst_nfq_JpName, dst_nfq_EnName in zipped_dst_nfq_Ticker_JpName_EnName_List:
    path_to_dst_nfq = f"data/nfq/nfq_dst/AutoRun_{dst_nfq_ticker}.nfq"
    print("\r", f"Now creating {path_to_dst_nfq} ...", end="")
    src_to_dst_replace_tuple:tuple[tuple[str,str], ...] = ((src_nfq_Nikkei, dst_nfq_nikkei), # modify_order = 0
                                                           (src_nfq_JpName, dst_nfq_JpName), # modify_order = 1
                                                           (src_nfq_EnName, dst_nfq_EnName)) # modify_order = 2
    with open(path_to_dst_nfq, "ab") as dst_nfq_fp:
        with open(path_to_src_nfq, "rb") as src_nfq_fp:
            src_nfq_all_content = src_nfq_fp.read()
            dst_nfq_all_content = src_nfq_all_content
            for modify_order in range(len(src_to_dst_replace_tuple)):
                dst_nfq_all_content = dst_nfq_all_content.replace(
                    src_to_dst_replace_tuple[modify_order][SRC_PATTERN_TUPLE_INEDX].encode(src_nfq_encoding),
                    src_to_dst_replace_tuple[modify_order][DST_REPLACE_TUPLE_INEDX].encode(src_csv_encoding),
                )
            dst_nfq_fp.write(dst_nfq_all_content)
print("\nThe AutoRun script has been generated")

# scripts\get_from_nfq\script_creater.py