from pynfq import pyNFQ as nfq


class Path:

    TICKER_SYMBOL_CSV_PATH = "scripts/nfq2xlsx/TickerOnly.csv"

    SRC_DIRPATH_DICT = {
        nfq.repair_nfqxlsx.__name__: "data/nfq/raw_nfqxlsx/raw_stcvol_nfqxlsx/20000101-20191231",  # must be remain!!
        nfq.xlsx2csv.__name__: "data/nfq/concat_nfqxlsx/concat_stcvol_nfqxlsx",
    }

    DST_DIRPATH_DICT = {
        nfq.repair_nfqxlsx.__name__: "data/nfq/fix_nfqxlsx/fix_stcvol_nfqxlsx/20000101-20191231",
        nfq.xlsx2csv.__name__: "data/nfq/nfqcsv/stcvol_nfqcsv",
    }

    # TEMP_XLSX_DATE_DIRPATH = "data/temp_xlsx/temp_xlsx_date"
    # TEMP_XLSX_MAIN_DIRPATH = "data/temp_xlsx/temp_xlsx_main"
    # TEMP_XLSX_COMPLETE_DIRPATH = "data/temp_xlsx/temp_xlsx_complete"


class Constant:

    REPAIR = True
    XLSX2CSV = False

    REMOVE_COLUMN_FOR_XLSX2CSV = [1,2,3,4,5,6,7,8]  # 横
    # if you run "Add_new_xlsx.py", please set [1,2,3,4,5,6,7,8] to this variable
    # if you run "convert_nfq2xlsx.py", please set [] to this variable
    REMOVE_ROW_FOR_XLSX2CSV = [1,2]  # 縦
    # if you run "Add_new_xlsx.py", please set [1,2] to this variable
    # if you run "convert_nfq2xlsx.py", please set [] to this variable

    ACTUAL_RANGE_ROW = {"start": 0, "end": 4} #
    KESSANTANSIN_RANGE_ROW = {"start": 2, "end": 4} # 
    YUUKAHOUKOKU_RANGE_ROW = {"start": 5, "end": 7} # 
    # KESSANTANSIN_DATE_ROW = 984
    # YUUKAHOUKOKU_DATE_ROW = 985

    SUBJECTNAME_COLUMN = 6
    SUBJECTCODE_COLUMN = 7

    progress = "0000000"
