# 開発記録

## 反映済みの更新概要
- masktext01.py: 初期版（動画のテキスト領域をROIで指定してインペイント処理）
- masktext02.py: コマンドライン引数で入出力パスを受け取るように変更
- masktext03.py: ROIマスク作成を見直し、インペイントの適用条件を明確化
- masktext04.py: 差分なし（masktext03.py と同一内容）
- masktext05.py: ROIのdtypeを明示し、デバッグ出力を追加
- masktext06.py: ROIをフレームサイズに応じて動的に設定、デバッグ出力を削除
- masktext07.py: フレームを writable な配列に変換してから処理
- masktext08.py: 音声を保持して書き出し、CLI用import位置を整理

## 現在の仕様
- ROIはフレームサイズに応じて自動計算
- 文字領域は輝度条件でマスク化してインペイント
- 変換後の動画は音声付きで出力
- CLIで入出力パスを指定

