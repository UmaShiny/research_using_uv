import pandas as pd
import numpy as np
from pathlib import Path
from datetime import datetime
import re
from pprint import pprint

def reduce_funda_columns():
    funda_dp = Path('data/main/build/nfq/nfqcsv/main_nfqcsv')
    funda_fp_list = [fp for fp in funda_dp.rglob('.') if fp.suffix == '.csv']
    dst_dir = Path('data/main/build/nfq/nfqcsv_reduced')

    for funda_fp in funda_fp_list:
        df = pd.read_csv(funda_fp)
        print('\r', 'Processing:', funda_fp.stem, f'({len(df.columns)}) => ', end='')

        df['受取手形・売掛金及び契約資産／売掛金及びその他の短期債権'] = (
            df['（受取手形）'].fillna(0) + 
            df['（売掛金）'].fillna(0) + 
            df['（契約資産）'].fillna(0)
        )

        df['受取手形・売掛金及び契約資産／売掛金及びその他の短期債権'] = df['受取手形・売掛金及び契約資産／売掛金及びその他の短期債権'].replace(0, np.nan)
        
        df.drop(columns=[
            '（受取手形）', 
            '（売掛金）', 
            '（契約資産）'
        ], inplace=True)

        df['リース債権及びリース投資資産'] = (
            df['（リース債権）'].fillna(0) + 
            df['（リース投資資産）'].fillna(0)
        )

        df['リース債権及びリース投資資産'] = df['リース債権及びリース投資資産'].replace(0, np.nan)
        
        df.drop(columns=[
            '（リース債権）', 
            '（リース投資資産）'
        ], inplace=True)

        df['営業貸付金・営業投資有価証券'] = (
            df['（営業貸付金）'].fillna(0) + 
            df['（営業投資有価証券）'].fillna(0)
        )

        df['営業貸付金・営業投資有価証券'] = df['営業貸付金・営業投資有価証券'].replace(0, np.nan)
        
        df.drop(columns=[
            '（営業貸付金）', 
            '（営業投資有価証券）'
        ], inplace=True)

        df['商品・製品'] = (
            df['（商品）'].fillna(0) + 
            df['（製品）'].fillna(0)
        )
        
        df['商品・製品'] = df['商品・製品'].replace(0, np.nan)
        
        df.drop(columns=[
            '（商品）', 
            '（製品）'
        ], inplace=True)

        df['半製品・仕掛品'] = (
            df['（半製品）'].fillna(0) + 
            df['（仕掛品・未成工事支出金）'].fillna(0)
        )

        df['半製品・仕掛品'] = df['半製品・仕掛品'].replace(0, np.nan)

        df.drop(columns=['（仕掛品・未成工事支出金（うち未成工事支出金））'], inplace=True)

        df.drop(columns=['（うち未成工事受入金）'], inplace=True)

        df.drop(columns=[
            '（半製品）', 
            '（仕掛品・未成工事支出金）'
        ], inplace=True)

        df['原材料・貯蔵品'] = (
            df['（原材料）'].fillna(0) + 
            df['（貯蔵品）'].fillna(0)
        )

        df['原材料・貯蔵品'] = df['原材料・貯蔵品'].replace(0, np.nan)
        
        df.drop(columns=[
            '（原材料）', 
            '（貯蔵品）'
        ], inplace=True)

        df['短期貸付金'] = (
            df['（短期貸付金）'].fillna(0) + 
            df['（役員・従業員短期貸付金）'].fillna(0)
        )

        df['短期貸付金'] = df['短期貸付金'].replace(0, np.nan)
        
        df.drop(columns=[
            '（短期貸付金）', 
            '（役員・従業員短期貸付金）'
        ], inplace=True)

        df['建物・構築物'] = (
            df['（建物）'].fillna(0) + 
            df['（構築物）'].fillna(0)
        )

        df['建物・構築物'] = df['建物・構築物'].replace(0, np.nan)
        
        df.drop(columns=[
            '（建物）', 
            '（構築物）'
        ], inplace=True)

        df['機械装置及び運搬具'] = (
            df['（機械及び装置）'].fillna(0) + 
            df['（船舶・車両・運搬具）'].fillna(0)
        )

        df['機械装置及び運搬具'] = df['機械装置及び運搬具'].replace(0, np.nan)
        
        df.drop(columns=[
            '（機械及び装置）', 
            '（船舶・車両・運搬具）'
        ], inplace=True)

        df['投資有価証券・関係会社株式・出資金'] = (
            df['（投資有価証券）'].fillna(0) + 
            df['（関係会社有価証券）／（持分法で会計処理されている投資）'].fillna(0) + 
            df['（出資金）'].fillna(0) + 
            df['（関係会社出資金）'].fillna(0) + 
            df['（非連結子会社関連会社株式・社債・出資金）'].fillna(0)
        )

        df['投資有価証券・関係会社株式・出資金'] = df['投資有価証券・関係会社株式・出資金'].replace(0, np.nan)
        
        df.drop(columns=[
            '（投資有価証券）', 
            '（関係会社有価証券）／（持分法で会計処理されている投資）', 
            '（出資金）',
            '（関係会社出資金）',
            '（非連結子会社関連会社株式・社債・出資金）'
        ], inplace=True)

        df['支払手形・買掛金／買掛金及びその他の短期債務'] = (
            df['（支払手形）'].fillna(0) + 
            df['（買掛金）'].fillna(0)
        )

        df['支払手形・買掛金／買掛金及びその他の短期債務'] = df['支払手形・買掛金／買掛金及びその他の短期債務'].replace(0, np.nan)
        
        df.drop(columns=[
            '（支払手形）', 
            '（買掛金）'
        ], inplace=True)

        df['１年内返済の借入金'] =  (
            df['（短期借入金）'].fillna(0) + 
            df['（役員・従業員短期借入金）'].fillna(0) + 
            df['（コマーシャルペーパー）'].fillna(0) + 
            df['（１年内返済の長期借入金）'].fillna(0)
        )

        df['１年内返済の借入金'] = df['１年内返済の借入金'].replace(0, np.nan)
        
        df.drop(columns=[
            '（短期借入金）', 
            '（役員・従業員短期借入金）', 
            '（コマーシャルペーパー）', 
            '（１年内返済の長期借入金）'
        ], inplace=True)

        df['１年内償還の社債・転換社債'] = (
            df['（１年内償還の社債）'].fillna(0) + 
            df['（１年内償還の転換社債）'].fillna(0)
        )

        df['１年内償還の社債・転換社債'] = df['１年内償還の社債・転換社債'].replace(0, np.nan)

        df['社債・転換社債'] = (
            df['（社債）'].fillna(0) +
            df['（転換社債）'].fillna(0)
        )

        df['社債・転換社債'] = df['社債・転換社債'].replace(0, np.nan)

        df.drop(columns=[
            '（社債）',
            '（転換社債）'
        ], inplace=True)
        
        df.drop(columns=[
            '（１年内償還の社債）', 
            '（１年内償還の転換社債）'
        ], inplace=True)

        df['未払金・未払費用'] = (
            df['（未払金）'].fillna(0) + 
            df['（未払費用）'].fillna(0)
        )

        df['未払金・未払費用'] = df['未払金・未払費用'].replace(0, np.nan)
        
        df.drop(columns=[
            '（未払金）', 
            '（未払費用）'
        ], inplace=True)

        df['退職給付に係る負債（退職給付引当金）'] = (
            df['（役員退職慰労引当金）'].fillna(0) + 
            df['（債務保証損失引当金）'].fillna(0) + 
            df['（その他長期引当金）'].fillna(0)
        )

        df['退職給付に係る負債（退職給付引当金）'] = df['退職給付に係る負債（退職給付引当金）'].replace(0, np.nan)
        
        df.drop(columns=[
            '（役員退職慰労引当金）', 
            '（債務保証損失引当金）',
            '（その他長期引当金）'
        ], inplace=True)

        df['受取利息・配当金［累計］'] = (
            df['（受取利息・割引料・有価証券利息）［累計］'].fillna(0) +
            df['（受取配当金）［累計］'].fillna(0)
        )

        df['受取利息・配当金［累計］'] = df['受取利息・配当金［累計］'].replace(0, np.nan)
        
        df.drop(columns=[
            '（受取利息・割引料・有価証券利息）［累計］',
            '（受取配当金）［累計］'
        ], inplace=True)

        df['その他資産処分益・評価益［累計］'] = (
            df['（その他資産処分益）［累計］'].fillna(0) +
            df['（その他資産評価益）［累計］'].fillna(0)
        )

        df['その他資産処分益・評価益［累計］'] = df['その他資産処分益・評価益［累計］'].replace(0, np.nan)
        
        df.drop(columns=[
            '（その他資産処分益）［累計］',
            '（その他資産評価益）［累計］'
        ], inplace=True)

        df['支払利息・割引料［累計］'] = (
            df['（社債利息）［累計］'].fillna(0) + 
            df['（コマーシャルペーパー利息）［累計］'].fillna(0) +
            df['（手形売却損）［累計］'].fillna(0) +
            df['（売上割引）［累計］'].fillna(0)
        )

        df['支払利息・割引料［累計］'] = df['支払利息・割引料［累計］'].replace(0, np.nan)
        
        df.drop(columns=[
            '（社債利息）［累計］', 
            '（コマーシャルペーパー利息）［累計］',
            '（手形売却損）［累計］',
            '（売上割引）［累計］'
        ], inplace=True)

        df['その他資産処分損・評価損［累計］'] = (
            df['（その他資産処分損）［累計］'].fillna(0) +
            df['（その他資産評価損）［累計］'].fillna(0)
        )

        df['その他資産処分損・評価損［累計］'] = df['その他資産処分損・評価損［累計］'].replace(0, np.nan)
        
        df.drop(columns=[
            '（その他資産処分損）［累計］',
            '（その他資産評価損）［累計］'
        ], inplace=True)

        df['事業・組織再編関連利益［累計］'] = (
            df['（有形固定資産処分益・評価益）［累計］'].fillna(0) +
            df['（有形固定資産以外のその他資産処分益・評価益）［累計］'].fillna(0)
        )

        df['事業・組織再編関連利益［累計］'] = df['事業・組織再編関連利益［累計］'].replace(0, np.nan)
        
        df.drop(columns=[
            '（有形固定資産処分益・評価益）［累計］',
            '（有形固定資産処分益・評価益（うち不動産））［累計］',
            '（有形固定資産以外のその他資産処分益・評価益）［累計］'
        ], inplace=True)

        df['減損損失［累計］'] = (
            df['（有形固定資産処分損・評価損）［累計］'].fillna(0) +
            df['（有形固定資産以外のその他資産処分損・評価損）［累計］'].fillna(0)
        )

        df['減損損失［累計］'] = df['減損損失［累計］'].replace(0, np.nan)
        
        df.drop(columns=[
            '（有形固定資産処分損・評価損）［累計］',
            '（有形固定資産処分損・評価損（うち不動産））［累計］',
            '（有形固定資産以外のその他資産処分損・評価損）［累計］'
        ], inplace=True)

        df['受取利息・配当金［３ヵ月］'] = (
            df['（受取利息・割引料・有価証券利息）［３ヵ月］'].fillna(0) +
            df['（受取配当金）［３ヵ月］'].fillna(0)
        )

        df['受取利息・配当金［３ヵ月］'] = df['受取利息・配当金［３ヵ月］'].replace(0, np.nan)
        
        df.drop(columns=[
            '（受取利息・割引料・有価証券利息）［３ヵ月］',
            '（受取配当金）［３ヵ月］'
        ], inplace=True)

        df['その他資産処分益・評価益［３ヵ月］'] = (
            df['（その他資産処分益）［３ヵ月］'].fillna(0) +
            df['（その他資産評価益）［３ヵ月］'].fillna(0)
        )

        df['その他資産処分益・評価益［３ヵ月］'] = df['その他資産処分益・評価益［３ヵ月］'].replace(0, np.nan)
        
        df.drop(columns=[
            '（その他資産処分益）［３ヵ月］',
            '（その他資産評価益）［３ヵ月］'
        ], inplace=True)

        df['支払利息・割引料［３ヵ月］'] = (
            df['（社債利息）［３ヵ月］'].fillna(0) + 
            df['（コマーシャルペーパー利息）［３ヵ月］'].fillna(0) +
            df['（手形売却損）［３ヵ月］'].fillna(0) +
            df['（売上割引）［３ヵ月］'].fillna(0)
        )

        df['支払利息・割引料［３ヵ月］'] = df['支払利息・割引料［３ヵ月］'].replace(0, np.nan)
        
        df.drop(columns=[
            '（社債利息）［３ヵ月］', 
            '（コマーシャルペーパー利息）［３ヵ月］',
            '（手形売却損）［３ヵ月］',
            '（売上割引）［３ヵ月］'
        ], inplace=True)

        df['その他資産処分損・評価損［３ヵ月］'] = (
            df['（その他資産処分損）［３ヵ月］'].fillna(0) +
            df['（その他資産評価損）［３ヵ月］'].fillna(0)
        )

        df['その他資産処分損・評価損［３ヵ月］'] = df['その他資産処分損・評価損［３ヵ月］'].replace(0, np.nan)
        
        df.drop(columns=[
            '（その他資産処分損）［３ヵ月］',
            '（その他資産評価損）［３ヵ月］'
        ], inplace=True)

        df['事業・組織再編関連利益［３ヵ月］'] = (
            df['（有形固定資産処分益・評価益）［３ヵ月］'].fillna(0) +
            df['（有形固定資産以外のその他資産処分益・評価益）［３ヵ月］'].fillna(0)
        )

        df['事業・組織再編関連利益［３ヵ月］'] = df['事業・組織再編関連利益［３ヵ月］'].replace(0, np.nan)
        
        df.drop(columns=[
            '（有形固定資産処分益・評価益）［３ヵ月］',
            '（有形固定資産処分益・評価益（うち不動産））［３ヵ月］',
            '（有形固定資産以外のその他資産処分益・評価益）［３ヵ月］'
        ], inplace=True)

        df['減損損失［３ヵ月］'] = (
            df['（有形固定資産処分損・評価損）［３ヵ月］'].fillna(0) +
            df['（有形固定資産以外のその他資産処分損・評価損）［３ヵ月］'].fillna(0)
        )

        df['減損損失［３ヵ月］'] = df['減損損失［３ヵ月］'].replace(0, np.nan)
        
        df.drop(columns=[
            '（有形固定資産処分損・評価損）［３ヵ月］',
            '（有形固定資産処分損・評価損（うち不動産））［３ヵ月］',
            '（有形固定資産以外のその他資産処分損・評価損）［３ヵ月］'
        ], inplace=True)


        print(f'({len(df.columns)})', end=' ')

        df.to_csv(dst_dir / funda_fp.name, index=False)
        print('=> Done', end='  ')
        
