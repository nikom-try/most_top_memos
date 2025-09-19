# Most Top Memos

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

このアプリケーションは、常に最前面に表示されるシンプルなメモ帳です。複数のメモを管理し、それぞれが独立したウィンドウで開かれます。

## 機能

- 常に最前面に表示されるウィンドウ
- 新しいメモを追加するボタン
- 各ウィンドウを閉じるボタン
- ウィンドウを開くたびに異なるカラフルな背景色（見やすい薄い色）
- 太字のフォントで文字を表示

## スクリーンショット

![Screenshot](img/screenshot.png) <!-- スクリーンショットを追加してください -->

## インストール

1. Python 3.x をインストールしてください。
2. このリポジトリをクローンまたはダウンロードしてください。
   ```bash
   git clone https://github.com/your-username/most-top-memos.git
   ```
3. プロジェクトディレクトリに移動してください。
   ```bash
   cd most-top-memos
   ```
4. 必要に応じて仮想環境を作成してください。
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/macOS
   venv\Scripts\activate     # Windows
   ```
5. 依存関係をインストールしてください。
   ```bash
   pip install -r requirements.txt
   ```

## 使用方法

1. `main.py`を実行してください。
   ```bash
   python main.py
   ```
2. 最初のメモウィンドウが開きます。
3. 「新しいメモ」ボタンをクリックして、新しいメモウィンドウを作成できます。
4. 「閉じる」ボタンまたはウィンドウの閉じるボタンでウィンドウを閉じます。

## 必要環境

- Python 3.x
- Tkinter (Pythonの標準ライブラリ)

## ファイル構成

- `main.py`: アプリケーションのエントリーポイント
- `memo_window.py`: メモウィンドウクラスの定義
- `utils.py`: ユーティリティ関数（色の生成など）

## ライセンス

このプロジェクトはMITライセンスの下で公開されています。詳細は[LICENSE](LICENSE)ファイルを参照してください。

## コントリビューション

コントリビューションは歓迎します。IssueやPull Requestをお気軽にどうぞ！

1. フォークしてください。
2. featureブランチを作成してください (`git checkout -b feature/AmazingFeature`)。
3. 変更をコミットしてください (`git commit -m 'Add some AmazingFeature'`)。
4. ブランチにプッシュしてください (`git push origin feature/AmazingFeature`)。
5. Pull Requestを作成してください。

## 作者

あなたの名前 - [your-username](https://github.com/your-username)