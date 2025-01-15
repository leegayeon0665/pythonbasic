#import examCalculator as exC
from examCalculator import *

x = int(input('과목1의 점수를 입력하세요>> '))
y = int(input('과목2의 점수를 입력하세요>> '))
z = int(input('과목3의 점수를 입력하세요>> '))

#tot = examCalculator.totalScore(x,y,z)
#print(tot)

print(totalScore(x,y,z))




