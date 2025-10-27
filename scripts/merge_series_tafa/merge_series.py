from config import cons
import pandas as pd
import numpy as np
from pathlib import Path
import datetime

import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)
# 1. add nikkei-code to index of ta-db

class technical:
    # helper function
    @staticmethod
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
            technical.test_missing_nikkei_codes(daily_data_csv_path)

    # helper function
    @staticmethod
    def ampm_to_daily(df: pd.DataFrame) -> pd.DataFrame:
        df.columns = [
            'nikkei', 'ticker', 'jp',
            'am_open', 'am_high', 'am_low', 'am_close',
            'pm_open', 'pm_high', 'pm_low', 'pm_close',
        ]

        cols_to_clean = ['am_open', 'am_high', 'am_low', 'am_close', 'pm_open', 'pm_high', 'pm_low', 'pm_close']  # カンマが入りやすい列
        for col in cols_to_clean:
            df[col] = df[col].astype(str).str.replace(',', '', regex=False)

        df = df.astype({
            'nikkei'    : 'string',
            'ticker'    : 'string',
            'jp'        : 'string',
            'am_open'   : 'float64',
            'am_high'   : 'float64',
            'am_low'    : 'float64',
            'am_close'  : 'float64',
            'pm_open'   : 'float64',
            'pm_high'   : 'float64',
            'pm_low'    : 'float64',
            'pm_close'  : 'float64',
        })

        open_select_am_mask = df['am_open'].isna() # If AM open is NaN, select PM open
        df['open'] = np.where(open_select_am_mask, df['pm_open'], df['am_open'])

        high_select_am_mask = (df['am_high'] > df['pm_high']) | df['pm_high'].isna()
        df['high'] = np.where(high_select_am_mask, df['am_high'], df['pm_high'])

        low_select_am_mask = (df['am_low'] < df['pm_low']) | df['pm_low'].isna()
        df['low'] = np.where(low_select_am_mask, df['am_low'], df['pm_low'])

        close_select_am_mask = df['pm_close'].isna() # If PM close is NaN, select AM close
        df['close'] = np.where(close_select_am_mask, df['am_close'], df['pm_close'])

        df.drop(columns=[
            'am_open', 'am_high', 'am_low', 'am_close',
            'pm_open', 'pm_high', 'pm_low', 'pm_close',
        ], inplace=True)

        df = df.astype({
            'nikkei': 'string',
            'ticker': 'string',
            'jp'    : 'string',
            'open'  : 'float64',
            'high'  : 'float64',
            'low'   : 'float64',
            'close' : 'float64',
        })

        # df.columns = ['nikkei', 'ticker', 'jp', 'open', 'high', 'low', 'close']
        return df


    def get_weekly_data():
        ampm_expansed_data_csvs_dir = Path(cons.path.ampm_expansed_data_csvs)
        ampm_expansed_data_csv_path_list = sorted([fp for fp in ampm_expansed_data_csvs_dir.rglob('.') if fp.suffix == '.csv'])
        dst_dir_path = Path(cons.path.weekly_expansed_data_csvs)

        weekly_df = pd.DataFrame()
        passed_weekdays = []
        cnt = 0

        for ampm_data_csv_path in ampm_expansed_data_csv_path_list:
            print("\r", f'Processing {ampm_data_csv_path.name}...', end='')

            csv_date = ampm_data_csv_path.stem
            ampm_df = pd.read_csv(ampm_data_csv_path)

            daily_df = technical.ampm_to_daily(ampm_df)

            year = int(csv_date[:4])
            month = int(csv_date[4:6])
            day = int(csv_date[6:8])

            date = datetime.date(year, month, day)
            weekday = date.weekday()  # Monday is 0 and Sunday is 6

            daily_df.to_csv(
                Path(cons.path.daily_expansed_data_csvs) / f'daily_expansed_technical_{csv_date}_{weekday}.csv',
                index=False
            )

            if weekly_df.empty: # 未登録の場合だけ特別に処理する
                weekly_df['nikkei'] = daily_df['nikkei']
                weekly_df['ticker'] = daily_df['ticker']
                weekly_df['jp'] = daily_df['jp']

            if weekday == 2 or (weekday in passed_weekdays):  # If Wednesday or a previously passed weekday: finalize and save the week's data

                all_open_columns = [col for col in weekly_df.columns if 'open' in col]
                only_open_df = weekly_df[all_open_columns]
                weekly_df['open'] = only_open_df.bfill(axis=1).iloc[:, 0]  # Use the first open of the week

                all_high_columns = [col for col in weekly_df.columns if 'high' in col]
                weekly_df['weekly_high'] = weekly_df[all_high_columns].max(axis=1)
                
                all_low_columns = [col for col in weekly_df.columns if 'low' in col]
                weekly_df['weekly_low'] = weekly_df[all_low_columns].min(axis=1)

                all_close_columns = [col for col in weekly_df.columns if 'close' in col]
                only_close_df = weekly_df[all_close_columns]
                weekly_df['close'] = only_close_df.ffill(axis=1).iloc[:, -1]  # Use the last close of the week

                drop_columns = [col for col in weekly_df.columns if col not in ['nikkei', 'ticker', 'jp', 'open', 'weekly_high', 'weekly_low', 'close']]
                weekly_df.drop(columns=drop_columns, inplace=True)

                weekly_df = weekly_df[['nikkei', 'ticker', 'jp', 'open', 'weekly_high', 'weekly_low', 'close']]

                weekly_df.to_csv(
                    dst_dir_path / f'weekly_expansed_technical_{cnt}.csv', index=False
                )
                cnt += 1
                weekly_df = pd.DataFrame()
                passed_weekdays = []

                daily_df.columns = ['nikkei', 'ticker', 'jp', f'open_{weekday}', f'high_{weekday}', f'low_{weekday}', f'close_{weekday}']
                df_subset = daily_df.iloc[:, 0:7]
                weekly_df = pd.concat([weekly_df, df_subset], axis=1)
            else: # Monday, Thursday, Friday : only high and low are needed
                daily_df.columns = ['nikkei', 'ticker', 'jp', f'open_{weekday}', f'high_{weekday}', f'low_{weekday}', f'close_{weekday}']
                df_subset = daily_df.iloc[:, 3:7]
                weekly_df = pd.concat([weekly_df, df_subset], axis=1)
            passed_weekdays.append(weekday)

    def get_monthly_data():
        daily_expansed_data_csvs_dir = Path(cons.path.daily_expansed_data_csvs)
        daily_expansed_data_csv_path_list = sorted([fp for fp in daily_expansed_data_csvs_dir.rglob('.') if fp.suffix == '.csv'])
        dst_dir_path = Path(cons.path.monthly_expansed_data_csvs)

        monthly_df = pd.DataFrame()
        previous_month = 1
        for daily_expansed_data_csv_path in daily_expansed_data_csv_path_list:
            print("\r", f'Processing {daily_expansed_data_csv_path.name}...', end='')
            daily_df = pd.read_csv(daily_expansed_data_csv_path)

            # ex.) daily_expansed_technical_20010104_3.csv
            daily_code = daily_expansed_data_csv_path.stem

            day = int(daily_code[31:33])  # Extract day from filename
            month = int(daily_code[29:31])  # Extract month from filename
            year = int(daily_code[25:29])  # Extract year from filename

            if monthly_df.empty:  # 未登録の場合だけ特別に処理する
                monthly_df['nikkei'] = daily_df['nikkei']
                monthly_df['ticker'] = daily_df['ticker']
                monthly_df['jp'] = daily_df['jp']

            if previous_month != month:
                all_open_columns = [col for col in monthly_df.columns if 'open' in col]
                only_open_df = monthly_df[all_open_columns]
                monthly_df['open'] = only_open_df.bfill(axis=1).iloc[:, 0]  # Use the last open of the week

                all_high_columns = [col for col in monthly_df.columns if 'high' in col]
                monthly_df['weekly_high'] = monthly_df[all_high_columns].max(axis=1)
                
                all_low_columns = [col for col in monthly_df.columns if 'low' in col]
                monthly_df['weekly_low'] = monthly_df[all_low_columns].min(axis=1)

                all_close_columns = [col for col in monthly_df.columns if 'close' in col]

                monthly_df['close'] = monthly_df[all_close_columns[-1]]  # Use the last close of the week
                only_close_df = monthly_df[all_close_columns]
                monthly_df['close'] = only_close_df.ffill(axis=1).iloc[:, -1]  # Use the last close of the week

                drop_columns = [col for col in monthly_df.columns if col not in ['nikkei', 'ticker', 'jp', 'open', 'weekly_high', 'weekly_low', 'close']]
                monthly_df.drop(columns=drop_columns, inplace=True)

                monthly_df = monthly_df[['nikkei', 'ticker', 'jp', 'open', 'weekly_high', 'weekly_low', 'close']]

                monthly_df.to_csv(
                    dst_dir_path / f'monthly_expansed_technical_{year}_{previous_month}.csv',
                    index=False
                )
                monthly_df = pd.DataFrame()

                daily_df.columns = ['nikkei', 'ticker', 'jp', f'open_{day}', f'high_{day}', f'low_{day}', f'close_{day}']
                df_subset = daily_df.iloc[:, 0:7]
                monthly_df = pd.concat([monthly_df, df_subset], axis=1)
                previous_month = month
            else:
                daily_df.columns = ['nikkei', 'ticker', 'jp', f'open_{day}', f'high_{day}', f'low_{day}', f'close_{day}']
                df_subset = daily_df.iloc[:, 3:7]
                monthly_df = pd.concat([monthly_df, df_subset], axis=1)


