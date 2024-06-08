#只是為了幫使用者節省GPT的使用量，所以會將buttons.json的內容轉換成torakoGPT.json做資料壓縮與清洗
#內容包含了對應的按鈕名稱和對應的音檔名稱，如果torakoGPT.json已經有手動修改key則會保留不會覆蓋
#torakoGPT.json僅使用於GPT機器人，不會直接影響到網頁內容
#執行路徑為torako總目錄下執行 dev/dev_json_etl.py

from glob import glob
import json
import os
import shutil
from pprint import pprint

prefix='./docs'
audioPath=f"{prefix}/voice"
source=f"{prefix}/buttons.json"
target=f"{prefix}/torakoGPT.json"

with open(source, 'r', encoding='utf-8') as file:
    assembly = json.load(file)

with open(target, 'r',encoding='utf-8') as file:
    response = json.load(file)

datas=assembly['fulllist']
filenames=[]
buttonnames=[]
for data in datas:
    contexts=data['context']
    for context in contexts:
        #print(context)
        filenames.append(context['filename'])
        buttonnames.append(context['name'])
#print(filenames)
#response={}
updateTracker={}
for i,filename in enumerate(filenames):
    #檢查檔案是否存在
    if os.path.isfile(f"{audioPath}/{filename}.mp3"):
        try:
            print(f"{audioPath}/{filename}.mp3")
            #out=llm.audio2text(f"{audioPath}/{filename}.mp3")
            #segments = out['result']['segments']
            #raw_text = out['result']['text']
            #summary=llm.summaryLLM(f"{raw_text},{buttonnames[i]}")
            #檢查檔案名是否已經做過etl，若做過就跳過
            if filename in response.values():
                pass
            else:
                response[buttonnames[i]]=filename
                updateTracker[buttonnames[i]]=filename
                print(f"RENEW...{i}/{len(filenames)}",filename)
        except:
            pass
    #print(raw_text)
print("================本次更新START==============")
pprint(updateTracker)
print("================本次更新END==============")

print("請輸入 'Y' 繼續執行更新(將會覆蓋torakoGPT.json檔案)，或輸入其他鍵跳過本次更新內容：")
user_input = input().strip().upper()

if user_input in ['Y','YES']:
    print("更新中...")
    with open(target, 'w',encoding='utf-8') as f:
        json.dump(response, f,ensure_ascii=False, indent=4)
    print("更新完成...")
else:
    print("略過...")
