##피자 주문 함수

print('피자를 선택해주세요> \n페퍼로니 피자(3000원)\n치즈 피자(3200원)\n콤비네이션 피자(3500원)\n불고기 피자(3600원)\n해산물 피자(3800원)')

while True:
    pizzaname=input('메뉴 이름을 입력하세요 (종료는 exit):')
    
    if pizzaname=='페퍼로니 피자':
        pizzaprice=3000
    if pizzaname=='치즈 피자':
        pizzaprice=3200
    if pizzaname=='콤비네이션 피자':
        pizzaprice=3500
    if pizzaname=='불고기 피자':
        pizzaprice=3600
    if pizzaname=='해산물 피자':
        pizzaprice=3800
    if pizzaname=='exit':
        break
    pizzavalue=int(input('수량을 입력하세요.: '))

##음료 주문 함수

print('음료를 선택해주세요> \n콜라(1500원)\n사이다(1500원)\n생수(1000원)')   
while True:
    drinkname=input('메뉴 이름을 입력하세요 (종료는 exit):')
    
    if drinkname=='콜라':
        drinkprice=1500
    if drinkname=='사이다':
        drinkprice=1500
    if drinkname=='생수':
        drinkprice=1000
    if drinkname=='exit':
        break
    drinkvalue=int(input('수량을 입력하세요.: '))


   
