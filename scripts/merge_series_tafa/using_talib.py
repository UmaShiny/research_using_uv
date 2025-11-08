import talib
import numpy as np
import pandas as pd
from pathlib import Path
from datetime import datetime

def calculate_technical_indicators():

    src_weekly_dir = Path('data/main/expansion/technical/weekly_technical_by_wednesday')
    nk_reference_fp = Path('data/tickers/util_csv/nktk_cross_reference_rule.csv')

    all_nikkei:list[str] = pd.read_csv(nk_reference_fp)['nikkei'].tolist()

    csv_fps = [fp for fp in src_weekly_dir.rglob('.') if fp.suffix == '.csv']
    csv_fps.sort(key=lambda x: int(x.stem[19:]))  # Sort by week_id

    dfs = []
    for i, csv_fp in enumerate(csv_fps):
        print('\r', f'Calculating technical indicators for {csv_fp.stem} ({i+1}/{len(csv_fps)}) ... ', end='')
        df = pd.read_csv(csv_fp)
        # df['date'] = datetime.strptime(csv_fp.stem[25:33], '%Y%m%d').strftime('%Y/%m/%d')
        df['week_id'] = csv_fp.stem[19:]
        cols = ["week_id"] + [c for c in df.columns if c != "week_id"]
        df = df[cols]
        dfs.append(df)
    print('\nAll files loaded.')

    big_TradeRecord_df = pd.concat(dfs, ignore_index=True, axis=0).set_index(['nikkei', 'week_id']).reset_index()

    # Initialize columns for technical indicators
    big_TradeRecord_df[['SMA_5', 'SMA_15', 'SMA_40']] = np.nan
    big_TradeRecord_df[['RSI_26', 'RSI_14', 'RSI_9']] = np.nan
    big_TradeRecord_df[['MACD', 'MACD_signal', 'MACD_hist']] = np.nan
    big_TradeRecord_df[['STC_fk', 'STC_fd']] = np.nan
    big_TradeRecord_df[['MOM_10']] = np.nan
    big_TradeRecord_df[['BB2U', 'BB1U', 'BB1L', 'BB2L']] = np.nan

    for i, nikkei in enumerate(all_nikkei):
        print('\r', f'Calculating technical indicators for {nikkei} ({i+1}/{len(all_nikkei)}) ... ', end='')
        nikkei_mask = big_TradeRecord_df['nikkei'] == nikkei

        the_df = big_TradeRecord_df[nikkei_mask]
        
        null_mask = the_df['close'].notnull()
        head_bool = null_mask.iloc[0]
        lagged_null_mask = np.insert(null_mask, 0, not head_bool)[:-1]

        separate_mask = ((null_mask == True) & (lagged_null_mask == False)) | ((null_mask == False) & (lagged_null_mask == True))

        df_separate_index = the_df[separate_mask].index.to_list()

        separate_tuple = [(idx, sep_bool) for idx, sep_bool in zip(df_separate_index, separate_mask[separate_mask == True])] + [(the_df.index[-1]+1, not null_mask.iloc[-1])]

        the_df_partial_list = []
        if len(separate_tuple) != 1:
            sep_idx_list = []
            
            if null_mask.iloc[0] == False:
                sep_idx_list = [(start_idx, end_idx) for start_idx, end_idx in zip(separate_tuple[:-1], separate_tuple[1:])][1::2]
            else:
                sep_idx_list = [(start_idx, end_idx) for start_idx, end_idx in zip(separate_tuple[:-1], separate_tuple[1:])][0::2]

            the_df_partial_list = [
                big_TradeRecord_df.iloc[start_idx[0]:end_idx[0]][nikkei_mask.iloc[start_idx[0]:end_idx[0]]]
                for start_idx, end_idx in sep_idx_list
            ]

        else:
            the_df_partial_list = [(big_TradeRecord_df[nikkei_mask & null_mask], 0, len(big_TradeRecord_df))]

        for the_df_partial in the_df_partial_list:

            nikkei_df = the_df_partial.copy()

            close_prices = nikkei_df['close'].values
            high_prices = nikkei_df['weekly_high'].values
            low_prices = nikkei_df['weekly_low'].values

            nikkei_df['SMA_5'] = talib.SMA(close_prices, timeperiod=5)      # nearly equal to 25D
            nikkei_df['SMA_15'] = talib.SMA(close_prices, timeperiod=15)    # nearly equal to 75D
            nikkei_df['SMA_40'] = talib.SMA(close_prices, timeperiod=40)    # nearly equal to 200D

            nikkei_df['RSI_26'] = talib.RSI(close_prices, timeperiod=26)
            nikkei_df['RSI_14'] = talib.RSI(close_prices, timeperiod=14)
            nikkei_df['RSI_9'] = talib.RSI(close_prices, timeperiod=9)

            nikkei_df['MACD'], nikkei_df['MACD_signal'], nikkei_df['MACD_hist'] = talib.MACD(
                close_prices, fastperiod=12, slowperiod=26, signalperiod=9
            )

            nikkei_df['STC_fk'], nikkei_df['STC_fd'] = talib.STOCH(
                high_prices, low_prices, close_prices,
                fastk_period=14, slowk_period=3, slowk_matype=0,
                slowd_period=3, slowd_matype=0
            )

            nikkei_df['MOM_10'] = talib.MOM(close_prices, timeperiod=10)

            nikkei_df['BB1U'], _, nikkei_df['BB1L'] = talib.BBANDS(
                close_prices, timeperiod=15, nbdevup=1, nbdevdn=1, matype=0
            )

            nikkei_df['BB2U'], _, nikkei_df['BB2L'] = talib.BBANDS(
                close_prices, timeperiod=15, nbdevup=2, nbdevdn=2, matype=0
            )

            close_diff = nikkei_df['close'][1:].values - nikkei_df['close'][:-1].values
            close_diff = np.insert(close_diff, 0, 0)
            nikkei_df['Close_Diff'] = close_diff

            nikkei_df.iloc[:40, 2:] = np.nan # Remove initial rows with NaN indicators due to lookback periods

            input_mask = nikkei_df.index

            big_TradeRecord_df.loc[input_mask] = nikkei_df

    print('\nAll technical indicators calculated.')
    big_TradeRecord_df.drop(columns=['ticker', 'jp'], inplace=True)
    output_fp = Path('data/main/master/weekly_TradeRecord(by_wednesday)_TechnicalIndicators_2.csv')
    big_TradeRecord_df.to_csv(output_fp, index=False)

