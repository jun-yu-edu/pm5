data1 = {'names': ['사이다', '콜라', '생수'], 'cost' : [1300, 1500, 900], 'stock': [4, 2, 1]}

while True:

    print("어떤 음료를 주문하시겠습니까?")
    order = str(input())
    if order in data1['names'] and data1['stock'][data1['names'].index(order)] > 0 :
        drink = data1['names'].index(order)
        print(f"{data1['cost'][drink]}원입니다.")
        print("금액을 넣어주세요.")
        cash = int(input())
        give = cash - data1['cost'][drink]
        if give > 0:
            print(f"거스름돈은 {give}입니다.")
            print(f"{data1['stock'][drink] - 1}개 남았습니다.")
            data1['stock'][drink]  = data1['stock'][drink] - 1
        else :
            print("금액이 부족합니다. 다시 주문해주세요.")

    else:
        print("주문하신 음료가 없습니다.")