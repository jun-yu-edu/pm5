total = [{"name" : "사이다", "price" : 1300, "N" : 4},
         {"name" : "콜라", "price" : 1500, "N" : 2},
         {"name" : "생수", "price" : 900, "N" : 1}]

print("**============🍹🍹🍹음료수 자판기에 오신 것을 환영합니다.🍹🍹🍹============**")
print("**====================🍹🍹🍹사이다, 콜라, 생수🍹🍹🍹=====================**")
print("********죄송하지만^^, 💳카드💳만 받습니다.***********'현금 사절'********")

keep_going = True

while keep_going:
    print("==============================================================================")
    bev = input("어떤 음료를 드실건가요?: ")
    for t in total:
        if t["name"] == bev:
            n = t["N"]
            if n > 0:   
                p = t["price"]
                print(f'{p}원을 결제하겠습니다. 앞에 카드를 꽂아 주세요.')
                print("구매해주셔서 감사합니다.")
                t['N'] = t['N'] - 1
            if n <= 0:
                print("품절입니다. 다음 기회를 노려주세요.")
                keep_going = False