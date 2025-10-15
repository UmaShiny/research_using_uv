import jpx
from jpx_config import table_format
from jpx_config import constant as const_cfg
from pathlib import Path
import pandas as pd
import re

# jpx_obj = jpx.dataset.pdf2csv(
#     jpx_pdf_dir=const_cfg.tmp_fmt4_input_dir,
#     output_csv_dir=const_cfg.fmt4_output_dir
# )

def check_nan_in_index():

    ta_dataset_path = Path(const_cfg.jpx_dataset_path)
    all_csv = [f for f in ta_dataset_path.rglob('*') if f.is_file() and f.suffix == '.csv']

    header = [
        "年月日",
        "コード",
        "銘柄名",
        "前場始値",
        "前場高値",
        "前場安値",
        "前場終値",
        "後場始値",
        "後場高値",
        "後場安値",
        "後場終値",
    ]

    for i, csv in enumerate(all_csv):
        df = pd.read_csv(csv)
        print("\r", f"Processing {csv}...{i+1}/{len(all_csv)}", end="")
        range_df = df.iloc[:, 0:3]
        mask = range_df.isnull().any(axis=1)
        df_with_nan = range_df[mask]
        if not df_with_nan.empty:
            print(f"\nRows with NaN:\n{df_with_nan}\n")
    return


def check_value():

    ta_dataset_path = Path(const_cfg.jpx_dataset_path)
    all_csv = [f for f in ta_dataset_path.rglob('*') if f.is_file() and f.suffix == '.csv']

    header = [
        "年月日",
        "コード",
        "銘柄名",
        "前場始値",
        "前場高値",
        "前場安値",
        "前場終値",
        "後場始値",
        "後場高値",
        "後場安値",
        "後場終値",
    ]

    exist_range_tuple = [
        (0, 3),
        (3, 7),
        (7, 11)
    ]

    # ある行のいずれかにNanが含まれている場合、その行を抽出する
    # ただし、すべてがNanである行は除外する
    for i, csv in enumerate(all_csv):
        df = pd.read_csv(csv)
        print("\r", f"Processing {csv}...{i+1}/{len(all_csv)}", end="")
        range_df = df.iloc[:, 7:11]
        mask = range_df.isnull().any(axis=1) & (~range_df.isnull().all(axis=1))
        df_with_nan = range_df[mask]
        if not df_with_nan.empty:
            print(f"\nRows with NaN in columns {header[7:11]}:\n{df_with_nan}\n")
    
    return


def extract_row():
    ta_dataset_path = Path(const_cfg.jpx_dataset_path)
    all_csv = [f for f in ta_dataset_path.rglob('*') if f.is_file() and f.suffix == '.csv']
    delete_ticker_list = []
    for i, csv in enumerate(all_csv):
        # 0 ~ 11列目までを抽出し、それ以外は削除する
        df = pd.read_csv(csv)
        print("\r", f"Processing {csv}...{i+1}/{len(all_csv)}", end="")
        mask = (df.iloc[:, 1] % 10 != 0) | (df.iloc[:, 2].str.contains("受益証券")) | (df.iloc[:, 2].str.contains("投資証券")) | (df.iloc[:, 2].str.contains("ETF")) | (df.iloc[:, 2].str.contains("ETN")) | (df.iloc[:, 2].str.contains("REIT")) | (df.iloc[:, 2].str.contains("外国株式")) | (df.iloc[:, 2].str.contains("新株予約権")) | (df.iloc[:, 2].str.contains("特別清算銘柄")) | (df.iloc[:, 2].str.contains("整理銘柄")) | (df.iloc[:, 2].str.contains("投信")) | (df.iloc[:, 2].str.contains("債券")) | (df.iloc[:, 2].str.contains("優先株")) | (df.iloc[:, 2].str.contains("ワラント"))
        delete_ticker_list.extend(df[mask].iloc[:, 1].tolist())
        delete_ticker_list = list(set(delete_ticker_list))
        

    delete_ticker_list = sorted(list(set(delete_ticker_list)))
    print(f"\nTotal extracted rows: {len(delete_ticker_list)}")

    for i, csv in enumerate(all_csv):
        df = pd.read_csv(csv)
        df.drop(df.columns[11:], axis=1, inplace=True)
        print("\r", f"Processing {csv} for deletion...{i+1}/{len(all_csv)}", end="")
        df_filtered = df[~df.iloc[:, 1].isin(delete_ticker_list)]
        df_filtered.iloc[:, 1] = (df_filtered.iloc[:, 1] // 10).astype(int)

        df_filtered.to_csv(f"./data/target_jpx_dataset/{csv.name}", index=False)
    
    print("\nCompleted cleaning and saving files.")





