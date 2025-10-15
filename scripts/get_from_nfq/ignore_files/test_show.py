import win32gui

# 子ウィンドウを再帰的に列挙する関数
def enum_all_child_windows(hwnd, level=0):
    # 現在のウィンドウのタイトルを取得
    title = win32gui.GetWindowText(hwnd)
    print(f"{'  ' * level}HWND: {hwnd}, Title: '{title}', Level: {level}")

    # 子ウィンドウを列挙
    def enum_children_callback(child_hwnd, extra):
        enum_all_child_windows(child_hwnd, level + 1)

    # 子ウィンドウを列挙
    win32gui.EnumChildWindows(hwnd, enum_children_callback, None)

# 親ウィンドウのHWNDを取得する関数（ここではメモ帳を例として取得）
def find_notepad_window():
    def callback(hwnd, extra):
        if "レポート表示" in win32gui.GetWindowText(hwnd):
            extra.append(hwnd)
    hwnds = []
    win32gui.EnumWindows(callback, hwnds)
    return hwnds[0] if hwnds else None

# 親ウィンドウを特定
parent_hwnd = find_notepad_window()
if parent_hwnd:
    # 親ウィンドウから再帰的に子ウィンドウを列挙
    enum_all_child_windows(parent_hwnd)
else:
    print("メモ帳が見つかりませんでした。")

