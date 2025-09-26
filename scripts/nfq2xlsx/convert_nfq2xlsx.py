from pynfq import pyNFQ as nfq
from Delfiles import test_filedel
from Config import Path as cp
from Config import Constant as cc


def main(repair: bool = True, xlsx2csv: bool = True):
    try:
        pyNFQ_obj = nfq(path_to_ticker_symbol_csv=cp.TICKER_SYMBOL_CSV_PATH)

        if cc.REPAIR:
            pyNFQ_obj.repair_nfqxlsx(
                src_dirpath=cp.SRC_DIRPATH_DICT[nfq.repair_nfqxlsx.__name__],
                dst_dirpath=cp.DST_DIRPATH_DICT[nfq.repair_nfqxlsx.__name__],
                folder_exist_check=True,
            )
            print(f"test: {nfq.repair_nfqxlsx.__name__} ok")

        if cc.XLSX2CSV:
            pyNFQ_obj.xlsx2csv(
                src_dirpath=cp.SRC_DIRPATH_DICT[nfq.xlsx2csv.__name__],
                dst_dirpath=cp.DST_DIRPATH_DICT[nfq.xlsx2csv.__name__],
                remove_column=cc.REMOVE_COLUMN_FOR_XLSX2CSV,
                remove_row=cc.REMOVE_ROW_FOR_XLSX2CSV,
            )
            print(f"test: {nfq.xlsx2csv.__name__} ok")

    except Exception as e_outer:
        print(f"UnExcpected Error: {e_outer}")
    finally:
        delete_files_question: str | None = None
        while delete_files_question not in ("y", "n"):
            delete_files_question = input(
                "Do you delete generated files? [y/n] >> "
            ).lower()
        if delete_files_question == "y":
            test_filedel()
        print("test is done")


if __name__ == "__main__":
    main()