def yearly2quarterly():
    funda_dp = Path('data/main/build/nfq/nfqcsv_reduced')
    funda_fp_list = [fp for fp in funda_dp.rglob('.') if fp.suffix == '.csv']
    dst_dir = Path('data/main/build/nfq/nfqcsv_reduced_modify_quarterly')

    # 発表月に応じて四半期をラベリング
    def assign_quarter(month):
        if month in [7, 8, 9]:
            return 'Q1'
        elif month in [10, 11, 12]:
            return 'Q2'
        elif month in [1, 2, 3]:
            return 'Q3'
        elif month in [4, 5, 6]:
            return 'Q4'
        else:
            return None  # 例外（発表月が想定外のとき）

    for funda_fp in funda_fp_list:
        df = pd.read_csv(funda_fp)
        print('\r', 'Processing:', funda_fp.stem, f'({len(df.columns)}) => ', end='')

        df['決算発表日'] = pd.to_datetime(df['決算発表日'])

        df['月'] = df['決算発表日'].dt.month

        df['四半期'] = df['月'].apply(assign_quarter)

        df.drop(columns=['月'], inplace=True)

        df_yearly_only = df.filter(like='累計', axis=1).columns.to_list()

        # 四半期順を保証
        # Q4を踏んだら次の年度番号を+1
        seq = []
        counter = 0
        for q in df['四半期']:
            seq.append(counter)
            if q == 'Q4':
                counter += 1

        df['年度ラベル'] = seq

        for col in df.columns.to_list()[2:-5]:
            # step. 1
            # 欠損値を埋める

            df['今年度データ有'] = (
                df.
                groupby('年度ラベル')[col].
                transform(lambda x: x.notnull().any(axis=0))
            )

            # df['来年度データ有'] = df.loc[df['四半期'] == 'Q1', '今年度データ有']
            df['来年度データ有'] = df['今年度データ有'].shift(periods=-1, fill_value=True)
            df['来年度データ有'] = df['来年度データ有'].bfill()


            cond_1 = False # 周期的に記録されており，かつその数が全レポートの1/4倍以下の場合
            cond_2 = False # ほぼすべて埋まっている場合
            cond_3 = False # その他の条件（未使用）

            counted = df.groupby('四半期')[col].count()
            max_label = counted.idxmax()  # 最大値を持つ四半期
            max_val = counted.max()
            min_val = counted.min()
            # other_sum = counted.sum() - max_val

            # Qn に偏りがある場合を，以下の条件で設定（状況によって修正が必要な場合もあり）
            # ほとんどの場合はQn=4なので，のちにbfillで1/4倍することで線形補完を行う
            if (max_val - min_val > max_val / 2) and (counted.sum() > len(df) / 4):
                cond_1 = True
            # ほぼすべて埋まっているのに，何かしらの原因で欠損している場合を，
            # 以下の条件で設定（状況によって修正が必要な場合もあり）
            if counted.sum() / len(df_yearly_only) > 0.8:
                cond_2 = True
            if cond_1 and cond_2:
                cond_1 = False  # 両方満たす場合はcond_2を優先する
            
            if cond_1: # 1/4したデータをffillしていく
                # 0埋めはダメ => 情報を知らないことになる
                # 情報を持ち越すことが重要なのでは？

                # 科目名が「累計」を含む場合は，年度ごとの差分を取る
                if col in df_yearly_only: 
                    
                    # 値がffillされていない場合
                    # 累計データの場合は期間内に存在する文書の数で割る

                    # 各 年度ラベル に対して 四半期の種類数 を計算
                    df = df.copy()

                    df[col] = df[col].fillna(0)
                    quarter_count = df.groupby('年度ラベル')['四半期'].nunique()
                    mask = df.groupby('年度ラベル')[col].nunique() == 1

                    df_mask = df['年度ラベル'].map(mask)

                    # それを各行にマッピングして col を割る
                    tmp_df = df['年度ラベル'].map(quarter_count)
                    df.loc[df_mask, 'diff'] = df[col] / tmp_df

                    df['diff'] = df.groupby('年度ラベル')[col].transform(
                        lambda x: x - x.shift(1) if ~mask[mask.index[x.name]] else x
                    )

                    # 元の列を差分列で置き換え
                    tmp_df = df.groupby('年度ラベル')['diff']
                    tmp_df = tmp_df.ffill()
                    df['diff'] = tmp_df
                    # 元の列を差分列で置き換え
                    df.loc[df['diff'].notna(), col] = df['diff'][df['diff'].notna()]

                    df.drop(columns=['diff'], inplace=True)

                    df = df.copy()
                else:
                    # 累計データでない場合はそのまま
                    # 期中で ffill を適用
                    tmp_df = df.groupby('年度ラベル')[col]
                    df[col] = tmp_df.transform(lambda x: x.ffill())

                    # 今年度・来年度両方にデータが存在する場合にのみ，さらにffillを適用
                    tmp_df = df.loc[df['今年度データ有'] & df['来年度データ有'], col]
                    df.loc[df['今年度データ有'] & df['来年度データ有'], col] = tmp_df.ffill()

                    df = df.copy()

            elif cond_2: # 四半期のラベルごとに平均して埋める
                # 平均で埋めると，例えば流動資産などで不自然な値になる可能性があるため，
                # この場合，突然企業が即座に現金化が可能な資産を多く持ったこととなり不適切
                # よって期中の平均データで補完する
                df[col] = df.groupby('年度ラベル')[col].transform(lambda x: x.fillna(x.mean()))
                if col in df_yearly_only: 

                    # 値がffillされていない場合
                    # 各年度ラベル内で差分を取る
                    df[col] = df[col].fillna(0)
                    tmp_df = df.groupby('年度ラベル')[col]

                    df['diff'] = tmp_df.transform(lambda x: x - x.shift(1))

                    # 元の列を差分列で置き換え
                    df.loc[df['diff'].notna(), col] = df['diff'][df['diff'].notna()]

                    df.drop(columns=['diff'], inplace=True)

                    df = df.copy()
            else:
                # 今年度・来年度両方にデータが存在する場合にのみ，さらにffillを適用
                tmp_df = df.loc[df['今年度データ有'] & df['来年度データ有'], col]
                df.loc[df['今年度データ有'] & df['来年度データ有'], col] = tmp_df.ffill()
        
        df.drop(columns=['今年度データ有', '来年度データ有', '年度ラベル', '四半期'], inplace=True)
        drop_columns = [col for col in df.columns if '［３ヵ月］' in col if col not in ['売上高・営業収益（短信サマリー）［３ヵ月］']]
        df.drop(columns=drop_columns, inplace=True)
        df.columns = df.columns.str.replace(r'［累計］|［３ヵ月］', '', regex=True)

        print(f'({len(df.columns)})', end=' ')

        df.to_csv(dst_dir / funda_fp.name, index=False)

