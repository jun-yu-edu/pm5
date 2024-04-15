# 종로구의 pm10Value, pm25Value의 1달치 데이터를 정리하시오.

import requests
from pprint import pprint

URL = "http://apis.data.go.kr/B552584/ArpltnInforInqireSvc/getMsrstnAcctoRltmMesureDnsty?serviceKey=%2BiEaRW7xrORUYANDjKPrnvW9DAAqDJNKv3E4sm3Vwbes8db4rFSa%2FTnEVPEmaCWv1BzeVE2ek9Fv8onYt9obpQ%3D%3D&returnType=json&numOfRows=100&pageNo=1&stationName=%EC%A2%85%EB%A1%9C%EA%B5%AC&dataTerm=MONTH&ver=1.0"

response = requests.get(URL)

data = response.json() # 주어진 정보가 json 일 때

data = data.get('response').get('body').get('items')

# pprint(data)
from collections import defaultdict
dic = defaultdict(list)


for datum in data:
    date = datum.get('dataTime').split()[0]
    dic[date].append(int(datum.get('pm10Value')))
pprint(dic)


def average(lst):
    return sum(lst)/len(lst)

my_pm10 = [{key : average(value)} for key, value in dic.items()]

result = []
for key, value in dic.items():
    result.append({ key : average(value) })

pprint(my_pm10)