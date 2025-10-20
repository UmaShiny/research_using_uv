import win32gui
import time
import win32api
import pyautogui

time.sleep(5)
hwnd = win32gui.FindWindow(None, "NEEDS-FinancialQUEST")
l, t, r, b = win32gui.GetWindowRect(hwnd)
x,y = win32api.GetCursorPos()
rx, ry = x-l,y-t
print(x,y)
print(rx,ry)
print(f"w: {r-l}, h:{b-t}")


# NEEDS-FinancialQUEST
# scripts\get_from_nfq\temp.py