def calculate_fundamental_indicators():
    etc_dir = Path('data/main/expansion/fundamental/etc/weekly_etc')
    finrep_dir = Path('data/main/expansion/fundamental/financial_report/weekly_FinancialReport')
    weekly_trarec_dir = Path('data/main/expansion/technical/weekly_technical_by_wednesday')

    nk_reference_fp = Path('data/tickers/util_csv/nktk_cross_reference_rule.csv')
    origin_nk_reference_df = pd.read_csv(nk_reference_fp)

    etc_csv_fps = sorted([fp for fp in etc_dir.rglob('.') if fp.suffix == '.csv'], key=lambda x: int(x.stem[4:]))
    finrep_csv_fps = sorted([fp for fp in finrep_dir.rglob('.') if fp.suffix == '.csv'], key=lambda x: int(x.stem[23:]))
    weekly_trarec_csv_fps = sorted([fp for fp in weekly_trarec_dir.rglob('.') if fp.suffix == '.csv'], key=lambda x: int(x.stem[19:]))

    fundamental_indicators_df = pd.DataFrame()

    for etc_fp, finrep_fp, weekly_trarec_fp in zip(etc_csv_fps, finrep_csv_fps, weekly_trarec_csv_fps):
        assert etc_fp.stem[4:] == finrep_fp.stem[23:], f"Week ID mismatch: {etc_fp.stem[4:]} != {finrep_fp.stem[23:]}"
        print('\r', f'Processing week ID {etc_fp.stem[4:]} ... ', end='     ')
        tmp_fundamental_indicators_df = origin_nk_reference_df.copy().set_index('nikkei').sort_values(by='nikkei', key=lambda x: x.str[1:].astype(int)).reset_index()
        etc_df = pd.read_csv(etc_fp).copy().set_index('nikkei').sort_values(by='nikkei', key=lambda x: x.str[1:].astype(int)).reset_index()
        finrep_df = pd.read_csv(finrep_fp).copy().set_index('nikkei').sort_values(by='nikkei', key=lambda x: x.str[1:].astype(int)).reset_index()
        weekly_trarec_df = pd.read_csv(weekly_trarec_fp).copy().set_index('nikkei').sort_values(by='nikkei', key=lambda x: x.str[1:].astype(int)).reset_index()

        finrep_df['非支配株主持分／非支配持分'] = finrep_df['非支配株主持分／非支配持分'].fillna(0)
        finrep_df['親会社株主に帰属する当期純利益（連結）／当期利益（単独）［累計］'] = finrep_df['親会社株主に帰属する当期純利益（連結）／当期利益（単独）［累計］'].fillna(finrep_df['親会社株主に帰属する当期純利益（連結）／当期利益（単独）［累計］'].mean())

        BPS_series = (finrep_df['資産合計'] - finrep_df['負債合計'] - finrep_df['非支配株主持分／非支配持分'])*1e+6 / etc_df['期中平均株式数［累計］']

        tmp_fundamental_indicators_df['week_id'] = etc_fp.stem[4:]
        tmp_fundamental_indicators_df['PBR'] = weekly_trarec_df['close'] / BPS_series
        tmp_fundamental_indicators_df['EPS'] = finrep_df['親会社株主に帰属する当期純利益（連結）／当期利益（単独）［累計］']*1e+6 / etc_df['期中平均株式数［累計］']
        tmp_fundamental_indicators_df['PER'] = weekly_trarec_df['close'] / tmp_fundamental_indicators_df['EPS']
        tmp_fundamental_indicators_df['dividends_per_share'] = etc_df['１株当たり配当金（各期末）']
        tmp_fundamental_indicators_df['market_capitalization'] = weekly_trarec_df['close'] * etc_df['期中平均株式数［累計］']

        fundamental_indicators_df = pd.concat([fundamental_indicators_df, tmp_fundamental_indicators_df], ignore_index=True, axis=0)

    output_fp = Path(f'data/main/master/weekly_FundamentalIndicators.csv')
    fundamental_indicators_df = fundamental_indicators_df[['nikkei', 'week_id', 'PBR', 'PER', 'EPS', 'dividends_per_share', 'market_capitalization']]
    fundamental_indicators_df.to_csv(output_fp, index=False)

