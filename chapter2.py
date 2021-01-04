# 챕터 3 - 연산자, 수식, 숫자처리함수, 랜덤함수

# ctrl + / : 선택라인 주석

# 자료형
age = 4
is_adult = age >= 3
print("나이는 " + str(age))
print("나는 어른? " + str(is_adult))

# 연산자
print(6/3) # 2.0
print(6//3) # 2

# 간단한 수식
age += 4

# 숫자처리함수
print(abs(-5)) # 5
print(pow(4, 2)) # 16
print(max(5, 12)) # 12
print(min(5, 12)) # 5
print(round(3.14)) # 3 반올림
print(round(4.99)) # 5

from math import *
print(floor(4.99)) # 내림 4
print(ceil(3.14)) # 올림 4
print(sqrt(16)) # 제곱근 4

## 랜덤함수
from random import *
print(random()) # 0.0~1.0 미만의 임의의 값 생성
print(random() * 10) # 0.0 ~ 10.0 미만
print(int(random() * 10)) # 0 ~ 10 미만
print(int(random() * 10) + 1) # 1 ~ 10 이하
print(int(random() * 45) + 1) # 1 ~ 45 이하
print(randrange(1, 46)) # 1 ~ 46 미만
print(randint(1, 45)) # 1 ~ 45 이하

# 퀴즈 2
# 4 ~ 28 이하
from random import *
date = randint(4, 28)
print("오프라인 스터디 모임 날짜는 매월 " + str(date) + " 일로 선정되었습니다.")
