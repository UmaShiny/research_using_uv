from config import cons
import pandas as pd
import numpy as np
from pathlib import Path
import os
# 1. add nikkei-code to index of ta-db

def test_missing_nikkei_codes(daily_data_csv_path: Path):
    nfqcsv_path = Path('data/nfq/nfqcsv/main_nfqcsv')
    nikkei_codes_1 = [fp.stem for fp in nfqcsv_path.rglob('.') if fp.suffix == '.csv']

    daily_data_csv = pd.read_csv(f'data/expansed_technical/{daily_data_csv_path.name}')
    nikkei_codes_2 = daily_data_csv['nikkei'].unique().tolist()

    missing_nikkei_codes = len(set(nikkei_codes_1) - set(nikkei_codes_2))
    if missing_nikkei_codes != 0:
        raise ValueError(f'Missing nikkei codes found in {daily_data_csv_path.name}: {missing_nikkei_codes}')
    
    print(missing_nikkei_codes, end='')

def expanse_dailydb_with_nikkei_code():
    nkc_tkc_map_csv = Path(cons.path.nkc_tkc_map_csv)
    nkc_tkc_map_df = pd.read_csv(nkc_tkc_map_csv, dtype=str).copy()
    delete_from_expansed_daily_data_df = pd.read_csv(cons.path.deleted_tickers_csv)
    
    daily_data_csv_dir = Path(cons.path.daily_data_csvs)
    daily_data_csv_path_list = [fp for fp in daily_data_csv_dir.rglob('.') if fp.suffix == '.csv']

    dst_dir_path = Path('data/expansed_technical/')

    for daily_data_csv_path in daily_data_csv_path_list:

        print("\r", f'Processing {daily_data_csv_path.name}...', end=' ')

        daily_data_df = pd.read_csv(daily_data_csv_path)

        # nikkeiコードとtickerコードのデータ型をstr型に変換する
        nkc_tkc_map_df['ticker'] = nkc_tkc_map_df['ticker'].astype(str)
        daily_data_df[daily_data_df.columns[1]] = daily_data_df[daily_data_df.columns[1]].astype(str)

        # 外部結合することで，一つの大きなデータフレームにする
        expansed_daily_data_df = nkc_tkc_map_df.merge(
            daily_data_df,
            left_on='ticker',
            right_on=daily_data_df.columns[1],
            how='outer'
        )

        # nikkeiコードが空の場合はその行を削除し，不要な情報を削除する
        expansed_daily_data_df = expansed_daily_data_df[~expansed_daily_data_df['nikkei'].isnull()]
        expansed_daily_data_df.drop(columns=expansed_daily_data_df.columns[3:7], inplace=True)
        dup_mask = ~expansed_daily_data_df.duplicated(subset=['nikkei'])
        expansed_daily_data_df = expansed_daily_data_df[dup_mask]
        delete_mask = expansed_daily_data_df['nikkei'].isin(delete_from_expansed_daily_data_df['nikkei'])
        expansed_daily_data_df = expansed_daily_data_df[~delete_mask]

        # いったん保存して終了
        expansed_daily_data_df.to_csv(
            dst_dir_path / daily_data_csv_path.name,
            index=False
        )

        # 欠損しているnikkeiコードがないか確認する
        test_missing_nikkei_codes(daily_data_csv_path)

expanse_dailydb_with_nikkei_code()