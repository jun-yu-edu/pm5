#시나리오
#사용자가 음료, 개수 선택 후 가격 지불 
#재고가 있는 경우 사용자가 낸 가격과 음료 가격 비교 -> 
    # 금액이 부족하지 않다면 사용자가 구매한 음료, 구매 금액, 남은 재고, 거스름돈 알려줌 / 
    # 금액이 부족하다면 금액 부족 알림 후 처음부터 다시 선택
#재고가 없는 경우 재고 부족 알림 후 처음부터 다시 선택 

beverage = ['사이다', '콜라', '생수']
price = [1300, 1500, 900]
stock = [4, 2, 1]

sum = 0
money = 0

while(1):
    print("#########자판기##########")

    i = 0
    for i in range(0,3):
        print(f'{beverage[i]} {price[i]}원 {stock[i]}개') #자판기의 음료, 가격, 재고 차례대로 출력
    print("##########################")
    
    pick = input('구매를 원하시는 제품을 선택하세요 (제품명 입력): ') #사용자에게 제품명 입력받음
    count = int(input('몇 개 구매하시겠습니까?(숫자만 입력) : ')) #사용자가 구매하고자 하는 물품 갯수 입력받음
    bill = int(input('얼마를 내시겠습니까? (숫자로 입력): ' )) #사용자가 지불할 금액 입력받음

    if pick == '사이다':
        sum = price[0] * count
        money = bill - sum
        if money < 0 :
            print('지불 금액을 다시 확인해주세요. \n')
            continue
        stock[0] -= count
        if stock[0] < 0 :
            print('해당 상품은 재고가 없습니다.')
            continue
        print(f'{pick}를 선택했습니다. 총 금액은 {sum}원입니다.\n 거스름돈 {money}원 입니다.\n 해당 상품 재고는 현재 {stock[0]}개 남았습니다.\n ')

         
    elif pick == '콜라':
        sum = price[1] * count
        money = bill - sum
        if money < 0 :
            print('지불 금액을 다시 확인해주세요. \n')
            continue
        stock[1] -= count
        if stock[1] <= 0 :
            print('해당 상품은 재고가 없습니다.')
            continue
        print(f'{pick}를 선택했습니다. 총 금액은 {sum}원입니다.\n 거스름돈 {money}원 입니다.\n 해당 상품 재고는 현재 {stock[1]}개 남았습니다.\n ')

    elif pick == '생수':
        sum = price[2] * count
        money = bill - sum
        if money < 0 :
            print('지불 금액을 다시 확인해주세요. \n')
            continue
        stock[2] -= count
        if stock[2] <= 0 :
            print('해당 상품은 재고가 없습니다.')
            continue
        print(f'{pick}를 선택했습니다. 총 금액은 {sum}원입니다.\n 거스름돈 {money}원 입니다.\n 해당 상품 재고는 현재 {stock[2]}개 남았습니다.\n ')
        # 
    
    else:
        print('입력이 올바르지 않습니다. 다시 입력해주세요. \n')



    


