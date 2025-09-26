from scripts.nfq2xlsx.pynfq import pyNFQ as nfq

class main_Constant:
    SRC_DIRPATH_DICT = {
        nfq.repair_nfqxlsx.__name__ : ".\\data\\raw_data", # must be remain!!
        nfq.xlsx2csv.__name__       : ".\\data\\temp_xlsx"
    }

    DST_DIRPATH_DICT = {
        nfq.repair_nfqxlsx.__name__ : ".\\data\\temp_xlsx",
        nfq.xlsx2csv.__name__       : ".\\data\\funda_csv"
    }