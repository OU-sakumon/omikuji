# 阪大作問サークルのおみくじ作成を自動化する
阪大作問サークルでは、「数学おみくじ」「英語おみくじ」を作成して学祭で販売しています。全てのおみくじの裏には、問題が書かれています。
これまでは以下の手順で行っていました。
* LaTeXを用いてPDF形式の問題を作成する。
* 一つ一つスクリーンショットする
* PowerPointに手動で貼り付ける。

このレポジトリでは、それをPythonを用いて自動化します。

# 使い方
1. ターミナルを開く
3. （初回のみ）`git clone git@github.com:yunaimatsu/omikuji.git`をコピペして実行する
4. LaTeXで問題を作る
5. 作問が終わったら`omikuji`ディレクトリの中で`source gen.sh`をコピペして実行する

# 展望
Webページ形式にしてブラウザ上でノーコードで作業できるようなUIにしたい。
