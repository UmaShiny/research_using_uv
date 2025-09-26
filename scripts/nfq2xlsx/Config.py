from pynfq import pyNFQ as nfq


class Path:

    TICKER_SYMBOL_CSV_PATH = "TickerOnly.csv"

    SRC_DIRPATH_DICT = {
        nfq.repair_nfqxlsx.__name__: ".\\data\\raw_data",  # must be remain!!
        nfq.xlsx2csv.__name__: ".\\data\\temp_xlsx",
    }

    DST_DIRPATH_DICT = {
        nfq.repair_nfqxlsx.__name__: ".\\data\\temp_xlsx",
        nfq.xlsx2csv.__name__: ".\\data\\funda_csv",
    }


class Constant:

    REPAIR = True
    XLSX2CSV = False

    REMOVE_COLUMN_FOR_XLSX2CSV = [1, 2, 4, 5]
    REMOVE_ROW_FOR_XLSX2CSV = [1, 2, 3, 4, 5]
