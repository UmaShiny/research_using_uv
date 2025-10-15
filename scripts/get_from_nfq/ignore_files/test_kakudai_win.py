import win32gui
import win32api
import time

def get_relative_to_topright(hwnd, point):
    # ウィンドウの矩形
    left, top, right, bottom = win32gui.GetWindowRect(hwnd)
    print(left, top, right, bottom)

    # 基準点（右上）
    base_x, base_y = right, top
    
    # point はスクリーン座標 (x, y)
    x, y = point
    rel_x = x - base_x
    rel_y = y - base_y
    return (rel_x, rel_y)

# 例: Excelウィンドウ
hwnd = 265120

# クリックした位置（スクリーン座標だとする）
time.sleep(5)
x, y = win32api.GetCursorPos()
point = (x, y)

rel = get_relative_to_topright(hwnd, point)
print("右上基準での相対座標:", rel)
