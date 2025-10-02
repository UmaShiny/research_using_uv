import zipfile
from pathlib import Path
import re
import pandas as pd
import pdfplumber as pp
from jpx_config import constant as cfg
import time

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

    @staticmethod
    def jpxUtil_extract_table(pdf: pp.PDF) -> list[str]:
        """カラム名の両端座標と、値の両端座標の距離が最短になるように、カラム名と値を紐づけ、もし紐づけられなかったカラムがあった場合は、値NaNを入れる"""

        def __helper_y_grouping(chars: list[dict]) -> list[list[dict]]:
            sorted_chars = sorted(chars, key=lambda x: (x['top'], x['x0']))

            # 行ごとに文字をグループ化（y座標順にソート）
            lines = []
            current_line = []
            prev_y = None
            for ch in sorted_chars:
                y = ch["top"]
                if prev_y is None or abs(y - prev_y) < cfg.extract_y_tolerance:  # 誤差許容
                    current_line.append(ch)
                else:
                    lines.append(current_line)
                    current_line = [ch]
                prev_y = y
            if current_line:
                lines.append(current_line)

            return lines[1:]  # 1行目は不要なので除外

        def __helper_get_every_column_width(lines: list[dict]) -> list[tuple[int, int]]:
            # カラムの両端座標のリスト
            space_list = [(a["x1"], b["x0"]) for a, b in zip(column_line[:-1], column_line[1:]) if int(abs(b['x0'] - a['x1'])) > 0]
            space_list.append((column_line[0]["x0"], column_line[-1]["x1"]))  # 先頭と末尾のスペースも追加
            sorted_space_list = sorted([item for sublist in space_list for item in sublist])
            column_width = list(zip(sorted_space_list[::2], sorted_space_list[1::2]))
            return column_width

        def __helper_x_grouping(lines: list[list[dict]], column_width: list[tuple[int, int]]) -> list[str]:

            def __helper_set_index(words: list[dict]) -> list[dict]:
                word_index_tmp = []
                proximity = []
                for word in words:
                    x0:float = word[0]['x0']
                    x1:float = word[-1]['x1']
                    for i, (col_start, col_end) in enumerate(column_width):
                        proximity.append(abs(x0 - col_start) + abs(x1 - col_end))
                    word_index = proximity.index(min(proximity))
                    word_index_tmp.append((word_index, word))
                    proximity = []
                for index in range(len(cfg.fmt_1_config.header)):
                    if index not in [wi[0] for wi in word_index_tmp]:
                        word_index_tmp.append((index, []))  # 値がない場合は空リストを追加
                
                word_index_tmp = sorted(word_index_tmp, key=lambda x: x[0])  # インデックス順にソート
                word_index = []
                for wi in word_index_tmp:
                    word_index.append(''.join([ch['text'] for ch in wi[1]]) if wi[1] else '')
                return word_index

            # 列ごとに文字をグループ化（x座標順にソート）
            rows = []
            for line in lines:  # 不要な行を除外
                line = sorted(line, key=lambda x: x['x0'])  # x座標順にソート
                current_word = []
                prev_x = None
                words = []
                for ch in line:
                    x = ch["x0"]
                    if prev_x is None or abs(x - prev_x) < cfg.extract_x_tolerance:  # 誤差許容
                        current_word.append(ch)
                    else:
                        words.append(current_word)
                        current_word = [ch]
                    prev_x = ch["x1"]
                if current_word:
                    words.append(current_word)
                rows.append(words)
            
            for i, row in enumerate(rows):
                rows[i] = __helper_set_index(row)
            
            return rows

        all_rows = []

        for page in pdf.pages:

            chars = page.chars

            lines = __helper_y_grouping(chars)

            column_line = lines[0]

            column_width = __helper_get_every_column_width(column_line)

            only_record = lines[1:]

            rows = __helper_x_grouping(only_record, column_width)

            all_rows.extend(rows)

        return all_rows


    def __init__(self, processed_jpx_dir: str = 'data/processed_jpx', output_csv_dir: str = 'data/jpx_dataset') -> None:
        self.processed_jpx_dir = Path(processed_jpx_dir)
        self.output_csv_dir = Path(output_csv_dir)


    @classmethod
    def pdf2csv(cls, jpx_pdf_dir: str, output_csv_dir: str) -> None:

        # load all PDF files
        all_pdf_paths = [f for f in Path(jpx_pdf_dir).rglob('*') if f.is_file() and f.suffix == '.pdf']
        print(f"Found {len(all_pdf_paths)} PDF files in {jpx_pdf_dir}")

        # initialize empty list to store extracted table data
        table: list[str] = []

        # get all tables from each PDF file
        for pdf_path in all_pdf_paths:
            print("\r Processing file:", pdf_path.name, end="")
            with pp.open(pdf_path) as pdf:
                time.sleep(0.1)  # to avoid potential file access issues
                table.extend(cls.jpxUtil_extract_table(pdf))
        
        # save to CSV
        df = pd.DataFrame(table, columns=cfg.fmt_1_config.header)
        output_path = Path(output_csv_dir) / f"{__name__}_{time.time()}.csv"
        df.to_csv(output_path, index=False, encoding='shift_jis')
        print(f"\nSaved extracted table to {output_path}")