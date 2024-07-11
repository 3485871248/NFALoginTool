import os
import win32con
import win32gui

STARTLIST = ["欢迎来到nfa登录辅助程序", "当前版本号0.0.3", "广告：0.45nfa -> s-y.lol\n", "输入help查看帮助"]  # 开始提示
HELPLIST = ["单条nfa：输入到此程序", "多条nfa：输入mult回车，将txt文件拖入此程序", "回车：复制下一项", "stop：退出", "top：窗口置顶/不置顶"]  # 帮助文本
TopState = 0


def top_window(switch):  # 窗口置顶切换
    hwnd = win32gui.GetForegroundWindow()
    if switch == 1:
        win32gui.SetWindowPos(hwnd, win32con.HWND_TOPMOST, 0, 0, 0, 0, win32con.SWP_NOMOVE | win32con.SWP_NOSIZE)
    else:
        win32gui.SetWindowPos(hwnd, win32con.HWND_NOTOPMOST, 0, 0, 0, 0, win32con.SWP_NOMOVE | win32con.SWP_NOSIZE)


def copynfa(element):  # 主要程序
    nfalist = element.split("]")
    nfa = [item for item in nfalist if "[" not in item][0]
    if nfa.find(" "):
        nfalist = nfa.split(" ")
        nfa = nfalist[0]
    nfalist = nfa.split(":")
    os.system("echo " + nfalist[0] + "| clip")
    print("已自动复制账号，回车复制密码")
    input()
    os.system("echo " + nfalist[1] + "| clip")
    print("已复制密码，回车开始下一项")
    input()


for i in STARTLIST:  # 开始提示打印
    print(i)

while True:  # 命令/输入系统
    Command = input()

    if Command == "help":  # 获取帮助
        for i in HELPLIST:
            print(i)

    elif Command == "stop":  # 停止程序
        exit()

    elif Command == "mult":  # txt文件导入
        FilePath = input("将txt拖到此程序：")
        ReadFile = open(FilePath, "r")
        ReadList = ReadFile.readlines()
        ReadFile.close()

        for i in ReadList:
            copynfa(i)

    elif Command == "top":  # 切换置顶
        if TopState == 0:
            TopState = 1
            print("已置顶")
        else:
            TopState = 0
            print("已取消置顶")
        top_window(TopState)

    else:  # 单条nfa
        copynfa(Command)
