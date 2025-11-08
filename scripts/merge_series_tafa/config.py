class cons:

    target = 't'

    class path:
        
        # mapping file and listing deleted tickers file
        # nkc_tkc_map_csv = 'data/tickers/result/Tickers_with_Nikkei.csv'
        nkc_tkc_map_csv = 'data/tickers/result/4608_cf_table.csv'
        deleted_tickers_csv = 'data/tickers/result/Deleted_Tickers_with_Nikkei.csv'

        # src and dst paths for fundamental data
        # daily_data_csvs = 'data/origin_fundamental/only_finres'
        # dst_expansed_data_csvs = 'data/expansed_fundamental/daily_expansed_only_finres'
        daily_data_csvs = 'data/origin_fundamental/etc'
        dst_expansed_data_csvs = 'data/expansed_fundamental/daily_expansed_etc'

        # complementation file path
        # src_complemented_data_csvs = 'data/expansed_fundamental/daily_expansed_only_finres_spare'
        # dst_complemented_data_csvs = 'data/expansed_fundamental/daily_expansed_complemented_only_finres'
        src_complemented_data_csvs = 'data/expansed_fundamental/daily_expansed_etc_spare'
        dst_complemented_data_csvs = 'data/expansed_fundamental/daily_expansed_complemented_etc'

        # dst paths for expansed technical data
        ampm_expansed_data_csvs = 'data/expansed_technical/ampm_expansed_technical'
        daily_expansed_data_csvs = 'data/expansed_technical/daily_expansed_technical'
        weekly_expansed_data_csvs = 'data/expansed_technical/weekly_expansed_technical'
        monthly_expansed_data_csvs = 'data/expansed_technical/monthly_expansed_technical'

        # fundamental_kessan_only_csvs = 'data/nfq/nfqcsv/main_nfqcsv'
        # fundamental_kessan_only_csvs = 'data/nfq/nfqcsv/stcvol_delmissing_nfqcsv'

        # conversion dst / src paths

        # imputarion dst / src paths by cross-sectional mean

        # src_fundamental_imputed_by_csmean = 'data/expansed_fundamental/daily_expansed_deleted_invalid_date_complemented_only_finres'
        # dst_fundamental_imputed_by_csmean = 'data/expansed_fundamental/daily_expansed_deleted_invalid_date_complemented_only_finres_imputed_by_csmean'

        src_fundamental_imputed_by_csmean = 'data/expansed_fundamental/daily_expansed_deleted_invalid_date_complemented_etc'
        dst_fundamental_imputed_by_csmean = 'data/expansed_fundamental/daily_expansed_deleted_invalid_date_complemented_etc_imputed_by_csmean'



code_packing = """
def wed_weekday(date: str) -> int:
    weekday = datetime.date(int(date[0:4]), int(date[4:6]), int(date[6:8])).weekday()
    if weekday < 2:
        return weekday + 3
    else:
        return (weekday - 2) % 7  # Convert Wednesday=2 to 0, ... Tuesday=1 to 6

def mon_weekday(date: str) -> int:
    weekday = datetime.date(int(date[0:4]), int(date[4:6]), int(date[6:8])).weekday()
    return weekday  # Monday=0, Sunday=6

daily_technical_file = Path('data/main/expansion/technical/ampm_technical')
file_list = sorted([fp.stem for fp in daily_technical_file.rglob('.') if fp.suffix == '.csv'])

result = {'date': [], 'weekday': []}
tmp_date_list = []
for day_serial in range(0, (datetime.date(2023, 12, 31) - datetime.date(2001, 1, 3)).days):
    tmp_var = (datetime.timedelta(days=day_serial) + datetime.date(2001, 1, 3)).strftime('%Y%m%d')
    if tmp_var == '20050506': 
        print('')
    if not file_list:
        break
    if day_serial % 7 == 0 and tmp_date_list:
        date_and_weekday = [(date, wed_weekday(date)) for date in tmp_date_list]
        date_and_weekday_sorted = sorted(date_and_weekday, key=lambda x: x[1])
        date = date_and_weekday_sorted[0][0]
        result['date'].append(datetime.datetime.strptime(date, '%Y%m%d').strftime('%Y/%m/%d'))
        result['weekday'].append(mon_weekday(date))
        tmp_date_list = []
    if file_list[0] == (datetime.date(2001, 1, 3) + datetime.timedelta(days=day_serial)).strftime('%Y%m%d'):
        tmp_date_list.append(file_list.pop(0))

# green color for finished message
print('\n \033[92m= Finished checking technical files.\033[0m')

result_df = pd.DataFrame(result)
merged_df = pd.merge(
    result_df, pd.read_csv('docs/technical_fundamental_valid_weekly_date_check.csv'),
    on='date',
    how='outer', 
)

merged_df.to_csv('docs/technical_fundamental_valid_weekly_date_check_v2.csv', index=False)
"""




