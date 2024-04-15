#2. 자판기 음료 선택,
# 자판기에 금액을 넣고,
# 구매 개수 선택, 
# 선택한 음료의 거스름돈 출력

df=[{'음료':'사이다','가격':1300,'재고':4},{'음료':'콜라','가격':1500,'재고':2},{'음료':'생수','가격':900,'재고':1}]
name2=input('음료를 선택하세요:')
pay=int(input('금액을 지불하세요:'))
piece2=int(input('구매할 개수를 입력하세요:'))

for bevarage in df:
    if bevarage['음료']==name2:
        print(f'거스름돈은{pay-((bevarage['가격'])*(piece2))}입니다.')

# 3. 구매후 남은 음료 재고 표시


index = 0

for item in df:
    if item['음료'] == name2:
        if item['재고'] >= piece2:
            item['재고'] -= piece2
            print("{} {}개를 구매했습니다.".format(name2, piece2))
        else:
            print("재고가 부족합니다.")
        break

# 재고 상태 출력
print("재고 상태:")
for item in df:
    print(item)
