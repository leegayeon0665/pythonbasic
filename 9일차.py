import polyArea  #함수 호출

print('사각형 넓이 계산')
width = float(input('사각형의 가로 입력>> '))
height = float(input('사각형의 세로 입력>> '))
print(f'사각형 넓이 = {polyArea.rectArea(width,height)}')

print('삼각형 넓이 계산')
base = float(input('삼각형의 밑변 입력>> '))
height = float(input('사각형의 높이 입력>> '))
print(f'삼각형 넓이 = {polyArea.triArea(base,height)}')
