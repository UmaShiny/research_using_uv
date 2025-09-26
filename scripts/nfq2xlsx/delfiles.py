from scripts.nfq2xlsx.pynfq import pyNFQ as nfq
from pathlib import Path
from scripts.nfq2xlsx.Config import main_Constant as tc

def test_filedel() -> None:
    try: 
        for _, val in tc.DST_DIRPATH_DICT.items():
            if val == tc.SRC_DIRPATH_DICT[nfq.repair_nfqxlsx.__name__]: 
                raise IndexError(f"you must remain dict index: \"{val}\"")
            folder = Path(val)  # 対象のフォルダを指定

            for f in folder.iterdir():  # 直下の中身を順番にチェック
                if f.is_file():        # ファイルなら削除
                    f.unlink()
    except Exception as e_inner:
        print(f"UnExcpected Error: {e_inner}")
        print("You may have failed to delete files in the following folder.")
        for _, val in tc.DST_DIRPATH_DICT.items():
            print(val)
        raise
    else: print("delete files completed")

if __name__ == "__main__":
    test_filedel()