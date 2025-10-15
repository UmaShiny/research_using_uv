import re
import pandas as pd

path_to_src_nfq = ".\\src_nfq\\AutoRun_exapmle_copy.nfq" # このnfqファイルを参照して，必要な修正を実施後，dst_nfqに出力する
# path_to_dst_nfq = ".\\dst_nfq\\AutoRun_Allitem.nfq" # src_nfqを修正した内容を蓄積して，最終的に全社分のデータを取得できる自動実行スクリプトを作成する
path_to_datasrc_csv = ".\\csv\\Ticker_JpName_EnName.csv" # データを取得したい企業を一意に特定するための基本データが入ってるcsvファイル

src_csv_encoding = "shift_jis"
src_nfq_encoding = "utf-8"

dst_TickerHead_Memory:int = 10

datasrc_csv = pd.read_csv(path_to_datasrc_csv, encoding=src_csv_encoding)
dst_nfq_tickerList:list[str] = datasrc_csv["TICKER"].tolist()
dst_nfq_JpNameList:list[str] = datasrc_csv["CORPORATE_CCANAME"].tolist()
dst_nfq_EnNameList:list[str] = datasrc_csv["CORPORATE_ENAME1"].tolist()
zipped_dst_nfq_Ticker_JpName_EnName_List = list(zip(dst_nfq_tickerList, dst_nfq_JpNameList, dst_nfq_EnNameList))

# src_nfqの置き換え対象を変数として定義する
src_nfq_Ticker:str = "src_nfq_Ticker"
src_nfq_JpName:str = "src_nfq_JpName"
src_nfq_EnName:str = "src_nfq_EnName"

SRC_PATTERN_TUPLE_INEDX, DST_REPLACE_TUPLE_INEDX = 0, 1
for dst_nfq_Ticker, dst_nfq_JpName, dst_nfq_EnName in zipped_dst_nfq_Ticker_JpName_EnName_List:
    if not dst_nfq_Ticker[1].isdigit(): continue
    dst_TickerHead = int(dst_nfq_Ticker[1:3])
    if dst_TickerHead > dst_TickerHead_Memory: dst_TickerHead_Memory = dst_TickerHead
    path_to_dst_nfq = f".\\dst_nfq\\AutoRun_Allitem_{dst_TickerHead_Memory}_test.nfq"
    src_to_dst_replace_tuple:tuple[tuple[str,str], ...] = ((src_nfq_Ticker, dst_nfq_Ticker), # modify_order = 0
                                                           (src_nfq_JpName, dst_nfq_JpName), # modify_order = 1
                                                           (src_nfq_EnName, dst_nfq_EnName)) # modify_order = 2
    with open(path_to_dst_nfq, "ab") as dst_nfq_fp:
        with open(path_to_src_nfq, "rb") as src_nfq_fp:
            src_nfq_all_content = src_nfq_fp.read()
            dst_nfq_all_content = src_nfq_all_content
            for modify_order in range(len(src_to_dst_replace_tuple)):
                dst_nfq_all_content = dst_nfq_all_content.replace(src_to_dst_replace_tuple[modify_order][SRC_PATTERN_TUPLE_INEDX].encode(src_nfq_encoding),
                                                                  src_to_dst_replace_tuple[modify_order][DST_REPLACE_TUPLE_INEDX].encode(src_csv_encoding),)
            dst_nfq_fp.write(dst_nfq_all_content)
print("The AutoRun script has been generated")