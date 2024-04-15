#사용자가 음료 사이다, 콜라, 생수 중 음료를 구매하려고 합니다. 
# 일인당 한 개씩만 가능합니다. 재고가 떨어지면 구매가 불가능하다고 알립니다.
# 관리자가 볼 수 있게 구매한 음료명, 가격, 남은 재고를 알려줍니다.
name=['사이다','콜라','생수']
price= [1300,1500,900]
stock= [4,2,1]

print(stock[0])

drink_1={name:'사이다', price: 1300, stock:4}
drink_2={name:'콜라', price:1500,stock:2}
drink_3={name:'생수', price:900,stock:1}

drinks = [name, price, stock]

order_1 =[]
order_2 =[]
order_3=[]

for i in name:
    if i =='사이다':
        order_1.append()
        order_1.append(stock[0]-1)
        order_1.append(price[0]*1)
        print('1번 고객님의 음료 이름, 재고, 가격입니다')
    if i =='콜라':
        order_2.append()
        order_2.append(stock[1]-1)
        order_2.append(price[1]*1)
        print('2번 고객님의 음료 이름, 재고, 가격입니다')
    if i =='생수':
        order_3.append()
        order_3.append(stock[2]-1)
        order_3.append(price[2]*1)
        print('3번 고객님의 음료 이름,재고, 가격입니다.')
   
if stock[0,1,2]<=0:
    print('재고가 없습니다')