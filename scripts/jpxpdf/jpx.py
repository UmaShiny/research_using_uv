import zipfile
from pathlib import Path
import re
import pandas as pd
import pdfplumber as pp
from jpx_config import constant as const
from jpx_config import table_format
from jpx_config import fmt_1, fmt_2, fmt_3, fmt_4, fmt_5
from util.jpx_util import extract_table_util as et_util
import time
import gc


class file:

    def __init__(self, raw_jpx_dir: str = 'data/raw_jpx', processed_jpx_dir: str = 'data/processed_jpx') -> None:
        self.raw_jpx_dir = Path(raw_jpx_dir)
        self.processed_jpx_dir = Path(processed_jpx_dir)

    def extract_jpx(self) -> None:
        raw_jpx_zip = [f for f in self.raw_jpx_dir.rglob('*') if f.is_file() and f.suffix == '.zip']

        for zip_path in raw_jpx_zip:
            with zipfile.ZipFile(zip_path, 'r') as zip_ref:
                zip_ref.extractall(self.processed_jpx_dir)

    def Adjust_names(self) -> None:
        jpx_files = [f for f in self.processed_jpx_dir.rglob('*') if f.is_file() and f.suffix == '.pdf']

        for file_path in jpx_files:
            new_name = re.sub(pattern=r".+(\d{8}.pdf)", repl=r"\1", string=file_path.name)
            new_path = file_path.with_name(new_name)
            file_path.rename(new_path)
            print(f"Renamed {file_path.name} to {new_name}")


class dataset:

    def __init__(self) -> None:
        pass

    @classmethod
    def start_processing(cls, fmt: table_format) -> bool:
        start_flag = False
        if const.progress: 
            pdf_date_ydf = int(Path(fmt.pdf_path).stem)
            if pdf_date_ydf >= const.start_file_stem: 
                start_flag = True
            else:
                return False
        else: 
            start_flag = True

        return start_flag
    
    @classmethod
    def split_pdf_by_date(cls, fmt: fmt_4) -> None:
        pdf_path = fmt.pdf_path
        if fmt.origin_file_date < 999999:
            fmt.split_pdf_by_date_iter(pdf_path)
            gc.collect()
            return 
        else:
            print(f"Already split: {fmt.file_date} -> {fmt.origin_file_date}")

    @staticmethod
    def jpxUtil_extract_table(fmt: fmt_1 | fmt_2 | fmt_3 | fmt_5) -> list[list[str]]:
        """カラム名の両端座標と、値の両端座標の距離が最短になるように、カラム名と値を紐づけ、もし紐づけられなかったカラムがあった場合は、値NaNを入れる"""

        fmt_name = fmt.name # fmt_1, fmt_2, fmt_3, fmt_4のいずれか

        all_rows: list[list[str]] = [] # 全ページのデータを格納する二次元リスト

        is_broken, pdf_path = et_util.isPdfBroken(fmt)

        column_width: list[tuple[int, int]] # 各カラムの占める文字面積のx軸における両端座標のリスト

        with pp.open(pdf_path) as pdf:
            
            time.sleep(fmt.sleep_time) # PDF読み込みの安定化のために少し待つ

            # column_width: list[tuple[int, int]] # 各カラムの占める文字面積のx軸における両端座標のリスト
            records: list[list[dict]] # データ全体のうち、カラム名を除いた部分

            for page in pdf.pages:
                
                # y軸ごとに文字をグループ化
                chars = page.chars
                lines, have_cols = et_util.y_grouping(chars, fmt)

                # カラムの両端座標のリストを取得
                if have_cols: 
                    column_line = lines[0]
                    column_width = et_util.get_every_column_width(column_line, fmt_name)
                    records = lines[1:]
                else:
                    records = lines

                # x軸ごとに文字をグループ化して、カラムに紐づける
                rows = et_util.x_grouping(records, column_width, fmt)

                # rowsは多段のrowであり、テーブル状のデータになっているので、行単位に解して追加
                all_rows.extend(rows)

            # 「銘柄略称」の項目は複数行にまたがっている場合があるため、これを一行にまとめる処理を実行する
            fmt.make_rows_single_line(all_rows)

            
        if is_broken:
            Path(f"{fmt.pdf_path.parent}\\tmp_{fmt.pdf_path.stem}.pdf").unlink() # 一時的に生成したPDFファイルを削除する

        return all_rows


    @staticmethod
    def jpxUtil_save_table_as_csv(fmt: fmt_1 | fmt_2 | fmt_3 | fmt_5, table: list[list[str]], output_csv_dir: str) -> None:
        """抽出したテーブルデータをcsvファイルとして保存する"""

        def save_df2csv(date: str, table: list[list[str]]) -> None:
            df = pd.DataFrame(data=table, columns=const.fmt_config_map[fmt.name].header)
            output_path = Path(output_csv_dir) / f"{date}.csv"
            df.to_csv(output_path, index=False)
            print(f"{'\033[92m'}Saved extracted table to {output_path}{'\033[0m'}\n")

        if fmt.name == "fmt_5":
            table.sort(key=lambda x: x[1])

        if len(fmt.pdf_path.stem) == 6:
            split_table_by_date: dict[str, list[list[str]]] = {}
            for row in table[1:]:
                date = row[0]
                if date not in split_table_by_date:
                    split_table_by_date[date] = []
                split_table_by_date[date].append(row)
            for date, table in split_table_by_date.items():
                save_df2csv(date, table)
        else:
            date = fmt.pdf_path.stem
            save_df2csv(date, table)


    @classmethod
    def pdf2csv(cls, jpx_pdf_dir: str, output_csv_dir: str) -> None:

        # すべてのPDFファイルを取得する
        all_pdf_paths = [f for f in Path(jpx_pdf_dir).rglob('*') if f.is_file() and f.suffix == '.pdf']
        print(f"Found {len(all_pdf_paths)} PDF files in {jpx_pdf_dir}")
        split_flag = False

        # csvファイルに順次変換して保存
        for pdf_path in all_pdf_paths:
            gc.collect() # ガベージコレクションを実行してメモリを解放する
            
            # JPXのPDFファイルの公開日付に応じたフォーマットを取得
            fmt = table_format(pdf_path).fmt_type

            if isinstance(fmt, fmt_4):
                cls.split_pdf_by_date(fmt)
                split_flag = True
                continue

            # もし最後の処理が中断されていた場合は、ここで判定して再開させることができる
            if cls.start_processing(fmt) is False: 
                continue

            print("Processing file:", pdf_path.name)

            # ここで二次元に加工されたPDFデータを抽出する
            table = cls.jpxUtil_extract_table(fmt=fmt)

            # 抽出したテーブルデータをcsvファイルとして保存する
            cls.jpxUtil_save_table_as_csv(fmt=fmt, table=table, output_csv_dir=output_csv_dir)
        
        print("All files have been processed.")


        if split_flag:
            tmp_dir = Path(jpx_pdf_dir) / f"tmp_{fmt.name}"
            cls.pdf2csv(
                jpx_pdf_dir=str(tmp_dir),
                output_csv_dir=output_csv_dir
            )