def drop_samary():
    path = Path('data/main/build/nfq/nfqcsv_reduced_modify_quarterly')

    for fp in [fp for fp in path.rglob('.') if fp.suffix == '.csv']:
        df = pd.read_csv(fp)
        print('\r', 'Processing:', fp.stem, f'({len(df.columns)}) => ', end='')

        drop_columns = [col for col in df.columns if '売上高・営業収益（短信サマリー）' in col]
        df.drop(columns=drop_columns, inplace=True)

        print(f'({len(df.columns)})', end=' ')

        df.to_csv(fp, index=False)
        print('=> Done', end='  ')

def drop_includer_and_sub():
    path = Path('data/main/build/nfq/nfqcsv_reduced_modify_quarterly')

    for fp in [fp for fp in path.rglob('.') if fp.suffix == '.csv']:
        df = pd.read_csv(fp)
        print('\r', 'Processing:', fp.stem, f'({len(df.columns)}) => ', end='')

        df.loc[df['固定資産の取得による支出（▲）'].isna(), '固定資産の取得による支出（▲）'] = (
            df['固定資産の取得による支出（うち有形固定資産）（▲）'].fillna(0) +
            df['固定資産の取得による支出（うち無形固定資産）（▲）'].fillna(0) +
            df['固定資産の取得による支出（うち投資その他の資産）（▲）'].fillna(0)
        )

        df = df.rename(columns={'固定資産の取得による支出（うち有形固定資産）（▲）': '有形固定資産の取得による支出（▲）',
                                 '固定資産の取得による支出（うち無形固定資産）（▲）': '無形固定資産の取得による支出（▲）',
                                 '固定資産の取得による支出（うち投資その他の資産）（▲）': '投資その他の資産の取得による支出（▲）'})

        df['有形固定資産の取得による支出（▲）'] = df['有形固定資産の取得による支出（▲）'].fillna(0)
        df['無形固定資産の取得による支出（▲）'] = df['無形固定資産の取得による支出（▲）'].fillna(0)
        df['投資その他の資産の取得による支出（▲）'] = df['投資その他の資産の取得による支出（▲）'].fillna(0)
        
        df.loc[df['固定資産の売却による収入'].isna(), '固定資産の売却による収入'] = (
            df['固定資産の売却による収入（うち有形固定資産）'].fillna(0) +
            df['固定資産の売却による収入（うち無形固定資産）'].fillna(0) +
            df['固定資産の売却による収入（うち投資その他の資産）'].fillna(0)
        )

        df = df.rename(columns={'固定資産の売却による収入（うち有形固定資産）': '有形固定資産の売却による収入',
                                 '固定資産の売却による収入（うち無形固定資産）': '無形固定資産の売却による収入',
                                 '固定資産の売却による収入（うち投資その他の資産）': '投資その他の資産の売却による収入'})
        
        df['有形固定資産の売却による収入'] = df['有形固定資産の売却による収入'].fillna(0)
        df['無形固定資産の売却による収入'] = df['無形固定資産の売却による収入'].fillna(0)
        df['投資その他の資産の売却による収入'] = df['投資その他の資産の売却による収入'].fillna(0)

        df['売上高・営業収益（日本基準）'] = df['売上高・営業収益（日本基準）'].fillna(0)
        df.loc[df['売上高・営業収益'].isna(), '売上高・営業収益'] = df['売上高・営業収益（日本基準）']

        # 売上高・営業収益と同じ値を持っている
        df.drop(columns=['売上高・営業収益（日本基準）'], inplace=True)

        # 金融収益が重要である場合もそうでない場合も，
        # 営業収益に反映されている時点で銀行であれば本業としての稼ぐ力
        # そうでなくとも本業としての稼ぐ力が反映されているため削除
        df.drop(columns=['売上高・営業収益（うち金融収益）'], inplace=True)

        print(f'({len(df.columns)})', end=' ')

        df.to_csv(fp, index=False)
        print('=> Done', end='  ')

