import win32gui
import win32con


def set_foreground_window():
    hwnd = win32gui.GetForegroundWindow()
    win32gui.SetWindowPos(hwnd, win32con.HWND_TOPMOST, 0, 0, 0, 0, win32con.SWP_NOMOVE | win32con.SWP_NOSIZE)


if __name__ == "__main__":
    set_foreground_window()

    # 这里可以放你的CLI程序的主逻辑
    input("Press Enter to exit...")
