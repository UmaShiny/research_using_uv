import win32api
import win32gui
import pyautogui
import time
import os

LOAD_SCRIPT_POINT_ABS       = (658, 327)
SELECT_FILE_POINT_REL       = (288, 238)
AUTORUN_BUTTON_POINT_ABS    = (821, 742)
CLOSE_LOG_POINT_REL         = (872, 564)
CLSOE_SELECT_FILE_POINT_REL = (919, 21)
DUR_TIME = 0.2

folder_path = "D:\\一時保存先\\project_py\\dst_nfq_copy"

def load_script():
    abs_p_x, abs_p_y = LOAD_SCRIPT_POINT_ABS
    pyautogui.moveTo(abs_p_x, abs_p_y, duration=DUR_TIME)
    pyautogui.click()

def select_file():
    hwnd = win32gui.FindWindow(None, "開く")
    left, top, _, _ = win32gui.GetWindowRect(hwnd)
    rel_p_x, rel_p_y = SELECT_FILE_POINT_REL
    abs_p_x, abs_p_y = left + rel_p_x, top + rel_p_y
    pyautogui.moveTo(abs_p_x, abs_p_y, duration=DUR_TIME)
    pyautogui.doubleClick()

def press_autorun_button():
    abs_p_x, abs_p_y = AUTORUN_BUTTON_POINT_ABS
    pyautogui.moveTo(abs_p_x, abs_p_y, duration=DUR_TIME)
    pyautogui.click()

def download_to_local():
    fail_num = 0
    while(fail_num < 60):
        time.sleep(1)
        hwnd = win32gui.GetForegroundWindow()
        if hwnd: 
            win_name = win32gui.GetWindowText(hwnd)
            if win_name == "データのダウンロード":
                pyautogui.press("y")
                fail_num = 0
            elif win_name == "自動運転":
                l, t, r, b = win32gui.GetWindowRect(hwnd)
                w, h = r-l, b-t
                if w > 350 or h > 200: continue
                pyautogui.press("Enter")
                return print("スクリプトが終了しました")
            else: fail_num += 1
    raise TimeoutError(f"異常終了しました: fail_num={fail_num}")

def close_log_window():
    rel_p_x, rel_p_y = CLOSE_LOG_POINT_REL
    hwnd = win32gui.FindWindow(None, "自動運転")
    l, t, r, b = win32gui.GetWindowRect(hwnd)
    abs_p_x, abs_p_y = rel_p_x + l, rel_p_y + t
    pyautogui.moveTo(abs_p_x, abs_p_y, duration=DUR_TIME)
    pyautogui.click()

def delete_preprofile():
    load_script()

    # select_file を改変 #
    hwnd = win32gui.FindWindow(None, "開く")
    left, top, _, _ = win32gui.GetWindowRect(hwnd)
    rel_p_x, rel_p_y = SELECT_FILE_POINT_REL
    abs_p_x, abs_p_y = left + rel_p_x, top + rel_p_y
    pyautogui.moveTo(abs_p_x, abs_p_y, duration=DUR_TIME)
    pyautogui.click()
    pyautogui.press("delete")

    rel_p_x, rel_p_y = CLSOE_SELECT_FILE_POINT_REL
    abs_p_x, abs_p_y = left + rel_p_x, top + rel_p_y
    pyautogui.moveTo(abs_p_x, abs_p_y, duration=DUR_TIME)
    pyautogui.click()

for f_iter in [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]:
    print(f"iteration: {f_iter}")
    load_script()
    time.sleep(1)

    select_file()
    time.sleep(1)

    press_autorun_button()
    time.sleep(1)

    download_to_local()
    time.sleep(1)

    close_log_window()
    time.sleep(1)

    delete_preprofile()
    time.sleep(1)