def drop_have_number_suffix_columns():
    path = Path('data/main/build/nfq/nfqcsv_reduced_modify_quarterly')

    for fp in [fp for fp in path.rglob('.') if fp.suffix == '.csv']:
        df = pd.read_csv(fp)
        print('\r', 'Processing:', fp.stem, f'({len(df.columns)}) => ', end='')

        drop_columns = [col for col in df.columns if re.search(r'\.\d+$', col)]
        nearly_columns = [re.sub(r'\.\d+$', '', col) for col in drop_columns]

        for nearly_col, drop_col in zip(nearly_columns, drop_columns):
            mask = df[nearly_col].isna()
            df.loc[mask, nearly_col] = df.loc[mask, drop_col]

        df.drop(columns=drop_columns, inplace=True)

        print(f'({len(df.columns)})', end=' ')

        df.to_csv(fp, index=False)
        print('=> Done', end='  ')

def check_important_column():
    important_columns = [
        '流動資産', '現金・預金／現金及び現金同等物', '固定資産／非流動資産', '資産合計',
        '流動負債', '負債合計', '純資産合計／資本合計', '資本金',
        '非支配株主持分／非支配持分', 
        '売上高・営業収益', '売上原価・営業原価','営業利益', '経常利益／税金等調整前当期純利益',
    ]

    path = Path('data/main/build/nfq/nfqcsv_reduced_modify_quarterly')

    dict_missing = {important_columns[i]: [] for i in range(len(important_columns))}
    for fp in [fp for fp in path.rglob('.') if fp.suffix == '.csv']:
        df = pd.read_csv(fp)
        print('\r', 'Processing:', fp.stem, end='')

        for col in important_columns:
            if len(df[df[col].notna()]) != len(df[col].values):
                dict_missing[col].append((fp.stem, round(len(df[df[col].notna()])/len(df[col].values), 2)))

        print(f'({len(df.columns)})', end=' ')

        print('=> Done', end='  ')
    
    print()
    for key, value in dict_missing.items():
        print({key: sorted(value, key=lambda x: x[1])})

