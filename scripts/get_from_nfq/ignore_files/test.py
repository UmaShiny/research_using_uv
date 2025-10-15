import win32api
import win32gui
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

time.sleep(5)

hwnd = win32gui.GetForegroundWindow()
# hwnd = 265120

title = win32gui.GetWindowText(hwnd)

print(f"hwnd_title: [{title}]")

x, y = win32api.GetCursorPos()

rel_x, rel_y = win32gui.ScreenToClient(hwnd, (x, y))

# rel_x, rel_y = get_relative_to_topright(hwnd, (x, y))
# print(rel_x, rel_y)
print(f"coordinates: {rel_x}, {rel_y}")