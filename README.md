# 反応速度評価のためのアプリ
## Requirements
Normal Win 10 with normal python. I don't know details what computer I have.
## 使い方
main.pyを起動すると、アプリが開始します。
SETTINGボタンを押すと設定画面にうつります。詳細の設定はconfigure.iniで行ってください。
STARTを押すと試験画面に移ります。sボタンで試験開始、エラーが発報されたら答えのボタンを押してください(任意設定可能)。
ダウンロードしたままの状態では1,2,3の選択肢があります。
qボタンで試験画面を閉じることができます。
out.csvにデータが蓄積されます。

## 技術的資料
### 概説
これはpythonを使ったとある試験装置です。クラスによってデータドリブンな運用がなされ、人間の反射速度の計測をデータ化します。
データドリブンなので、基本的な機能に追加機能を加えることが容易です。また、計測時間が正確になるよう、コードに留意し、誤差を最小化しています。

### 画面
画面遷移は以下で構成されています。
*開始画面 (root)
 起動時に表示される画面です。
*設定画面 (setting_window)
　設定を表示します。
*試験画面 (test_window)
　実際の試験の画面です。これはキーボードで操作します。

### テストデータの取り回し
テストデータは大まかには以下のクラスで扱われます
-Setting_params
 画面サイズやランダムネスの生成情報など、設定データが保存されます

-Test_data
 実際にテストを開始するとこのクラスが定義されます。
 決定されたエラー発報時間やテスト結果が保存され、最終的には出力ファイルに吐き出されます。
