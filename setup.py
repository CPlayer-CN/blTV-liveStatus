#encoding=utf-8
import requests,json,time

# 主站 ID，麦子的
mid=145149047
# 延迟，单位秒
delay=60
# 循环次数
round=1440

i=0

while i < round:
    html=requests.get('https://api.live.bilibili.com/room/v1/Room/getRoomInfoOld?mid=%s'%mid).json()
    print(html['data']['liveStatus'])
    time.sleep(delay)
    i+=1
