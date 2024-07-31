import ctypes
import os
import win32con
import win32gui

STARTLIST = ["欢迎来到nfa登录辅助程序", "当前版本号0.1.0", "广告：低价nfa -> s-y.lol\n", "输入help查看帮助"]  # 开始提示
HELPLIST = ["单条nfa：输入到此程序", "多条nfa：将txt文件拖入此程序并回车", "回车：复制下一项", "stop：退出", "top：窗口置顶/不置顶", "cls：清屏"]  # 帮助文本
TopState = 0


def top_window(switch):  # 窗口置顶切换
    hwnd = win32gui.GetForegroundWindow()
    if switch == 1:
        win32gui.SetWindowPos(hwnd, win32con.HWND_TOPMOST, 0, 0, 0, 0, win32con.SWP_NOMOVE | win32con.SWP_NOSIZE)
    else:
        win32gui.SetWindowPos(hwnd, win32con.HWND_NOTOPMOST, 0, 0, 0, 0, win32con.SWP_NOMOVE | win32con.SWP_NOSIZE)


def copynfa(element):  # 主要程序
    stack = []
    result = ''
    for char in element:
        if char == '[':
            stack.append(char)
        elif char == ']':
            stack.pop() if stack else None
        elif not stack:
            result += char
    # 从我那个NFAtoCombo里偷的，我看不懂
    nfalist = result
    if ' ' in nfalist:
        nfalist = nfalist.split(' ')

    nfalist = nfalist[0].split(":")
    os.system("echo " + nfalist[0] + "| clip")
    input("[提示]已自动复制账号，回车复制密码")
    os.system("echo " + nfalist[1] + "| clip")
    input("[提示]已复制密码，回车开始下一项")


ctypes.windll.kernel32.SetConsoleTitleW(ctypes.c_wchar_p("NFAtool by shuye https://github.com/3485871248/NFALoginTool"))

for i in STARTLIST:  # 开始提示打印
    print(i)

while True:  # 命令/输入系统
    Command = input()

    if Command == "help":  # 获取帮助
        for i in HELPLIST:
            print(i)

    elif Command == "stop":  # 停止程序
        exit()

    elif Command == "top":  # 切换置顶
        if TopState == 0:
            TopState = 1
            print("[命令]已置顶")
        else:
            TopState = 0
            print("[命令]已取消置顶")
        top_window(TopState)

    elif Command == "cls":  # 清屏
        os.system("cls")

    elif ":/" and ".txt" in Command:  # 多条nfa复制
        FilePath = Command
        ReadFile = open(FilePath, "r")
        ReadList = ReadFile.readlines()
        ReadFile.close()

        for i in ReadList:
            copynfa(i)

    elif ":" in Command:  # 单条nfa复制
        copynfa(Command)

    else:
        print("[错误]未知命令或 NFA/路径 格式错误")
