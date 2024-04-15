#시나리오 
# 음료 선택-> 현금-> 선택한 음료 재고 -1


# vending_machine=(drinks,prices,stock)
# vending_machine.display

#시나리오 
#drink에서 음료를 고르고(버튼을 누르고)
#개수 선택 
#개수>재고 ->음료수가 품절입니다 
#개수<재고 -> 현금지불로 넘어감 
#현금으로 지불 
#돈이 모자르면 -> 돈이 부족합니다 (현금)
#딱 맞게 넣으면 -> 내가 고른 음료수가 나옴 
#돈을 더 많이 넣으면 -> 거스름돈이 지급 ( 거스름돈은 낸돈-선택한 음료의 가격 )

drinks=['사이다','콜라','생수']
prices=[1300,1500,900]
stock=[4,2,1]

def display_menu(drinks, prices, stock):
    print('음료수 자판기 메뉴')
    for i in range(len(drinks)):
        print(f"{i+1},{drinks[i]}-{prices[i]}원-{stock[i]}개")

display_menu(drinks,prices,stock)
choice = int(input("음료를 선택하세요: "))

def select_drink(choice, drinks, prices, stock):
    choice -= 1
    if choice < 0 or choice >= len(drinks):
        print("잘못된 선택입니다.")
        return None
    elif stock[choice] <= 0:
        print("죄송합니다. 해당 음료수가 품절입니다.")
        return None
    else:
        print(f"{drinks[choice]}를 선택하셨습니다. {prices[choice]}원을 결제해주세요.")
        stock[choice] -= 1
        return prices[choice]

payment = select_drink(choice, drinks, prices, stock)
if payment:
    user_payment= int(input("돈을 넣어주세요"))
    if user_payment < payment:
        print("돈이 부족합니다.")
    else:
        change= user_payment-payment
        print(f'거스름돈 {change}원을 반환합니다.')