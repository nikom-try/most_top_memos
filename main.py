import tkinter as tk
from memo_window import MemoWindow
import sys
import os

# コンソールウィンドウを非表示化するための設定
if sys.platform.startswith('win'):
    import ctypes
    ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 0)

def main():
    root = tk.Tk()
    root.withdraw()  # メインウィンドウを非表示にする
    
    # 最初のメモウィンドウを作成
    MemoWindow(root)
    
    root.mainloop()

if __name__ == "__main__":
    main()