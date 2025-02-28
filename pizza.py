
def select(menu,menuname):
    order = {}
    print(f'\n****{menuname}목록****')
    for name, price in menu.items():
        print(f'{name} ({price})원')
    while True:
        p_name = input(f'주문할 {menuname} 입력하세요(종료:exit)')
        if p_name =='0':
            pass
        elif p_name in menu:
            count = int(input('수량을 입력하세요: '))
            order[p_name] = count
            print('주문 완료!')
        elif p_name == 'exit':
            break

    return order

def money_calculater(order,menu,menu_name):
    tot_price = 0
    for x in order_pizza.keys():
        price=0
        if x in menu.keys():
            price = price + (order[x] * menu[x])
        print(f'{x}({menu[x]}원) X {order[x]} = {price:,}원')
        tot_price = tot_price + price

    print(f'가격: {tot_price}')
    return tot_price



if __name__ == '__main__':
    pizza_menu={'페퍼로니 피자':3000,
                '치즈 피자':3200,
                '콤비네이션 피자':3500,
                '불고기 피자':3600, 
                '해산물 피자':3800}
    drink_menu={'콜라':1500,
                '사이다':1500,
                '생수':1000}
    

    #주문
    order_pizza = select(pizza_menu,'피자')
    print(order_pizza)
    order_drink = select(drink_menu,'음료')
    print(order_drink)

    #계산
    tot_pizza = money_calculater(order_pizza,pizza_menu, '피자')   #피자 계산
    tot_drink = money_calculater(order_drink,drink_menu, '음료')   #음료 계산

    print(f'전체 가격: 피자 + 음료 = {tot_pizza = tot_drink}')
    

