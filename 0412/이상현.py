#사용자는 보유소득, 구매희망음료 이름과 개수를 입력한다. 
# 1인당 한 종류의 음료만 1회 구매가능하다.
#사용자의 구매희망음료 개수와 자판기의 재고량, 
# 사용자의 보유소득과 희망구매금액을 비교한다.
#비교 결과에 따라 적절한 답변을 출력한다. 
# 거스름돈은 반환되지 않습니다.
 
print('=========1인당 1회만 구매 가능한 음료수 자판기 영업 시작합니다=========')
money = int(input('당신이 보유한 소득(원단위)는 얼마인가요? (숫자만 입력)'))
drink = input('당신이 주문할 음료수의 이름을 다음 세가지 중 하나만 선택하자면? (사이다, 콜라, 생수)')
num = int(input('당신이 주문하고 싶은 음료수 개수는 얼마인가요?'))
print()
print('자판기 투입구에 현금을 넣어주세요.')

if drink == '사이다':
    exis = 4
elif drink == '콜라':
    exis = 2
elif drink == '생수':
    exis = 1

if drink == '사이다':
    coffee = 1300
elif drink == '콜라':
    coffee = 1500
elif drink == '생수':
    coffee = 900
pay = coffee * num

print()
if (money >= pay) & (num <= exis):
    print('구매가 완료되었습니다. 맛있게 드세요!')
elif (money < pay) & (num <= exis):
    print('금액이 부족합니다. 구매는 다음에!')
elif (money >= pay) & (num > exis):
    print('재고가 부족합니다. 구매는 다음에!')
else:
    print('금액과 재고 모두 부족합니다. 구매는 다음에!')
print('=========구매 기회를 모두 소진했으므로 음료수 자판기 영업 종료합니다=========')