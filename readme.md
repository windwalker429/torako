# <del>大合</del>虎子素材庫

## 志願者招募
招募會使用git版控系統與基礎js的大福們一起來剪輯虎子的素材庫，讓我們一起推廣可愛的虎子

## 檔案規範
- 音訊：mp3格式，檔案名稱統一命名youtubeId-(xx)h(yy)m(zz)s.mp3，放置於docs/voice/，xx、yy、zz是直播時間戳記
- 前端：編輯docs/buttons.json即可，array依照直播時間由新往後排序，如果有舊直播請放在正確時間，如果有精選自己放到最上面
- 剪輯原則：正面表述原則，太瑟與髒話不要剪，長度1-20sec

## json格式
```
"context": [
  {
    "filename": "", //按鈕對應的檔案名稱，命名規則參考上述檔案規範
    "name": "", //按鈕標題
    "tag": [""] //按鈕tag，依目前網頁上有的為基準
  }
],
"name": "", //直播標題
"url": "", //直播的YouTube連結
"date": "yyyy-mm-dd" #直播的日期，僅作為方便排序使用，程式不會直接讀取日期
```

## なにこれ 這是什麼？
[前端網址請點這邊](https://windwalker429.github.io/torako/)
ボタンを押すと、[<del>大合</del>虎子](https://www.youtube.com/@YahooTWtaigatorako)がお話ししてくれます。

## 実装
ボタンの[data-voice]属性に指定されたファイル名に基づき音声を読み込み、
[buzz.js](http://buzz.jaysalvat.com/)を利用し音声再生を行っています。

## ライセンス
聲音的所有權利歸屬原作者Torako虎子所有。
其他部分請參考CC授權[CC-BY-NC-SA-4.0](http://creativecommons.org/licenses/by-nc-sa/4.0/deed.ja)に基づき自由にご利用ください。
