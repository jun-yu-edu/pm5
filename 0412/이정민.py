#자판기에서 판매되는 제품 종류와 가격 재고가 표시된다.
#돈을 넣고 제품을 선택하면 거스름 돈과 남은 재고를 보여준다.

VM_list = [{'drink': '사이다', 'price':1300, 'stock':4}, {'drink': '콜라', 'price':1500, 'stock':2}, {'drink': '생수', 'price': 900, 'stock':1}]

print('==========안녕하세요! 맛나 자판기입니다===========')
print('사이다(4) 1300', '콜라(2) 1500', '생수(1) 900')

pay = int(input('금액을 입력해 주세요: '))
drink = input('음료를 선택해 주세요: ')
cnt = int(input('음료의 개수를 선택해 주세요: '))


if drink == '사이다':
    if pay - VM_list[0]['price'] < 0:
        print('금액이 부족합니다.')
    else:
        print(pay - VM_list[0]['price'])    
        print(VM_list[0]['stock'] - cnt)
    

elif drink == '콜라':
    if pay - VM_list[1]['price'] < 0:
        print('금액이 부족합니다.')
    else:
        print(pay - VM_list[1]['price'])
        print(VM_list[1]['stock'] - cnt)
    

else:
    if pay - VM_list[2]['price'] < 0:
        print('금액이 부족합니다.')
    else:
        print(pay - VM_list[2]['price'])
        print(VM_list[2]['stock'] - cnt)