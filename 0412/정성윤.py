# 사용자가 돈을 내고,음료를 고르면, 
# 해당 음료 1개가 뽑아지고, 재고가 1개 줄고, 거스름돈이 나옴 
# 선택한 음료의 가격보다 적은 돈을 낼 경우 금액 부족 안내
# 재고 없을 시, 품절 안내

keep_going = True

data = [['사이다', 1300, 4], ['콜라',1500, 2], ['생수',900, 1]]
while keep_going:

    money = int(input("고객이 낸 돈:  "))
    name = input("음료명: ")

    for x in [0,1,2]:
        change = money - data[x][1]
        stock = data[x][2]
        if stock>0 and name in data[x] and change >= 0:
            # stock = stock - 1
            data[x][2] = stock - 1
            print(f"음료와 거스름 돈을 받으세요. 거스름 돈:{change}")
        elif stock>0 and name in data[x] and change < 0:
            print("금액이 부족합니다.")
        elif stock<=0:
            print("품절입니다.")
            keep_going = False