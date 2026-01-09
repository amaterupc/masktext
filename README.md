# masktext

動画の右下などに重なっているテキスト（電話番号など）を、インペインティングで目立たなくするための試作スクリプト集です。
`masktext01.py`〜`masktext08.py` は改良履歴として残っています。最新版の使用は `masktext08.py` を推奨します。

## できること

- 動画フレームの特定領域を検出・マスクしてインペインティング
- 音声を保持したまま書き出し（`masktext08.py`）

## 必要環境

- Python 3.9+（推奨）
- 依存ライブラリ
  - `opencv-python`
  - `moviepy`
  - `numpy`
- `ffmpeg`（`moviepy` の動画書き出しに必要）

インストール例:

```bash
pip install opencv-python moviepy numpy
```

`ffmpeg` が未導入の場合は別途インストールしてください（macOS なら `brew install ffmpeg` など）。

## 使い方（推奨: masktext08.py）

```bash
python masktext08.py <input_video_path> <output_video_path>
```

例:

```bash
python masktext08.py input.mp4 output.mp4
```

## マスク範囲の調整

`masktext08.py` の `remove_text_from_frame` 内で、マスク対象のROIを割合で指定しています。
動画によって位置が違う場合はここを調整してください。

```python
x_start = int(width * 0.75)
y_start = int(height * 0.9)
x_end = width
y_end = height
```

## 注意

- テキストの色・背景によってはマスク精度が落ちるため、条件式の調整が必要です。
- 画面全体に対して小さな領域を想定しています。必要に応じて範囲を拡大してください。

## 既存スクリプト

- `masktext.py` : 初期版（固定座標、音声保持なし）
- `masktext07.py` : ROIの割合指定（音声保持なし）
- `masktext08.py` : ROIの割合指定 + 音声保持
