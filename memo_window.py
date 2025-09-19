import tkinter as tk
from utils import generate_random_color

class MemoWindow:
    def __init__(self, root):
        self.root = root
        self.window = tk.Toplevel(root)
        self.window.title("メモ帳")
        # 初期サイズを小さく設定
        self.window.geometry("300x30")  # 幅を広めに設定
        self.window.attributes('-topmost', True)  # 常に最前面に表示
        # タイトルバーを非表示にする
        self.window.overrideredirect(True)
        
        # ランダム色を生成
        title_color = generate_random_color()
        
        # ボタンフレーム（タイトルバーの代わり）
        self.title_frame = tk.Frame(self.window, bg=title_color, height=30)
        self.title_frame.pack(fill=tk.X)
        self.title_frame.pack_propagate(False)  # 高さを固定
        
        # 移動ボタン
        self.move_button = tk.Button(
            self.title_frame,
            text="✥",  # 移動ボタン（四方向矢印）
            bg="#2196F3",
            fg="white",
            font=("Arial", 10, "bold"),
            relief=tk.FLAT,
            width=2
        )
        self.move_button.pack(side=tk.LEFT, padx=2, pady=2)
        
        # タイトルエントリ（編集可能なタイトル）
        self.title_var = tk.StringVar(value="メモ帳")
        self.title_entry = tk.Entry(
            self.title_frame,
            textvariable=self.title_var,
            bg=title_color,
            fg="black",
            font=("Arial", 12, "bold"),  # フォントを変更
            relief=tk.FLAT,
            justify=tk.CENTER
        )
        self.title_entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=5, pady=5)
        
        # 新しいメモを開くボタン (左側に配置)
        self.open_button = tk.Button(
            self.title_frame,
            text="□",  # 新しいメモボタン（四角）
            command=self.open_new_memo,
            bg="#4CAF50",
            fg="white",
            font=("Arial", 10, "bold"),
            relief=tk.FLAT,
            width=2
        )
        self.open_button.pack(side=tk.LEFT, padx=2, pady=2)  # LEFTに変更
        
        # 閉じるボタン (左側に配置)
        self.close_button = tk.Button(
            self.title_frame,
            text="×",  # 閉じるボタン（バツ）
            command=self.close_window,
            bg="#f44336",
            fg="white",
            font=("Arial", 10, "bold"),
            relief=tk.FLAT,
            width=2
        )
        self.close_button.pack(side=tk.LEFT, padx=2, pady=2)  # LEFTに変更
        
        # タイトルが変更されたときにウィンドウ幅を調整
        self.title_var.trace("w", self.adjust_window_width)
        
        # ウィンドウの移動用バインディング
        self.move_button.bind("<Button-1>", self.start_move)
        self.move_button.bind("<B1-Motion>", self.do_move)
        
        # ウィンドウを閉じたときの処理
        self.window.protocol("WM_DELETE_WINDOW", self.close_window)
        
        # 初期ウィンドウ幅を調整
        self.adjust_window_width()
    
    def adjust_window_width(self, *args):
        """タイトルの長さに応じてウィンドウの幅を調整する"""
        title = self.title_var.get()
        # フォントサイズ12のArialで文字数から幅を計算
        # 各ボタンの幅を考慮して、より余裕を持った計算に変更
        width = max(300, len(title) * 12 + 200)  # 最小幅を300pxに設定
        height = 30
        self.window.geometry(f"{width}x{height}")
    
    def open_new_memo(self):
        """新しいメモウィンドウを開く"""
        MemoWindow(self.root)
    
    def close_window(self):
        """ウィンドウを閉じる"""
        self.window.destroy()
    
    def start_move(self, event):
        """ウィンドウの移動開始"""
        self.x = event.x
        self.y = event.y

    def do_move(self, event):
        """ウィンドウの移動"""
        deltax = event.x - self.x
        deltay = event.y - self.y
        x = self.window.winfo_x() + deltax
        y = self.window.winfo_y() + deltay
        self.window.geometry(f"+{x}+{y}")