# drop_have_number_suffix_columns()
def modify_date():
    path = Path('data/main/build/nfq/nfqcsv_reduced_modify_quarterly_and_date')
    file_paths = [fp for fp in path.rglob('.') if fp.suffix == '.csv']

    # ファイルパスリストを想定してループ
    for fp in file_paths:  # file_paths は Path のリストを想定
        print('\r', 'Processing:', fp.stem, end='')

        df = pd.read_csv(fp)

        # 日付を安全に変換
        df['決算発表日'] = pd.to_datetime(df['決算発表日'], errors='coerce')

        # 1行シフトして前の決算日を取得
        shifted_df = df.shift(periods=1)

        # 正しい日数差の計算
        delta_days = (df['決算発表日'] - shifted_df['決算発表日']).dt.days

        # 差が200日を超えるものを検出（例：前年データを誤って翌年扱いしている場合）
        date_error_mask = delta_days > 200

        # 1年前に戻す処理
        df.loc[date_error_mask, '決算発表日'] = df.loc[date_error_mask, '決算発表日'] - pd.DateOffset(years=1)

        # 保存時に日付フォーマットを統一
        df['決算発表日'] = df['決算発表日'].dt.strftime('%Y-%m-%d')

        # 上書き保存
        df.to_csv(fp, index=False)
        print(' => Done', end='  ')


modify_date()