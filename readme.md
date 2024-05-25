# 大合虎子素材庫

## 志願者招募
招募會使用git版控系統與基礎html的大福們一起來剪輯虎子的素材庫，讓我們一起推廣可愛的虎子

##檔案規範
- 音訊：mp3格式，檔案名稱統一命名youtubeId-hhmmss.mp3，放置於docs/voice/
- 前端：直接編輯docs/index.html加入音訊按鈕，搶按照時間排序，如果有舊直播請放在正確時間，如果有精選自己放到最上面
- 剪輯原則：正面表述原則，太瑟與髒話不要剪，長度1-20sec

## なにこれ 這是什麼？
[動くものはこちらから。](https://windwalker429.github.io/torako/)
ボタンを押すと、[大合虎子](https://www.youtube.com/@YahooTWtaigatorako)がお話ししてくれます。

## 実装
ボタンの[data-voice]属性に指定されたファイル名に基づき音声を読み込み、
[buzz.js](http://buzz.jaysalvat.com/)を利用し音声再生を行っています。

## ライセンス
音声に関わる権利は全て元著作者に帰属します。
その他の部分については[CC-BY-NC-SA-4.0](http://creativecommons.org/licenses/by-nc-sa/4.0/deed.ja)に基づき自由にご利用ください。
