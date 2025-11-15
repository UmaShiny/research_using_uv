from config import cons
import pandas as pd
import numpy as np
from pathlib import Path
import datetime
import os

import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)
# 1. add nikkei-code to index of ta-db

class tafa:

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
    
    def check_valid_weekly_dates():

        daily_technical_file = Path('data/main/expansion/technical/daily_technical')
        data = {'date': [], 'weekday': []}

        previous_weekday = 0
        week_reset_flag = False
        passed_weekdays = []
        for daily_technical_file in [fp for fp in daily_technical_file.rglob('.') if fp.suffix == '.csv']:
            print("\r", f'* Checking {daily_technical_file.name}...', end=' ')
            current_weekday = int(daily_technical_file.stem[-1])
            if current_weekday == 2 or (current_weekday in passed_weekdays):
                data['date'].append(daily_technical_file.stem[-10:-2])
                data['weekday'].append(current_weekday)
                week_reset_flag = False
                passed_weekdays = []
            else:
                passed_weekdays.append(current_weekday)
            previous_weekday = current_weekday
        # green color for finished message
        print('\n \033[92m= Finished checking technical files.\033[0m')

        ta_df = pd.DataFrame(data)
        ta_df['date'] = pd.to_datetime(ta_df['date'], format='%Y%m%d').dt.strftime('%Y/%m/%d')
        fa_df = pd.read_csv('docs/fundamental_range_weekly.csv')
        fa_df['date'] = pd.to_datetime(fa_df['date'], format='%Y/%m/%d').dt.strftime('%Y/%m/%d')

        merged_df = pd.merge(ta_df, fa_df, on='date', how='outer', suffixes=('_ta', '_fa'))

        ta_only_mask = merged_df['weekday_ta'].notna()
        fa_only_mask = merged_df['weekday_fa'].notna()
        print(f'Technical length: {len(merged_df[ta_only_mask]["date"].tolist())} dates')
        print(f'Fundamental length: {len(merged_df[fa_only_mask]["date"].tolist())} dates')

        merged_df.to_csv('docs/technical_fundamental_valid_weekly_date_check.csv', index=False)

    class technical:

        def expanse_dailydb_with_nikkei_code():
            nkc_tkc_map_csv = Path(cons.path.nkc_tkc_map_csv)
            nkc_tkc_map_df = pd.read_csv(nkc_tkc_map_csv, dtype=str).copy()
            delete_from_expansed_daily_data_df = pd.read_csv(cons.path.deleted_tickers_csv)
            
            daily_data_csv_dir = Path(cons.path.daily_data_csvs)
            daily_data_csv_path_list = [fp for fp in daily_data_csv_dir.rglob('.') if fp.suffix == '.csv']

            dst_dir_path = Path(cons.path.dst_expansed_data_csvs)

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
                tafa.test_missing_nikkei_codes(daily_data_csv_path)

            # ここで何か処理を追加することができます
        # helper function

        @staticmethod
        def ampm_to_daily():

            src_dir = Path('data/main/expansion/technical/extraction_empty_data')
            dst_dir = Path('data/main/expansion/technical/daily_technical_extra')

            for csv_file in src_dir.rglob('*.csv'):
                df = pd.read_csv(csv_file)

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

                year = csv_file.stem[0:4]
                month = csv_file.stem[4:6]
                day = csv_file.stem[6:8]

                weekday = datetime.date(int(year), int(month), int(day)).weekday()  # Monday is 0 and Sunday is 6

                df.to_csv(dst_dir / f'daily_expansed_technical_{csv_file.stem}_{weekday}.csv', index=False)
            return df

        # TODO
        def get_weekly_data():
            daily_expansed_data_csvs_dir = Path('data/main/expansion/technical/daily_technical')
            daily_expansed_data_csv_path_list = sorted([fp for fp in daily_expansed_data_csvs_dir.rglob('.') if fp.suffix == '.csv'])
            dst_dir_path = Path('data/main/expansion/technical/weekly_technical_2')

            weekly_df = pd.DataFrame()
            passed_weekdays = []
            cnt = 0

            for fp in daily_expansed_data_csv_path_list:
                print("\r", f'Processing {fp.name}...', end='')

                csv_date = fp.stem

                daily_df = pd.read_csv(fp)

                year = int(csv_date[25:29])
                month = int(csv_date[29:31])
                day = int(csv_date[31:33])

                date = datetime.date(year, month, day)
                weekday = date.weekday()  # Monday is 0 and Sunday is 6

                sep_days = pd.read_csv('docs/weekly_separated.csv')['date'].tolist()
                sep_days = [date.replace('/', '') for date in sep_days]

                if weekly_df.empty:  # If weekly_df is empty, initialize with nikkei, ticker, jp columns
                    weekly_df = daily_df.copy()

                if fp.stem[25:33] in sep_days:  # If Wednesday or a previously passed weekday: finalize and save the week's data
                    sep_days.remove(fp.stem[25:33])
                    print(f' (created No.{cnt} weekly file.)', end='')

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

            print('remaining separated days:', sep_days)
            return

        def get_weekly_data_by_wednesday():
            daily_expansed_data_csvs_dir = Path('data/main/expansion/technical/daily_technical')
            daily_expansed_data_csv_path_list = sorted([fp for fp in daily_expansed_data_csvs_dir.rglob('.') if fp.suffix == '.csv'])
            dst_dir = Path('data/main/expansion/technical/weekly_technical_by_wednesday')

            sep_days = [date.replace('/', '') for date in pd.read_csv('docs/weekly_separated.csv')['date'].tolist() if isinstance(date, str)]

            weekly_df = pd.DataFrame()
            cnt = 0

            for fp in daily_expansed_data_csv_path_list:
                print("\r", f'Processing {fp.name}...', end=' ')

                daily_df = pd.read_csv(fp)

                if fp.stem[25:33] in sep_days:
                    sep_days.remove(fp.stem[25:33])

                    weekly_df = daily_df.copy()

                    weekly_df.columns = ['nikkei', 'ticker', 'jp', 'open', 'weekly_high', 'weekly_low', 'close']

                    weekly_df.to_csv(
                        dst_dir / f'TradeRecord_by_wed_{cnt}.csv',
                        index=False
                    )

                    print(f'created No.{cnt} weekly file.', end=' ')
                    cnt += 1


            print('remaining separated days:', sep_days)
            return

        def get_monthly_data():
            src_dir_path = Path('data/main/expansion/technical/daily_technical')
            dst_dir_path = Path('data/main/master/product/monthly_technical')

            src_dir = Path(src_dir_path)
            dst_dir = Path(dst_dir_path)
            
            daily_fp = sorted([fp for fp in src_dir.rglob('.') if fp.suffix == '.csv'])
            month_num = 0
            cnt = 0
            for i, fp in enumerate(daily_fp):
                print("\r", f'Processing {fp.name}... ({i + 1}/{len(daily_fp)})', end=' ')
                if int(fp.stem[4:6]) != month_num:
                    print(f'Creating monthly file for month {fp.stem[4:6]}...', end=' ')
                    month_num = int(fp.stem[4:6])
                    print(f'write on {dst_dir / f"{fp.stem[0:4]}_{month_num:02d}_No{cnt}.csv"}', end=' ')
                    pd.read_csv(fp).to_csv(
                        dst_dir / f'{fp.stem[0:4]}_{month_num:02d}_No{cnt}.csv', index=False
                    )
                    cnt += 1
            return

        # TODO
        def get_quarterly_data():
            pass

        def data_create_operation():
            pass

    class fundamental:

        def __init__(self, original_name='default', 
                     nfq_csv_dir='', 
                     etc_flag=False, 
                     mkdir_flag=False):
            todo_0 = ''
            todo_1 = ''
            todo_2 = ''
            todo_3 = ''
            todo_4 = ''
            todo_5 = ''
            todo_6 = ''
            todo_7 = ''
            todo_8 = ''
            todo_9 = ''
            todo_10 = ''
            while todo_0 not in ['y', 'n']:
                todo_0 = input('- 0: 日付分のファンダメンタルズファイルを作成しますか？ [y/n]: ')
                if todo_0 == 'y':
                    self.todo_0 = True
                else:
                    self.todo_0 = False
            while todo_1 not in ['y', 'n']:
                todo_1 = input('- 1: ファンダメンタルズデータを書き込みますか？ [y/n]: ')
                if todo_1 == 'y':
                    self.todo_1 = True
                else:
                    self.todo_1 = False
            while todo_2 not in ['y', 'n']:
                todo_2 = input('- 2: すべてのデータを平均値でNaN値埋めしますか？（非推奨） [y/n]: ')
                if todo_2 == 'y':
                    self.todo_2 = True
                else:
                    self.todo_2 = False
            while todo_3 not in ['y', 'n']:
                todo_3 = input('- 3: 全日経コードでファンダメンタルズファイルを拡張しますか？ [y/n]: ')
                if todo_3 == 'y':
                    self.todo_3 = True
                else:
                    self.todo_3 = False
            while todo_4 not in ['y', 'n']:
                todo_4 = input('- 4: ファイル間でデータの補完を行いますか？ [y/n]: ')
                if todo_4 == 'y':
                    self.todo_4 = True
                else:
                    self.todo_4 = False
            while todo_5 not in ['y', 'n']:
                todo_5 = input('- 5: 不可売買日を含むデータを削除しますか？ [y/n]: ')
                if todo_5 == 'y':
                    self.todo_5 = True
                else:
                    self.todo_5 = False
            while todo_6 not in ['y', 'n']:
                todo_6 = input('- 6: 欠損値をクロスセクショナル平均で補完しますか？（非推奨） [y/n]: ')
                if todo_6 == 'y':
                    self.todo_6 = True
                else:
                    self.todo_6 = False
            while todo_7 not in ['y', 'n']:
                todo_7 = input('- 7: ファンダメンタルズデータを週次に変換しますか？ [y/n]: ')
                if todo_7 == 'y':
                    self.todo_7 = True
                else:
                    self.todo_7 = False
            while todo_8 not in ['y', 'n']:
                todo_8 = input('- 8: ファンダメンタルズデータを月次に変換しますか？ [y/n]: ')
                if todo_8 == 'y':
                    self.todo_8 = True
                else:
                    self.todo_8 = False
            while todo_9 not in ['y', 'n']:
                todo_9 = input('- 9: 週次データを一つにまとめますか？ [y/n]: ')
                if todo_9 == 'y':
                    self.todo_9 = True
                else:
                    self.todo_9 = False
            while todo_10 not in ['y', 'n']:
                todo_10 = input('- 10: 月次データを一つにまとめますか？ [y/n]: ')
                if todo_10 == 'y':
                    self.todo_10 = True
                else:
                    self.todo_10 = False
            if original_name != '':
                original_name = original_name + '_'
            self.original_name = original_name
            self.nfq_csv_dir = f'data/main/build/nfq/nfqcsv/{nfq_csv_dir}'
            self.origin_fundamental_dir = f'data/main/origin/{original_name}fundamental'
            self.weekly_save_dir = f'data/main/master/product/weekly_{original_name}fundamental'
            self.monthly_save_dir = f'data/main/master/product/monthly_{original_name}fundamental'
            self.merge_weekly_save_path = f'data/main/master/product/weekly_{original_name}fundamental_all.csv'
            self.merge_monthly_save_path = f'data/main/master/product/monthly_{original_name}fundamental_all.csv'
            self.etc_flag = etc_flag
            check_y = None
            # ディレクトリが存在する場合は，ファイル数を表示する
            print('+ directory settings:')
            # ファイルがある場合は赤
            # ファイルがない場合は緑
            if os.path.exists(self.origin_fundamental_dir):
                print(f' - origin     : {self.origin_fundamental_dir} \033[91m({len(os.listdir(self.origin_fundamental_dir))} files already exist)\033[0m')
            else:
                print(f' - origin     : {self.origin_fundamental_dir} \033[92m(not exist)\033[0m')
            if os.path.exists(self.weekly_save_dir):
                print(f' - weekly     : {self.weekly_save_dir} \033[91m({len(os.listdir(self.weekly_save_dir))} files already exist)\033[0m')
            else:
                print(f' - weekly     : {self.weekly_save_dir} \033[92m(not exist)\033[0m')
            if os.path.exists(self.monthly_save_dir):
                print(f' - monthly    : {self.monthly_save_dir} \033[91m({len(os.listdir(self.monthly_save_dir))} files already exist)\033[0m')
            else:
                print(f' - monthly    : {self.monthly_save_dir} \033[92m(not exist)\033[0m')
            print('+ flag settings:')
            print(f' - etc_flag   : \033[92m{self.etc_flag}\033[0m')
            print(f' - mkdir_flag : \033[92m{mkdir_flag}\033[0m')
            while check_y not in ['y', 'n']:
                check_y = input(f'Are you sure to set fundamental directories with the original name "{original_name}"? (y/n): ')
            if mkdir_flag and check_y == 'y':
                os.makedirs(self.origin_fundamental_dir, exist_ok=True)
                os.makedirs(self.weekly_save_dir, exist_ok=True)
                os.makedirs(self.monthly_save_dir, exist_ok=True)
            if check_y == 'n':
                print('Process aborted by user.')

        class fundamental_core:
            cf_table_path = 'data/tickers/util_csv/nktk_cross_reference_rule.csv'
            process_finished_message = '\n \033[92m [ok] Finished processing fundamental files.\033[0m'
            process_skipped_message = '\033[93m [__] this process was skipped.\033[0m'

            def create_daily_funda_core(dst_path, have_same_columns_dir_path):
                CALENDER = 'data/main/expansion/technical/ampm_technical'
                dst_dir_path = Path(dst_path)
                columns = pd.read_csv(Path(f'{have_same_columns_dir_path}/N0000001.csv')).columns
                csv_list = [csv for csv in Path(CALENDER).rglob('.') if csv.is_file() and csv.suffix == '.csv']
                proccess_length = len(csv_list)
                for i, date in enumerate([csv.stem for csv in csv_list]):
                    print("\r", f'Creating empty {date}.csv... ({i+1}/{proccess_length})', end=' ')
                    # print("\r", f'Creating empty {date}.csv...', end=' ')
                    print(f'write on {dst_dir_path / f"{date}.csv"}', end=' ')
                    pd.DataFrame(columns=['nikkei', 'ticker', 'jp'] + columns[2:].to_list()).to_csv(
                        dst_dir_path / f'{date}.csv', index=False
                )
                # print('\nFinished creating empty daily fundamental files.')
                print(tafa.fundamental.fundamental_core.process_finished_message)
        
            def fill_finres_dates_to_daily_funda_core(src_dir_path, dst_path):
                CALENDER = 'data/main/expansion/technical/ampm_technical'
                cf_table = pd.read_csv(tafa.fundamental.fundamental_core.cf_table_path)
                funda_csv_path_list = sorted([fp for fp in Path(src_dir_path).rglob('.') if fp.suffix == '.csv'])
                date_list = [csv.stem for csv in Path(CALENDER).rglob('.') if csv.is_file() and csv.suffix == '.csv']

                for i, funda_csv_path in enumerate(funda_csv_path_list):
                    print("\r", f'Processing {funda_csv_path.name}... ({i+1}/{len(funda_csv_path_list)})', end=' ')
                    funda_df = pd.read_csv(funda_csv_path)
                    nikkei_code = funda_csv_path.stem
                    ticker, jp = cf_table[cf_table['nikkei'] == nikkei_code][['ticker', 'jp']].values[0]

                    for _, row in funda_df.iterrows():
                        date = row['決算発表日'].replace('-', '').replace('/', '')
                        if date in date_list:
                            # print(f'Filling data for nikkei {nikkei_code} on date {date}...', end=' ')
                            daily_funda_csv_path = Path(dst_path) / f'{date}.csv'
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

                            # print(f'write on {daily_funda_csv_path}', end=' ')
                            daily_funda_df.to_csv(daily_funda_csv_path, index=False)
                print(tafa.fundamental.fundamental_core.process_finished_message)
                return

            def fill_all_files_core(src_dir):
                dst_dir_path = Path(src_dir)
                funda_csv_path_list = sorted([fp for fp in Path(src_dir).rglob('.') if fp.suffix == '.csv'])

                for i, funda_csv_path in enumerate(funda_csv_path_list):
                    print("\r", f'Filling data for {funda_csv_path.name}... ({i+1}/{len(funda_csv_path_list)})', end=' ')
                    funda_df = pd.read_csv(funda_csv_path)

                    # 前方参照で欠損値を埋める
                    funda_df_ffilled = funda_df.copy()
                    funda_df_ffilled.iloc[:, 2:] = funda_df_ffilled.iloc[:, 2:].ffill()

                    # それでも埋まらない欠損値は平均値で埋める
                    funda_df_ffilled.iloc[:, 2:] = funda_df_ffilled.iloc[:, 2:].fillna(funda_df_ffilled.iloc[:, 2:].mean())

                    print(f'write on {dst_dir_path / funda_csv_path.name}', end=' ')
                    funda_df_ffilled.to_csv(dst_dir_path / funda_csv_path.name, index=False)
            

                print(tafa.fundamental.fundamental_core.process_finished_message)
                return 

            def expanse_dailydb_with_nikkei_code_core(src_dir_path):
                src_dir_path = Path(src_dir_path)
                dst_dir_path = Path(src_dir_path)
                nkc_tkc_map_csv = Path(tafa.fundamental.fundamental_core.cf_table_path)
                nkc_tkc_map_df = pd.read_csv(nkc_tkc_map_csv).copy()
                daily_data_csv_path_list = [fp for fp in Path(src_dir_path).rglob('.') if fp.suffix == '.csv']
                for daily_data_csv_path in daily_data_csv_path_list:

                    print("\r", f'Processing {daily_data_csv_path.name}...', end=' ')

                    daily_data_df = pd.read_csv(daily_data_csv_path)

                    # nikkeiコードとtickerコードのデータ型をstr型に変換する
                    nkc_tkc_map_df['ticker'] = nkc_tkc_map_df['ticker'].astype(str)
                    daily_data_df[daily_data_df.columns[1]] = daily_data_df[daily_data_df.columns[1]].astype(str)

                    # nkc_tkc_map_df.set_index(['nikkei', 'ticker', 'jp'], inplace=True)

                    # 結合することで，一つの大きなデータフレームにする
                    expansed_daily_data_df = daily_data_df.merge(
                        nkc_tkc_map_df.copy(),
                        how='outer',
                        left_on=['nikkei', 'ticker', 'jp'],
                        right_on=['nikkei', 'ticker', 'jp'],
                    )
                    
                    print(f'write on {dst_dir_path / daily_data_csv_path.name}', end=' ')
                    expansed_daily_data_df.to_csv(
                        dst_dir_path / daily_data_csv_path.name,
                        index=False
                    )
                print(tafa.fundamental.fundamental_core.process_finished_message)
                return 

            def complement_missing_fundamental_data_core(src_dir_path):
                fp_list = [fp for fp in Path(src_dir_path).rglob('.') if fp.suffix == '.csv']
                proccess_length = len(fp_list)
                while fp_list[:-1]:
                    current_file_path = fp_list.pop(0)
                    next_file_path = fp_list[0]
                    print("\r", f'Complementing data from {current_file_path.name} to {next_file_path.name}...({len(fp_list[:-1])}/{proccess_length})', end=' ')
                    current_df = pd.read_csv(current_file_path)
                    next_df = pd.read_csv(next_file_path)
                    unvalid_length = current_df.iloc[:, 3:].isnull().all(axis=1).sum()
                    print(f'valid data length: {unvalid_length}', end=' ')
                    merge_mask = ~current_df.iloc[:, 3:].isnull().all(axis=1) & next_df.iloc[:, 3:].isnull().all(axis=1)
                    next_df.loc[merge_mask, next_df.columns[3:]] = current_df.loc[merge_mask, current_df.columns[3:]]
                    print(f'write on {next_file_path}', end=' ')
                    next_df.to_csv(next_file_path, index=False)
                print(tafa.fundamental.fundamental_core.process_finished_message)
                return

            def delete_data_with_untradable_date_core(src_dir_path):
                daily_trade_dir = Path('data/main/origin/technical') # data\main\origin\technical
                daily_funda_dir = Path(src_dir_path)

                all_approved_tickers = pd.read_csv(tafa.fundamental.fundamental_core.cf_table_path)['ticker']
                all_len = len([fp for fp in daily_trade_dir.rglob('.') if fp.suffix == '.csv'][1:])

                for i, (ta_path, fa_path) in enumerate(zip(
                    sorted([fp for fp in daily_trade_dir.rglob('.') if fp.suffix == '.csv'][1:]),
                    sorted([fp for fp in daily_funda_dir.rglob('.') if fp.suffix == '.csv'])
                )):
                    print("\r", f'Processing {ta_path.name} and {fa_path.name}...({i+1}/{all_len})', end=' ')
                    ta_df = pd.read_csv(ta_path)
                    tmp_fa_df = pd.read_csv(fa_path)

                    fa_df = tmp_fa_df.copy()

                    valid_ticker_codes = ta_df[ta_df.columns[1]][ta_df[ta_df.columns[1]].isin(all_approved_tickers)].tolist()

                    # もしtickerが存在しない場合，取引が不可能なため，fundamentalデータは消去されなくてはならない
                    delete_mask = ~fa_df[fa_df.columns[1]].isin(valid_ticker_codes)

                    fa_df.loc[delete_mask, fa_df.columns[3:]] = np.nan

                    # """
                    print(f'write on {daily_funda_dir / fa_path.name}', end=' ')
                    fa_df.to_csv(
                        daily_funda_dir / fa_path.name,
                        index=False
                    )
                    # """

                    tmp_fa_mask = ~tmp_fa_df[tmp_fa_df.columns[3:]].isnull().all(axis=1)
                    fa_mask = ~fa_df[fa_df.columns[3:]].isnull().all(axis=1)
                    ta_in_fa_mask = ta_df[ta_df.columns[1]].isin(fa_df[fa_df.columns[1]])

                    length_fa_df = len(fa_df[tmp_fa_mask])
                    length_fa_df_after = len(fa_df[fa_mask])
                    length_ta_in_fa = len(ta_df[ta_in_fa_mask])

                    # 数字は緑で表示
                    if len(set(ta_df[ta_in_fa_mask][ta_df.columns[1]])) < len(set(fa_df[fa_mask]['ticker'])):

                        fa_df_after_tickers = set(fa_df[fa_mask][fa_df.columns[1]])
                        ta_df_tickers = set(ta_df[ta_in_fa_mask][ta_df.columns[1]])
                        print(fa_df_after_tickers - ta_df_tickers)

                        raise ValueError('Error: Valid data length increased after deletion, which should not happen.')
                    print(f'Valid data length: \033[92m{length_fa_df} -> {length_fa_df_after}\033[0m ({length_ta_in_fa})', end='')
                
                print(tafa.fundamental.fundamental_core.process_finished_message)
                return

            def impute_missing_by_cross_sectional_mean_core(src_dir_path):
                src_ta_dir_path = 'data/main/expansion/technical/ampm_technical'
                all_approved_tickers = pd.read_csv(Path(tafa.fundamental.fundamental_core.cf_table_path))['ticker']
                src_fa_fp_list = sorted([fp for fp in Path(src_dir_path).rglob('.') if fp.suffix == '.csv'])[1:]
                src_ta_fp_list = sorted([fp for fp in Path(src_ta_dir_path).rglob('.') if fp.suffix == '.csv'])
                process_length = len(src_fa_fp_list)
                for i, (ta_path, fa_path) in enumerate(zip(
                    src_ta_fp_list,
                    src_fa_fp_list,
                )):
                    print("\r", f'Processing {ta_path.name} and {fa_path.name}...({i+1}/{process_length})', end=' ')
                    ta_df = pd.read_csv(ta_path)
                    fa_df = pd.read_csv(fa_path)

                    valid_ticker_mask = ta_df[ta_df.columns[1]].isin(all_approved_tickers)
                    valid_ticker_codes = ta_df[ta_df.columns[1]][valid_ticker_mask].tolist()

                    # Check if the ticker codes are valid and create a mask for valid fundamental data
                    valid_fa_mask = fa_df[fa_df.columns[1]].isin(valid_ticker_codes)
                    valid_fa_df = fa_df[valid_fa_mask].copy()
                    impute_mask = valid_fa_df[valid_fa_df.columns[3:]].isnull().all(axis=1)

                    # Calculate cross-sectional mean and impute missing values
                    cs_mean_series = valid_fa_df.loc[~impute_mask, valid_fa_df.columns[3:]].mean()
                    valid_fa_df.loc[impute_mask, valid_fa_df.columns[3:]] = cs_mean_series.values
                    fa_df.loc[valid_fa_mask, fa_df.columns[3:]] = valid_fa_df.loc[:, valid_fa_df.columns[3:]]

                    # Check if the imputation was successful
                    fa_usable_mask = ~fa_df[fa_df.columns[3:]].isnull().all(axis=1)
                    length_total_valid_fa_df = len(set(fa_df[fa_usable_mask]['ticker']))
                    length_total_valid_ta_df = len(set(valid_ticker_codes))

                    there_is_no_data  = length_total_valid_fa_df == 0
                    imputed_perfectly = length_total_valid_fa_df == length_total_valid_ta_df

                    if imputed_perfectly or there_is_no_data:
                        print(f'Imputed data length: \033[92m{impute_mask.sum()}\033[0m, valid_ta_df_length : {len(valid_ticker_codes)}, valid_fa_df_length : {len(valid_fa_df)}, ', end='   ')

                        print(f'write on {fa_path}', end=' ')
                        fa_df.to_csv(
                            fa_path,
                            index=False
                        )

                    else:
                        raise ValueError('Error: Valid data length after imputation does not match valid ticker codes length.')

                print(tafa.fundamental.fundamental_core.process_finished_message)
                return

            def get_weekly_data_core(src_dir_path, dst_dir_path):
                sep_days = pd.read_csv('./scripts/merge_series_tafa/weekly_separated.csv')['date'].tolist()
                sep_days = [date.replace('/', '') for date in sep_days]

                daily_files = sorted(
                    [fp for fp in Path(src_dir_path).rglob('.') if fp.suffix == '.csv']
                )
                cnt = 0
                for i, fp in enumerate(daily_files):
                    print("\r", f'Processing {fp.name}... ({i + 1}/{len(daily_files)})', end=' ')

                    daily_df = pd.read_csv(fp)

                    if fp.stem[0:8] in sep_days:
                        sep_days.remove(fp.stem[0:8])

                        weekly_df = daily_df.copy()

                        print(f'write on {Path(dst_dir_path) / f"weekly_No{cnt}.csv"}', end=' ')
                        weekly_df.to_csv(
                            Path(dst_dir_path) / f'weekly_No{cnt}.csv',
                            index=False
                        )

                        print(f'created No.{cnt} weekly file.', end=' ')
                        cnt += 1

                print(tafa.fundamental.fundamental_core.process_finished_message)
                return

            def get_monthly_data_core(src_dir_path, dst_dir_path):
                src_dir = Path(src_dir_path)
                dst_dir = Path(dst_dir_path)
                
                daily_fp = [fp for fp in src_dir.rglob('.') if fp.suffix == '.csv']
                month_num = 0
                cnt = 0
                for i, fp in enumerate(daily_fp):
                    print("\r", f'Processing {fp.name}... ({i + 1}/{len(daily_fp)})', end=' ')
                    if int(fp.stem[4:6]) != month_num:
                        print(f'Creating monthly file for month {fp.stem[4:6]}...', end=' ')
                        month_num = int(fp.stem[4:6])
                        print(f'write on {dst_dir / f"{fp.stem[0:4]}_{month_num:02d}_No{cnt}.csv"}', end=' ')
                        pd.read_csv(fp).to_csv(
                            dst_dir / f'{fp.stem[0:4]}_{month_num:02d}_No{cnt}.csv', index=False
                        )
                        cnt += 1
                print(tafa.fundamental.fundamental_core.process_finished_message)
                return

            def merge_all_core(src_dir_path, dst_dir_path, frequency=''):
                tr_csv = pd.read_csv(Path('data/main/master/product/weekly_TR(wed)_Tech.csv'))
                invalid_mask = ~tr_csv.iloc[:, 2:].notnull().all(axis=1)

                freq_id_name = ''
                if frequency == '':
                    frequency = 'unknown frequency'
                    print('Frequency not specified, set to "unknown frequency".')
                    return
                if frequency == 'w':
                    id_start_idx = 9
                    freq_id_name = 'week'
                if frequency == 'm':
                    id_start_idx = 10
                    freq_id_name = 'month'
                if frequency == 'q':
                    print('Quarterly merging not implemented yet.')
                    return
                
                src_csv_fps = sorted([fp for fp in Path(src_dir_path).rglob('.') if fp.suffix == '.csv'], key=lambda x: int(x.stem[id_start_idx:]))

                all_finrep_df = pd.DataFrame()

                for i, finrep_fp in enumerate(src_csv_fps):
                    print('\r', f'Merging {freq_id_name} ID {finrep_fp.stem[id_start_idx:]} ({i+1}/{len(src_csv_fps)}) ... ', end='     ')
                    finrep_df = pd.read_csv(finrep_fp)
                    finrep_df[f'{freq_id_name}_id'] = finrep_fp.stem[id_start_idx:]
                    all_finrep_df = pd.concat([all_finrep_df, finrep_df], ignore_index=True, axis=0)

                print('\nAll fundamental csv merged.')
                all_finrep_df = all_finrep_df[['nikkei', f'{freq_id_name}_id'] + [c for c in all_finrep_df.columns if c not in ['nikkei', f'{freq_id_name}_id', 'ticker', 'jp']]]
                all_finrep_df.iloc[invalid_mask, 2:] = np.nan
                print('Invalid rows set to NaN.')

                output_fp = Path(dst_dir_path)
                all_finrep_df.to_csv(output_fp, index=False)

        def create_daily_funda(self):
            print('+ Creating daily fundamental files...')
            if self.todo_0 == False:
                print(tafa.fundamental.fundamental_core.process_skipped_message)
                return
            dst_dir_path = self.origin_fundamental_dir
            have_same_columns_dir_path = self.nfq_csv_dir
            tafa.fundamental.fundamental_core.create_daily_funda_core(
                dst_dir_path,
                have_same_columns_dir_path,
            )
        
        def fill_finres_dates_to_daily_funda(self):
            print('+ Filling fundamental data into daily fundamental files...')
            if self.todo_1 == False:
                print(tafa.fundamental.fundamental_core.process_skipped_message)
                return
            fundamental_csv_dir_path = self.nfq_csv_dir
            origin_dir_name = self.origin_fundamental_dir

            tafa.fundamental.fundamental_core.fill_finres_dates_to_daily_funda_core(
                fundamental_csv_dir_path,
                origin_dir_name
            )

        def fill_all_files(self):
            print('+ Filling all fundamental files with forward fill and mean imputation...')
            if self.etc_flag == False:
                print(tafa.fundamental.fundamental_core.process_skipped_message)
                return
            if self.todo_2 == False:
                print(tafa.fundamental.fundamental_core.process_skipped_message)
                return
            src_dir = self.nfq_csv_dir
            tafa.fundamental.fundamental_core.fill_all_files_core(
                src_dir,
            )

        def expanse_dailydb_with_nikkei_code(self):
            print('+ Expanding daily fundamental files with all Nikkei codes...')
            if self.todo_3 == False:
                print(tafa.fundamental.fundamental_core.process_skipped_message)
                return
            src_dir_path = self.origin_fundamental_dir

            tafa.fundamental.fundamental_core.expanse_dailydb_with_nikkei_code_core(
                src_dir_path

            )

        def complement_missing_fundamental_data(self):
            print('+ Complementing missing fundamental data between files...')
            if self.todo_4 == False:
                print(tafa.fundamental.fundamental_core.process_skipped_message)
                return
            src_dir_path = self.origin_fundamental_dir

            tafa.fundamental.fundamental_core.complement_missing_fundamental_data_core(
                src_dir_path
            )

        def delete_data_with_untradable_date(self):
            print('+ Deleting data with untradable dates...')
            if self.todo_5 == False:
                print(tafa.fundamental.fundamental_core.process_skipped_message)
                return
            src_dir_path = self.origin_fundamental_dir

            tafa.fundamental.fundamental_core.delete_data_with_untradable_date_core(
                src_dir_path
            )

        def impute_missing_by_cross_sectional_mean(self):
            print('+ Imputing missing fundamental data by cross-sectional mean...')
            if self.etc_flag == False:
                print(tafa.fundamental.fundamental_core.process_skipped_message)
                return
            if self.todo_6 == False:
                print(tafa.fundamental.fundamental_core.process_skipped_message)
                return
            src_dir_path = self.origin_fundamental_dir

            tafa.fundamental.fundamental_core.impute_missing_by_cross_sectional_mean_core(
                src_dir_path
            )

        def get_weekly_data(self):
            print('+ Converting fundamental data to weekly frequency...')
            if self.todo_7 == False:
                print(tafa.fundamental.fundamental_core.process_skipped_message)
                return
            src_dir = self.origin_fundamental_dir
            dst_dir = self.weekly_save_dir

            tafa.fundamental.fundamental_core.get_weekly_data_core(
                src_dir_path=src_dir,
                dst_dir_path=dst_dir
            )

        def get_monthly_data(self):
            print('+ Converting fundamental data to monthly frequency...')
            if self.todo_8 == False:
                print(tafa.fundamental.fundamental_core.process_skipped_message)
                return
            src_dir = self.origin_fundamental_dir
            dst_dir = self.monthly_save_dir

            tafa.fundamental.fundamental_core.get_monthly_data_core(
                src_dir_path=str(src_dir),
                dst_dir_path=str(dst_dir)
            )

        def clean_dup(self):
            print('+ Cleaning duplicate entries in fundamental data...')
            file_cnt = 0
            for fp in [fp for fp in Path(self.origin_fundamental_dir).rglob('.') if fp.suffix == '.csv']:
                print('\r', f'Processing {fp.name}...', end=' ')
                df = pd.read_csv(fp)
                print(f'Original length: {len(df)}', end=' ')
                df_cleaned = df.drop_duplicates(subset=df.columns[:3], keep='last')
                print(f'Cleaned length: {len(df_cleaned)}', end=' ')
                df_cleaned.to_csv(fp, index=False)
                print(f'Dropped {len(df) - len(df_cleaned)} duplicates.', end=' ')
                if len(df) - len(df_cleaned) > 0:
                    file_cnt += 1
            print(f'\n\033[32mFinished cleaning duplicates in {file_cnt} files.\033[0m')
        
        # TODO
        def get_quarterly_data(self):
            src_dir = Path('data/main/expansion/fundamental/financial_report/daily_FinancialReport')
            dst_dir = Path('data/main/expansion/fundamental/financial_report/quarterly_FinancialReport')
            pass

        def merge_all(self):
            print('+ Merging all fundamental data...')
            if self.todo_9 == False:
                print(tafa.fundamental.fundamental_core.process_skipped_message)
            else:
                src_dir_path = self.weekly_save_dir
                dst_dir_path = self.merge_weekly_save_path
                tafa.fundamental.fundamental_core.merge_all_core(
                    src_dir_path=src_dir_path,
                    dst_dir_path=dst_dir_path,
                    frequency='w'
                )
            if self.todo_10 == False:
                print(tafa.fundamental.fundamental_core.process_skipped_message)
            else:
                src_dir_path = self.monthly_save_dir
                dst_dir_path = self.merge_monthly_save_path
                tafa.fundamental.fundamental_core.merge_all_core(
                    src_dir_path=src_dir_path, 
                    dst_dir_path=dst_dir_path,
                    frequency='m'
                )

        def data_create_operation(self, timeframe=''):
            tafa.fundamental.create_daily_funda(self)
            tafa.fundamental.fill_finres_dates_to_daily_funda(self)
            tafa.fundamental.fill_all_files(self)
            tafa.fundamental.expanse_dailydb_with_nikkei_code(self)
            tafa.fundamental.complement_missing_fundamental_data(self)
            tafa.fundamental.delete_data_with_untradable_date(self)
            tafa.fundamental.impute_missing_by_cross_sectional_mean(self)
            tafa.fundamental.clean_dup(self)
            if 'w' in timeframe:
                tafa.fundamental.get_weekly_data(self)
                print('\033[32mWeekly data processing is done.\033[0m')
                timeframe = timeframe.replace('w', '')
            if 'm' in timeframe:
                tafa.fundamental.get_monthly_data(self)
                print('\033[32mMonthly data processing is done.\033[0m')
                timeframe = timeframe.replace('m', '')
            if 'd' in timeframe:
                print('\033[32mDaily data processing is done.\033[0m')
                timeframe = timeframe.replace('d', '')
            if 'q' in timeframe:
                # 青色で表示
                print('\033[34mQuarterly data processing is not yet implemented.\033[0m')
                timeframe = timeframe.replace('q', '')
            if timeframe != '':
                # 赤色で表示
                print('\033[31mPlease specify a valid timeframe: d (daily), w (weekly), m (monthly), q (quarterly).\033[0m')
            else:
                # 緑で表示
                print('\033[32mthis process is finished.\033[0m')
            tafa.fundamental.merge_all(self)
            return

# execution area

if __name__ == '__main__':
    contorller = None
    while contorller not in ['f', 't']:
        contorller = input('fundamental or technical? [f/t]: ')
        if contorller == 'f':
            funda = tafa.fundamental(
                original_name='forbeta',
                nfq_csv_dir='stcvol_delmissing_nfqcsv',
                etc_flag=True,
                mkdir_flag=True 
            )
        elif contorller == 't':
            tech = tafa.technical(
                original_name='remake',
                mkdir_flag=True
            )
        else:
            raise ValueError('Please input "f" or "t".')
    if contorller == 'f':
        funda.data_create_operation(timeframe='wm')
    elif contorller == 't':
        tech.data_create_operation(timeframe='wm')