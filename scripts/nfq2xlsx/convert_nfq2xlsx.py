from pathlib import Path
from scripts.nfq2xlsx.pynfq import pyNFQ as nfq
from scripts.nfq2xlsx.delfiles import test_filedel
from scripts.nfq2xlsx.Config import main_Constant as tc

try: 
    pyNFQ_obj = nfq(path_to_ticker_symbol_csv="TickerOnly.csv")

    pyNFQ_obj.repair_nfqxlsx(src_dirpath=tc.SRC_DIRPATH_DICT[nfq.repair_nfqxlsx.__name__],
                             dst_dirpath=tc.DST_DIRPATH_DICT[nfq.repair_nfqxlsx.__name__],
                             folder_exist_check=True)
    
    print(f"test: {nfq.repair_nfqxlsx.__name__} ok")

    pyNFQ_obj.xlsx2csv(src_dirpath=tc.SRC_DIRPATH_DICT[nfq.xlsx2csv.__name__],
                       dst_dirpath=tc.DST_DIRPATH_DICT[nfq.xlsx2csv.__name__],
                       remove_column=[1, 2, 4, 5],
                       remove_row=[1, 2, 3, 4, 5])
    
    print(f"test: {nfq.xlsx2csv.__name__} ok")

except Exception as e_outer:
    print(f"UnExcpected Error: {e_outer}")
finally:
    delete_files_question:str|None = None
    while delete_files_question not in ("y", "n"):
        delete_files_question = input("Do you delete generated files? [y/n] >> ").lower()
    if delete_files_question == "y": test_filedel()
    print("test is done")