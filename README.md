# analysis_notepad_app
 
分析メモ帳アプリ

# このアプリで出来ること

* 書いたメモを自然言語処理を利用して分析
    * そのデータを基に関連がありそうな過去のメモを提示 
    * =>自分も忘れていた過去のアイデアを再度振り返ることにより、より創造的なメモを作れる 

* 便利なメモ帳としての機能も付随


# 具体的な仕様

* MeCabを用いて分析 => 辞書に
    * そのデータをJSONファイルに保存・蓄積

* JSONファイルのデータを基に、MeCabによる分析と近い過去のメモを提示
    * 具体的には同一単語(原型)の個数で比較する


# Author 

 EaGitro (twitter: [@EaGitro](https://twitter.com/EaGitro), GitHub: [EaGitro](https://github.com/EaGitro))


 © EaGitro 2022 All Rights Reserved.
