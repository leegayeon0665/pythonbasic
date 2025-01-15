def rectArea(width,height):
    #a = width * height
    return width * height

def triArea(base,height):
    return base * height/2


if __name__ =='__main__':    ##함수가 만들어져 있는 곳에서 호출될 때만 실행 (내가 나를 호출할 때만 실행, 남이 나를 호출할 때는 실행X)
    print(f'사각형 넓이 = {rectArea(5,10)}')
    print(f'삼각형 넓이 = {triArea(5,10)}')
