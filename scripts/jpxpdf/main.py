import jpx
from jpx_config import table_format
from jpx_config import constant as const_cfg
from pathlib import Path
import pandas as pd

# jpx_obj = jpx.dataset.pdf2csv(
#     jpx_pdf_dir=const_cfg.tmp_fmt4_input_dir,
#     output_csv_dir=const_cfg.fmt4_output_dir
# )

ta_dataset_path = Path(const_cfg.jpx_dataset_path)
all_csv = [f for f in ta_dataset_path.rglob('*') if f.is_file() and f.suffix == '.csv']

header = [
    "年月日",
    "コード",
    "銘柄名",
    "前場始値",
    "前場高値",
    "前場安値",
    "前場終値",
    "後場始値",
    "後場高値",
    "後場安値",
    "後場終値",
]

exist_range_tuple = [
    (0, 3),
    (3, 7),
    (7, 11)
]

for i, csv in enumerate(all_csv):
    df = pd.read_csv(csv)
    print("\r", f"Processing {csv}...{i+1}/{len(all_csv)}", end="")
    range_df = df.iloc[:, 0:3]
    mask = range_df.isnull().any(axis=1)
    df_with_nan = range_df[mask]
    if not df_with_nan.empty:
        print(f"\nRows with NaN:\n{df_with_nan}\n")