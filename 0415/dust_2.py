# 시도별 실시간 측정정보 조회의 서울의 데이터에 대해, 
# 초 미세먼지 농도가 낮은 stationName순으로 정렬하시오.

import requests
from pprint import pprint

URL = "http://apis.data.go.kr/B552584/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty?serviceKey=%2BiEaRW7xrORUYANDjKPrnvW9DAAqDJNKv3E4sm3Vwbes8db4rFSa%2FTnEVPEmaCWv1BzeVE2ek9Fv8onYt9obpQ%3D%3D&returnType=json&numOfRows=100&pageNo=1&sidoName=%EC%84%9C%EC%9A%B8&ver=1.0"

response = requests.get(URL)

data = response.json() # 주어진 정보가 json 일 때

data = data.get('response').get('body').get('items')

# pprint(data)

# 전처리
for datum in data:
    if datum.get('pm25Value') == '-':
        datum['pm25Value'] = 0


# data.sort(key=lambda x : x.get('pm25Value'))
data.sort(key=lambda x : int(x.get('pm25Value')))

data = [[datum.get('stationName'), datum.get('pm25Value')] for datum in data]

# 위랑 완전히 같은 코드!
lst = []
for datum in data:
    lst.append([datum.get('stationName'), datum.get('pm25Value')])


pprint(data)






