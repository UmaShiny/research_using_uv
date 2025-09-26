from pathlib import Path
import openpyxl as pl
from Config import Constant as cc


def add_new_xlsx(xlsx_path: Path, new_xlsx_path: Path) -> None:
    try:
        wb = pl.load_workbook(xlsx_path)
        ws = wb.active
        if ws is None:
            raise ValueError("Worksheet is None")

        # 行の削除
        for col in cc.REMOVE_COLUMN_FOR_XLSX2CSV[::-1]:
            ws.delete_cols(col)

        # new_xlsx_path末尾に保存
        wb.save(new_xlsx_path)
    except Exception as e:
        print(f"Unexpected Error: {e}")
        raise
    else:
        print(f"add_new_xlsx completed: {new_xlsx_path}")
    finally:
        wb.close()
