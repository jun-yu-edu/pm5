# 터미널 창에 아래 명령어 입력(최초 1회)
# pip install requests
import requests

URL = "https://www.naver.com"

response = requests.get(URL)

data = response.json() # 주어진 정보가 json 일 때



    
from pprint import pprint

pprint(data) # 그냥 print보다 이쁘게 프린트됩니다