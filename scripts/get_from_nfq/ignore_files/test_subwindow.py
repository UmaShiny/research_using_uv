import win32gui
import pyautogui

def enum_child_windows(parent_hwnd):
    child_windows = []

    def callback(hwnd, _):
        child_windows.append((hwnd, win32gui.GetWindowText(hwnd)))

    win32gui.EnumChildWindows(parent_hwnd, callback, None)
    return child_windows

# 例: 特定のウィンドウ（例: メモ帳）を取得
def find_notepad_window():
    def callback(hwnd, extra):
        if "レポート表示" in win32gui.GetWindowText(hwnd):
            extra.append(hwnd)
    hwnds = []
    win32gui.EnumWindows(callback, hwnds)
    return hwnds[0] if hwnds else None

def print_window_info(hwnd):
    title = win32gui.GetWindowText(hwnd)
    class_name = win32gui.GetClassName(hwnd)
    is_visible = win32gui.IsWindowVisible(hwnd)

    print(f"HWND: {hwnd}, Title: '{title}', Class: {class_name}, Visible: {is_visible}")

# hwnd からウィンドウの位置とサイズを取得
def get_window_position(hwnd):
    # ウィンドウの位置とサイズを取得（左上の座標と右下の座標）
    rect = win32gui.GetWindowRect(hwnd)
    return rect  # (left, top, right, bottom)

# クリックする位置を決める
def click_window(hwnd):
    rect = get_window_position(hwnd)
    # 左上の座標 (rect[0], rect[1]) を使ってクリック
    # 画面中央付近をクリックする場合（調整も可能）
    x = rect[0] + (rect[2] - rect[0]) // 2  # 中央
    y = rect[1] + (rect[3] - rect[1]) // 2  # 中央
    pyautogui.click(x, y)


parent_hwnd = find_notepad_window()
if parent_hwnd:
    children = enum_child_windows(parent_hwnd)
    for hwnd, title in children:
        # print(f"HWND: {hwnd}, Title: {title}")
        print_window_info(hwnd)
else:
    print("メモ帳が見つかりませんでした。")


# hwnd = 265120
# click_window(265120)

"""
    HWND: 265120, Title: 'FqReport1.xlsx', Level: 2
      HWND: 330614, Title: '', Level: 3
        HWND: 265128, Title: '', Level: 4
        HWND: 265126, Title: '', Level: 4
      HWND: 265128, Title: '', Level: 3
      HWND: 265126, Title: '', Level: 3
    HWND: 330614, Title: '', Level: 2
      HWND: 265128, Title: '', Level: 3
      HWND: 265126, Title: '', Level: 3
    HWND: 265128, Title: '', Level: 2
    HWND: 265126, Title: '', Level: 2
  HWND: 265120, Title: 'FqReport1.xlsx', Level: 1
    HWND: 330614, Title: '', Level: 2
      HWND: 265128, Title: '', Level: 3
      HWND: 265126, Title: '', Level: 3
    HWND: 265128, Title: '', Level: 2
    HWND: 265126, Title: '', Level: 2
  HWND: 330614, Title: '', Level: 1
    HWND: 265128, Title: '', Level: 2
    HWND: 265126, Title: '', Level: 2
  HWND: 265128, Title: '', Level: 1
  HWND: 265126, Title: '', Level: 1
"""

"""
Desktop
 ├─ Excel メインウィンドウ (HWND 265120, "FqReport1.xlsx")
 │   ├─ 子ウィンドウ (HWND 330614, "")
 │   │   ├─ 子ウィンドウ (HWND 265128, "")
 │   │   └─ 子ウィンドウ (HWND 265126, "")
 │   ├─ 子ウィンドウ (HWND 265128, "")
 │   └─ 子ウィンドウ (HWND 265126, "")
 ├─ 別のウィンドウ (HWND 330614, "")
 │   ├─ 子 (HWND 265128, "")
 │   └─ 子 (HWND 265126, "")
 ├─ (HWND 265128, "")
 └─ (HWND 265126, "")

"""