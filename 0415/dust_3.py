# 시도별 실시간 측정정보 조회의 서울의 데이터를 
# stationName으로 접근하기 쉬운 자료구조로 재구성하시오.
# 단 값이 None인 key는 제외하시오.

import requests
from pprint import pprint

URL = "http://apis.data.go.kr/B552584/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty?serviceKey=%2BiEaRW7xrORUYANDjKPrnvW9DAAqDJNKv3E4sm3Vwbes8db4rFSa%2FTnEVPEmaCWv1BzeVE2ek9Fv8onYt9obpQ%3D%3D&returnType=json&numOfRows=100&pageNo=1&sidoName=%EC%84%9C%EC%9A%B8&ver=1.0"

response = requests.get(URL)

data = response.json() # 주어진 정보가 json 일 때

data = data.get('response').get('body').get('items')

# pprint(data)

dic = {}
for datum in data:
    station_name = datum.get('stationName')
    # print(station_name)

    dic[station_name] = datum

pprint(dic)

dic.get('구로구')