def delete_partial_fundamental_indicators():
    fa_fp = Path('data/main/master/weekly_FundamentalIndicators.csv')
    ta_fp = Path('data/main/master/weekly_TradeRecord(by_wednesday)_TechnicalIndicators_2.csv')
    fa_df = (
        pd.read_csv(fa_fp)
        .copy()
        .assign(nikkei_num=lambda d: d['nikkei'].str[1:].astype(int))
        .sort_values(by=['week_id', 'nikkei'])
        .reset_index(drop=True)
    ).drop(columns=['nikkei_num'])
    ta_df = (
        pd.read_csv(ta_fp)
        .copy()
        .assign(nikkei_num=lambda d: d['nikkei'].str[1:].astype(int))
        .sort_values(by=['week_id', 'nikkei'])
        .reset_index(drop=True)
    ).drop(columns=['nikkei_num'])

    invalid_ta_mask = ta_df.iloc[:, 2:].isnull().all(axis=1)
    fa_df.iloc[invalid_ta_mask, 2:] = np.nan

    fa_df = fa_df[['nikkei', 'week_id'] + [c for c in fa_df.columns if c not in ['nikkei', 'week_id']]]

    fa_df.to_csv(fa_fp.parent / 'weekly_FundamentalIndicators_cleaned.csv', index=False)

def impute_missing_fundamental_indicators():
    fa_fp = Path('data/main/master/weekly_Funda.csv')
    fa_df = pd.read_csv(fa_fp)

    impute_mask_1 = fa_df[['PBR', 'PER', 'EPS', 'dividends_per_share', 'market_capitalization']].isnull().any(axis=1)
    impute_mask_2 = ~fa_df[['PBR', 'PER', 'EPS', 'dividends_per_share', 'market_capitalization']].isnull().all(axis=1)

    impute_mask = impute_mask_1 & impute_mask_2

    cols = ['PBR', 'PER', 'EPS', 'dividends_per_share', 'market_capitalization']

    # まず groupby-transform 結果を全体に作る
    filled = fa_df.groupby('nikkei')[cols].transform(lambda g: g.ffill().bfill())

    # そのうち、impute_mask が True の行だけを上書き
    fa_df.loc[impute_mask, cols] = filled.loc[impute_mask, cols]

    fa_df.to_csv(fa_fp.parent / 'weekly_FundamentalIndicators_imputed.csv', index=False)

def merge_all_finrep():
    finrep_dir = Path('data/main/expansion/fundamental/financial_report/weekly_FinancialReport')
    tr_csv = pd.read_csv(Path('data/main/master/product/weekly_TR(wed)_Tech.csv'))

    invalid_mask = ~tr_csv.iloc[:, 2:].notnull().all(axis=1)
    
    finrep_csv_fps = sorted([fp for fp in finrep_dir.rglob('.') if fp.suffix == '.csv'], key=lambda x: int(x.stem[23:]))

    all_finrep_df = pd.DataFrame()

    for i, finrep_fp in enumerate(finrep_csv_fps):
        print('\r', f'Merging financial report for week ID {finrep_fp.stem[23:]} ({i+1}/{len(finrep_csv_fps)}) ... ', end='     ')
        finrep_df = pd.read_csv(finrep_fp)
        finrep_df['week_id'] = finrep_fp.stem[23:]
        all_finrep_df = pd.concat([all_finrep_df, finrep_df], ignore_index=True, axis=0)

    print('\nAll financial reports merged.')
    all_finrep_df = all_finrep_df[['nikkei', 'week_id'] + [c for c in all_finrep_df.columns if c not in ['nikkei', 'week_id', 'ticker', 'jp']]]
    all_finrep_df.iloc[invalid_mask, 2:] = np.nan
    print('Invalid rows set to NaN.')

    output_fp = Path('data/main/master/weekly_FR.csv')
    all_finrep_df.to_csv(output_fp, index=False)

merge_all_finrep()