class fundamental:
    
    def create_daily_funda():
        dst_dir_path = Path('data/fundamental/only_finres')

        columns = pd.read_csv(Path('data/nfq/nfqcsv/main_nfqcsv/N0000001.csv')).columns

        for date in [csv.stem for csv in Path('data/expansed_technical/ampm_expansed_technical').rglob('.') if csv.is_file() and csv.suffix == '.csv']:
            print("\r", f'Creating empty fundamental_daily_{date}.csv...', end=' ')
            pd.DataFrame(columns=['nikkei', 'ticker', 'jp'] + columns[2:].to_list()).to_csv(
                dst_dir_path / f'fundamental_daily_{date}.csv', index=False
            )
        print('\nFinished creating empty daily fundamental files.')
    
    def fill_finres_dates_to_daily_funda():
        path = cons.path.fundamental_kessan_only_csvs
        funda_csv_path_list = sorted([fp for fp in Path(path).rglob('.') if fp.suffix == '.csv'])
        cf_table = pd.read_csv('data/tickers/result/4608_cf_table.csv')

        date_list = [csv.stem[18:26] for csv in Path('data/fundamental/only_finres').rglob('.') if csv.is_file() and csv.suffix == '.csv']

        for funda_csv_path in funda_csv_path_list:
            print("\r", f'Processing {funda_csv_path.name}...', end=' ')
            funda_df = pd.read_csv(funda_csv_path)
            nikkei_code = funda_csv_path.stem
            ticker, jp = cf_table[cf_table['nikkei'] == nikkei_code][['ticker', 'jp']].values[0]

            for _, row in funda_df.iterrows():
                date = row['決算発表日'].replace('/', '')
                if date in date_list:
                    print("\r", f'Filling data for nikkei {nikkei_code} on date {date}...', end=' ')
                    daily_funda_csv_path = Path('data/fundamental/only_finres') / f'fundamental_daily_{date}.csv'
                    daily_funda_df = pd.read_csv(daily_funda_csv_path)

                    # 新しい行作成
                    new_df = pd.DataFrame({
                        'nikkei': [nikkei_code],
                        'ticker': [ticker],
                        'jp': [jp]
                    })

                    # row の 2列目以降を DataFrame に変換して横結合
                    row_df = pd.DataFrame([row[2:].values], columns=row[2:].index)
                    new_df = pd.concat([new_df, row_df], axis=1, sort=False)

                    # daily_funda_df に追加
                    daily_funda_df = pd.concat([daily_funda_df, new_df], axis=0, ignore_index=True)

                    daily_funda_df.to_csv(daily_funda_csv_path, index=False)


# technical.get_monthly_data()

fundamental.fill_finres_dates_to_daily_funda()