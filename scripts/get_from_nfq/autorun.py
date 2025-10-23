import win32api
import win32gui
import pyautogui
import time
import os

LOAD_SCRIPT_POINT_ABS       = (633, 327) #
SELECT_FILE_POINT_REL       = (288, 238) #
AUTORUN_BUTTON_POINT_ABS    = (815, 1260) #
CLOSE_LOG_POINT_REL         = (867, 567) # 
CLSOE_SELECT_FILE_POINT_REL = (952, 23) #
DUR_TIME = 0.2
TMP_TIME = 0.4

folder_path = "data/nfq/nfq_dst"

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
                return print(" スクリプトが終了しました", end="")
            else: fail_num += 1
    raise TimeoutError(f" 異常終了しました: fail_num={fail_num}")

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

total = len([f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))])
for i, f_iter in enumerate([f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]):
    print("\r", f"iteration: {f_iter} : {i+1}/{total}", end="")
    load_script()
    time.sleep(TMP_TIME)

    select_file()
    time.sleep(TMP_TIME)

    press_autorun_button()
    time.sleep(TMP_TIME)

    download_to_local()
    time.sleep(TMP_TIME)

    close_log_window()
    time.sleep(TMP_TIME)

    delete_preprofile()
    time.sleep(TMP_TIME)