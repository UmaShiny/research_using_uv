from jpx_config import constant as const
from jpx_config import table_format
from pathlib import Path
from jpx_config import fmt_1, fmt_2, fmt_3, fmt_4, fmt_5
import pdfplumber as pp
import subprocess

class extract_table_util:

    class core:

        @staticmethod
        def merge_buy_sell_if_needed(words: list[list[dict[str, float | int | str]]]) -> None:
            words_tmp = ["".join([txt["text"] for txt in wi if isinstance(txt["text"], str)]) for wi in words]

            if bool(set(words_tmp) & set(["ｶ"])):
                buy_sell_index = words_tmp.index("ｶ")
            elif bool(set(words_tmp) & set(["ｳ"])):
                buy_sell_index = words_tmp.index("ｳ")
            else: # 「買」「売」のどちらも存在しない場合
                buy_sell_index = -1
            
            if buy_sell_index > -1:
                # 売り気配である「買」「売」のどちらかが存在する場合、後続の要素のindexもbuy_sell_indexに固定する
                words[buy_sell_index].extend(words[buy_sell_index + 1])
                del words[buy_sell_index + 1]

        @staticmethod
        def calculate_proximity(word_index_tmp: list, words: list[dict], column_width: list[tuple[int, int]]) -> None:
            for word in words:

                index:int = 0
                proximity = [] # 各カラムとwordの距離を格納するリスト
                x0:float = word[0]['x0']
                # x1_tmp:float = word[0]["x1"]
                x1:float = word[-1]['x1']

                decided_index_flag = False # indexが決定したかどうかのフラグ
                for i, (col_start, col_end) in enumerate(column_width):
                    # ひとまず、カラムの両端座標とwordの両端座標の距離の和を格納しておく
                    proximity.append(abs(x0 - col_start) + abs(x1 - col_end))

                    if decided_index_flag:
                        continue
                    
                    if word[0]["adv"] > 4:
                        index = 2
                        decided_index_flag = True
                    else:
                        if (x0 >= col_start and x0 <= col_end) or (x1 >= col_start and x1 <= col_end): # wordの先頭か末尾がカラム内に完全に収まっている場合
                        # if x0 >= col_start and x1 <= col_end: # wordの先頭か末尾がカラム内に完全に収まっている場合
                            # proximity[-1] = 0 # 調子が悪いときは、上の条件式を交換した後、ここをコメントアウト
                            index = i
                            decided_index_flag = True
                        else: # wordの先頭も末尾もカラム内に収まっていない場合
                            index = proximity.index(min(proximity)) # 最も近いカラムのindexを取得している

                word_index_tmp.append((index, word, proximity))
            return

        @staticmethod
        def resolve_index_conflict(word_index_tmp: list[tuple[int, list[dict[str, float | int | str]], list[int]]]) -> None:

            def is_conflict() -> bool:
                return len([wi[0] for wi in word_index_tmp]) > len(set([wi[0] for wi in word_index_tmp]))
            

            while is_conflict(): # indexに重複がある限りループ
                prev_info = word_index_tmp[0]
                for word_info in word_index_tmp[1:]:
                    for i in range(1, len(word_index_tmp[1:])):
                        if word_info[0] == prev_info[0]: # index is duplicated

                            # 後発の方がproximityが小さい -> 先発の方を理論上の最大値にする
                            if word_info[2][word_info[0]] < prev_info[2][prev_info[0]]:
                                prev_info_tmp = prev_info # 最小のproximityを理論上の最大値にするための一時変数
                                prev_info_tmp[2][prev_info[0]] = max(prev_info[2]) + 1 # 最小のproximityを理論上の最大値にする
                                word_index_tmp[i-1] = (prev_info_tmp[2].index(min(prev_info_tmp[2])),) + word_index_tmp[i-1][1:] # 元のリストに反映
                            
                            # 先発の方がproximityが小さい -> word_infoの方を理論上の最大値にする
                            else:
                                word_info_tmp = word_info # 最小のproximityを理論上の最大値にするための一時変数
                                word_info_tmp[2][word_info[0]] = max(word_info[2]) + 1 # 最小のproximityを理論上の最大値にする
                                word_index_tmp[i] = (word_info_tmp[2].index(min(word_info_tmp[2])),) + word_index_tmp[i][1:] # 元のリストに反映
                            
                            # indexの重複を解消したかどうかを確認する
                            if not is_conflict():
                                return
                        
                        # このforループの最後にprev_infoを更新する
                        prev_info = word_info

        @staticmethod
        def set_index(words: list[dict], column_width: list[tuple[int, int]], fmt: str) -> list[str]:
            word_index_tmp = [] # (index, word, proximity)のタプルのリスト
            word_index = [] # indexに対応するwordのリスト

            # 各カラムとwordの距離を計算し、最も近いカラムのindexをwordに紐づける
            extract_table_util.core.calculate_proximity(word_index_tmp, words, column_width)
            
            # indexの重複を解消（proximityが最小のものを優先）
            extract_table_util.core.resolve_index_conflict(word_index_tmp)
            
            # カラムに対応する値がなかった場合は空リストを追加
            for index in range(len(const.fmt_config_map[fmt].header)):
                if index not in [wi[0] for wi in word_index_tmp]:
                    word_index_tmp.append((index, [], None))  # 値がない場合は空リストを追加
            
            # テキスト情報から文字列に変換する
            word_index_tmp.sort(key=lambda x: x[0])
            for wi in word_index_tmp:
                word_index.append(''.join([ch['text'] for ch in wi[1]]) if wi[1] else '')
            
            return word_index

        @staticmethod
        def update_prev_ch(prev_ch: dict) -> tuple[float, float, float]:
            prev_x = prev_ch["x1"]
            prev_width = prev_ch["width"]
            prev_adv = prev_ch["adv"]
            return prev_x, prev_width, prev_adv

        @staticmethod
        def match_context(curr_ch: dict, prev_x1: float, prev_width: float, prev_adv: float) -> bool:
            curr_ch["adv"] = prev_adv if curr_ch["text"] == "." and curr_ch["adv"]*3 > prev_adv else curr_ch["adv"] # 小数点のadv情報を前の文字のadv情報に合わせる
            curr_ch["adv"] = prev_adv if curr_ch["text"] == "E" and curr_ch["adv"] > prev_adv else curr_ch["adv"] # 小数点のadv情報を前の文字のadv情報に合わせる
            curr_ch["adv"] = prev_adv if curr_ch["text"] == "+" and curr_ch["adv"] > prev_adv else curr_ch["adv"] # 小数点のadv情報を前の文字のadv情報に合わせる
            criteria_1 = -prev_width < curr_ch["x0"] - prev_x1 <= const.extract_x_tolerance
            criteria_2 = prev_adv == curr_ch["adv"] # 前後でadv情報が同じである場合    
            if criteria_1 and criteria_2:
                return True
            return False

        @staticmethod
        def not_match_context(curr_ch: dict, prev_x1: float, prev_width: float, prev_adv: float) -> bool:
            criteria_1 = -prev_width <= curr_ch["x0"] - prev_x1 <= 0.012
            criteria_2 = prev_adv != curr_ch["adv"]
            if criteria_1 and criteria_2:
                return True
            return False

        @staticmethod
        def update_tmp_line(pass_ch_list: list[dict], tmp_line: list[dict]) -> None:
            """pass_ch_listに一時的に格納した文字をtmp_lineの先頭に戻し、pass_ch_listをクリアする"""
            for pc in pass_ch_list[::-1]:
                tmp_line.insert(0, pc)  
            pass_ch_list.clear()
        
        @staticmethod
        def iscontinuous(tmp_line: list[dict], pass_ch_list: list[dict]) -> bool:
            criteria_1 = len(tmp_line) == 1
            criteria_2 = len(pass_ch_list) == 0
            if criteria_1 and criteria_2:
                return False
            return True
        
        @staticmethod
        def isfinal(tmp_line: list[dict], pass_ch_list: list[dict]) -> bool:
            return not extract_table_util.core.iscontinuous(tmp_line, pass_ch_list)


    @staticmethod
    def y_grouping(chars: list[dict], fmt: fmt_1 | fmt_2 | fmt_3 | fmt_4 | fmt_5) -> tuple[list[list[dict]], bool]:
        """y軸ごとに文字をグループ化し、行ごとのリストを返す"""

        sorted_chars = sorted(chars, key=lambda x: (x['top'], x['x0'])) # sorted_chars : 左上が始点となり、右下へ読み進められるようソート
        lines = []                                                      # lines : ｙ値ごとのリスト
        current_line = []                                               # current_line : 現在のｙ値に対応する行の文字を格納するリスト
        prev_y = None                                                   # prev_y : 直前の文字のｙ値

        for ch in sorted_chars:
            y = ch["top"] # 文字のｙ値を取得
            if prev_y is None or abs(y - prev_y) < const.extract_y_tolerance:  # 誤差許容と直前のｙ値と現在のｙ値の比較をする
                current_line.append(ch) # 誤差許容内であれば同じ行とみなす
            else:
                lines.append(current_line) # 誤差許容内でなければ違う行とみなす
                current_line = [ch] # 新しい行のリストを開始するための再代入
            prev_y = y # y値の更新
        if current_line:
            lines.append(current_line) # 最後の行を追加

        return fmt.return_lines_have_cols(lines)

    @staticmethod
    def get_every_column_width(column_line: list[dict], fmt:str) -> list[tuple[int, int]]:
        # カラムの両端座標のリスト
        space_list = []
        # distance_list = [round(a["x1"] - b["x0"], 2) for a, b in zip(column_line[:-1], column_line[1:]) if abs(b['x0'] - a['x1']) > 0]
        for a, b in zip(column_line[:-1], column_line[1:]):
            if round(abs(b['x0'] - a['x1']), 1) > 0:
                space_list.append((b['x0'], a['x1']))
            elif round(abs(b['x0'] - a['x1']), 1) < 0:
                space_list.append((b['x0']-(5.64/2), a['x1']))
            else:
                continue

        space_list.append((column_line[0]["x0"], column_line[-1]["x1"]))  # 先頭と末尾のスペースも追加
        sorted_space_list = sorted([item for sublist in space_list for item in sublist])
        column_width = list(zip(sorted_space_list[::2], sorted_space_list[1::2]))
        # カラム数の確認
        if len(column_width) != len(const.fmt_config_map[fmt].header):
            raise ValueError(f"Column count mismatch: expected {len(const.fmt_config_map[fmt].header)}, got {len(column_width)}")

        return column_width

        
    @staticmethod
    def x_grouping(lines: list[list[dict]], column_width: list[tuple[int, int]], fmt: fmt_1 | fmt_2 | fmt_3 | fmt_4 | fmt_5) -> list[list[str]]:
        """列ごとに文字をグループ化（x座標順にソート）し、カラムに紐づける"""
        rows_tmp: list[list[dict]] = [] # rows_tmp : 各行ごとの「文字情報リスト」を格納する一時的な二次元リスト
        rows: list[list[str]] = []      # rows : 各行ごとの「文字列」を格納する二次元リスト
            
        # fmt_4, fmt_5の場合
        if fmt.name in ["fmt_4", "fmt_5"]:
            print(f"date : {fmt.pdf_path.name}")
            for line in lines:

                if "".join([ch['text'] for ch in line])[:8] != str(fmt.origin_file_date):
                    continue # その行がファイルに対応する日付データでない場合はスキップする   

                prev_ch, tmp_line = line[0], line[1:]
                tmp = [prev_ch]
                (prev_x1, prev_width, prev_adv) = extract_table_util.core.update_prev_ch(prev_ch)
                pass_ch_list = []
                words = []

                while True:

                    if len(tmp_line) == 0: break # 処理対象がなくなった場合、whileループを抜ける
                    curr_ch = tmp_line[0]

                    if extract_table_util.core.match_context(curr_ch, prev_x1, prev_width, prev_adv): # 文字同士が重なっていない場合
                        tmp.append(curr_ch)
                        if len(tmp_line) == 1:
                            words.append(tmp)
                            if extract_table_util.core.iscontinuous(tmp_line, pass_ch_list): # まだ処理すべき文字が存在する場合
                                extract_table_util.core.update_tmp_line(pass_ch_list, tmp_line)
                                tmp_line = tmp_line[:-1]
                                curr_ch = tmp_line[0]
                                tmp = [curr_ch]
                        (prev_x1, prev_width, prev_adv) = extract_table_util.core.update_prev_ch(curr_ch)
                
                    elif extract_table_util.core.not_match_context(curr_ch, prev_x1, prev_width, prev_adv): # 文字同士が重なっている場合
                        pass_ch_list.append(curr_ch)

                    else: # 文字が区切りのタイミング（1. 要素の終端　2. 行の終端）
                        words.append(tmp)
                        if extract_table_util.core.iscontinuous(tmp_line, pass_ch_list): # まだ処理すべき文字が存在する場合
                            extract_table_util.core.update_tmp_line(pass_ch_list, tmp_line)
                            curr_ch = tmp_line[0]
                            tmp = [curr_ch]
                            (prev_x1, prev_width, prev_adv) = extract_table_util.core.update_prev_ch(curr_ch)
                        else: # もう処理すべき文字が存在しない場合
                            tmp = [curr_ch]
                            words.append(tmp)

                    del tmp_line[0] # 処理済みの先頭の文字を消去する

                rows_tmp.append(words)

            for row_tmp in rows_tmp:
                row = extract_table_util.core.set_index(row_tmp, column_width, fmt.name) # 要素をカラムに紐づけたリストを取得
                rows.append(row) # rows（各行ごとの「文字列」）を二次元リスト追加

            
        # fmt_1, fmt_2, fmt_3の場合
        elif fmt.name in ["fmt_1", "fmt_2", "fmt_3"]:
            for line in lines:
                # line = sorted(line, key=lambda x: x['x0']) # line : x座標順にソートされた行の文字情報リスト
                current_word = []                            # current_word : 直前の文字情報
                prev_x1 = None                               # prev_x1 : 直前の文字のx1座標
                words = []                                   # words : 行内の単語ごとの文字情報リスト
                
                for curr_ch in line:
                    x = curr_ch["x0"] # 文字のx0座標を取得
                    if prev_x1 is None or (x - prev_x1) < const.extract_x_tolerance:  # 誤差許容と直前のx0座標と現在のx0座標の比較をする
                        current_word.append(curr_ch) # 誤差許容内であれば同じ単語とみなす
                    else:
                        words.append(current_word) # 誤差許容内でなければ違う単語とみなす
                        current_word = [curr_ch] # 新しい単語のリストを開始するための再代入
                    prev_x1 = curr_ch["x1"] # x1座標の更新
                
                if current_word: 
                    words.append(current_word) # 行の最後の「文字情報リスト」を追加

                extract_table_util.core.merge_buy_sell_if_needed(words) # 「買」「売」のどちらかが存在する場合、これを結合する
                rows_tmp.append(words) # words（文字情報リスト）を一時的な二次元リストに追加

                for row_tmp in rows_tmp:
                    row = extract_table_util.core.set_index(row_tmp, column_width, fmt.name) # 要素をカラムに紐づけたリストを取得
                    rows.append(row) # rows（各行ごとの「文字列」）を二次元リスト追加
            
        else:
            raise ValueError(f"Unsupported format: {fmt.name}")

        return rows
    
    @classmethod
    def isPdfBroken(cls, fmt: fmt_1 | fmt_2 | fmt_3 | fmt_4 | fmt_5) -> tuple[bool, Path]:
        """PDFファイルが壊れているかどうかを確認し、壊れている場合はcpdfを用いて再生成する"""
        path_to_file = fmt.pdf_path
        tmp_pdf = pp.open(path_to_file)
        if tmp_pdf.metadata == {} and tmp_pdf.pages == []:
            
            # PDFファイルが壊れている場合、cpdfを用いて再生成する
            command = [
                const.path_to_cpdf, # cpdfの実行ファイル名であり、別途インストールが必要
                "gswin64c", # Ghostscriptの実行ファイル名であり、別途インストールが必要
                "-o", 
                f"{fmt.pdf_path.parent}\\tmp_{fmt.pdf_path.stem}.pdf", 
                str(fmt.pdf_path)
            ]
            
            subprocess.call(command, timeout=60) # 60秒以内に処理が終わらなければタイムアウトさせる
            is_broken = True
            pdf_path = Path(f".\\data\\extracted_jpx\\{fmt.name}\\tmp_{fmt.pdf_path.stem}.pdf")
        else: 
            is_broken = False
            pdf_path = fmt.pdf_path
        
        tmp_pdf.close()

        return (is_broken, pdf_path)
