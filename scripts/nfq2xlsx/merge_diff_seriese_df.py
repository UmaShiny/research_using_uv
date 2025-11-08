import pandas as pd
import numpy as np
from pathlib import Path

def merge_2df():
    series1_dir = Path('data/nfq/concat_nfqxlsx/concat_stcvol_nfqxlsx/20000101-20191231')
    series2_dir = Path('data/nfq/concat_nfqxlsx/concat_stcvol_nfqxlsx/20200101-20231231')

    output_dir = Path('data/nfq/concat_nfqxlsx/concat_stcvol_nfqxlsx/merged_concat_stcvol_nfqxlsx')

    series1_filepath = [f for f in series1_dir.rglob('.') if f.suffix == '.xlsx']
    series2_filepath = [f for f in series2_dir.rglob('.') if f.suffix == '.xlsx']

    while series1_filepath or series2_filepath:
        print('\r', f"remaining files - series1: {len(series1_filepath)}, series2: {len(series2_filepath)}", end=' ')
        series1_head, series2_head = None, None
        if series1_filepath and series2_filepath:
            series1_head = series1_filepath[0]
            series2_head = series2_filepath[0]
            # continue to merging process
        elif not series1_filepath and not series2_filepath:
            break
        elif not series1_filepath:
            series2_head = series2_filepath[0]
            print(f"copying: {series2_head.name}", end='  ')
            df = pd.read_excel(series2_head, sheet_name=pd.ExcelFile(series2_head).sheet_names[0], index_col=0)
            df.to_excel(output_dir / series2_head.name, sheet_name=series2_head.stem)
            series2_filepath.pop(0)
            continue
        elif not series2_filepath:
            series1_head = series1_filepath[0]
            print(f"copying: {series1_head.name}", end='  ')
            df = pd.read_excel(series1_head, sheet_name=pd.ExcelFile(series1_head).sheet_names[0], index_col=0)
            df.to_excel(output_dir / series1_head.name, sheet_name=series1_head.stem)
            series1_filepath.pop(0)
            continue
        else:
            break

        if series1_head.name == series2_head.name:

            print(f"merging: {series1_head.name}", end=' ')

            df1 = pd.read_excel(series1_head, sheet_name=pd.ExcelFile(series1_head).sheet_names[0], index_col=0)
            df2 = pd.read_excel(series2_head, sheet_name=pd.ExcelFile(series2_head).sheet_names[0], index_col=0)

            merged_df = pd.concat([df1, df2], axis=1)

            merged_df.to_excel(output_dir / series1_head.name, sheet_name=series1_head.stem)

            series1_filepath.pop(0)
            series2_filepath.pop(0)
        else:
            if series1_head.name < series2_head.name:
                print(f"copying: {series1_head.name}", end='  ')
                df = pd.read_excel(series1_head, sheet_name=pd.ExcelFile(series1_head).sheet_names[0], index_col=0)
                df.to_excel(output_dir / series1_head.name, sheet_name=series1_head.stem)
                series1_filepath.pop(0)
            else:
                print(f"copying: {series2_head.name}", end='  ')
                df = pd.read_excel(series2_head, sheet_name=pd.ExcelFile(series2_head).sheet_names[0], index_col=0)
                df.to_excel(output_dir / series2_head.name, sheet_name=series2_head.stem)
                series2_filepath.pop(0)

def delete_include_dot_column():
    dir_path = Path('data/nfq/concat_nfqxlsx/concat_stcvol_nfqxlsx/merged_concat_stcvol_nfqxlsx')
    del_cnt = 0
    for file_path in [f for f in dir_path.rglob('.') if f.suffix == '.xlsx']:
        print('\r', f"processing: {file_path.name}", end=' ')
        df = pd.read_excel(file_path, sheet_name=pd.ExcelFile(file_path).sheet_names[0], index_col=0)
        mask_dot = df.columns.astype(str).str.contains(r'\.')
        del_cnt += mask_dot.sum()
        df_cleaned = df.loc[:, ~mask_dot]
        df_cleaned.to_excel(file_path, sheet_name=file_path.stem)

    print(f"\r{del_cnt} rows deleted.          ")

# merge_2df()
delete_include_dot_column()