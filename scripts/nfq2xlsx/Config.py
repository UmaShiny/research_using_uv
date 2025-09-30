from pynfq import pyNFQ as nfq


class Path:

    TICKER_SYMBOL_CSV_PATH = ".\\scripts\\nfq2xlsx\\TickerOnly.csv"

    SRC_DIRPATH_DICT = {
        nfq.repair_nfqxlsx.__name__: ".\\data\\raw_data\\raw_data_date",  # must be remain!!
        nfq.xlsx2csv.__name__: ".\\data\\temp_xlsx\\temp_xlsx_complete",
    }

    DST_DIRPATH_DICT = {
        nfq.repair_nfqxlsx.__name__: ".\\data\\temp_xlsx\\temp_xlsx_date",
        nfq.xlsx2csv.__name__: ".\\data\\funda_csv",
    }

    TEMP_XLSX_DATE_DIRPATH = ".\\data\\temp_xlsx\\temp_xlsx_date"
    TEMP_XLSX_MAIN_DIRPATH = ".\\data\\temp_xlsx\\temp_xlsx_main"
    TEMP_XLSX_COMPLETE_DIRPATH = ".\\data\\temp_xlsx\\temp_xlsx_complete"


class Constant:

    REPAIR = False
    XLSX2CSV = True

    REMOVE_COLUMN_FOR_XLSX2CSV = [] # 横
    # if you run "Add_new_xlsx.py", please set [1,2,3,4,5,6,7,8] to this variable
    # if you run "convert_nfq2xlsx.py", please set [] to this variable
    REMOVE_ROW_FOR_XLSX2CSV = [] # 縦
    # if you run "Add_new_xlsx.py", please set [1,2] to this variable
    # if you run "convert_nfq2xlsx.py", please set [] to this variable

    ACTUAL_RANGE_ROW = {"start": 0, "end": 493} # 
    KESSANTANSIN_RANGE_ROW = {"start": 2, "end": 493}
    YUUKAHOUKOKU_RANGE_ROW = {"start": 493, "end": 984}
    KESSANTANSIN_DATE_ROW = 984
    YUUKAHOUKOKU_DATE_ROW = 985

    SUBJECTNAME_COLUMN = 6
    SUBJECTCODE_COLUMN = 7

    progress = "7561"
