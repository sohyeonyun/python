# 챕터 4 - 리스트, 사전, 튜플, 세트, 자료구조의 변경

####################################### 리스트 [] ##############################
subway = ["유재석", "조세호", "박명수"]

# 조세호는 몇 번째?
print(subway.index("조세호"))   # 1

# 하하가 탐
subway.append("하하")           # ['유재석', '조세호', '박명수', '하하']  

# 정형돈을 유재석, 조세호 사이에 태움
subway.insert(1, "정형돈")      # ['유재석', '정형돈', '조세호', '박명수', '하하']

# 마지막 사람 내림
print(subway.pop()) # 하하
print(subway)       # ['유재석', '정형돈', '조세호', '박명수'] 

# 같은 이름의 사람 몇 명인지
subway.append("유재석")
print(subway.count("유재석")) # 2

# 정렬도 가능
num_list = [5, 2, 4, 3, 1]
num_list.sort()     # [1, 2, 3, 4, 5]

# 순서 뒤집기 가능
num_list.reverse()  # [5, 4, 3, 2, 1]

# 모두 지우기
num_list.clear()    # []

# 다양한 자료형 함께 사용
mix_list = ["조세호", 20, True]

# 리스트 확장
num_list = [5, 2, 4, 3, 1]
num_list.extend(mix_list) 
print(num_list)             # [5, 2, 4, 3, 1, '조세호', 20, True]

num_list.remove('조세호')
print(num_list)
num_list.add("하")
print(num_list)


####################################### 사전 #################################
cabinet = {3:"유재석", 100:"김태호"}

print(cabinet[3])
print(cabinet[100])

print(cabinet.get(3))
# print(cabinet[5]) # error
print(cabinet.get(5))   # None
print(cabinet.get(5, "사용 가능")) # 사용 가능 (기본값 넣기)

print(3 in cabinet) # True
print(5 in cabinet) # False

# 키가 문자열
cabinet = {"A-3":"유재석", "B-100":"김태호"}
print(cabinet["A-3"])

# 새 손님
cabinet["C-20"] = "조세호"  # 없으면 추가
cabinet["A-3"] = "김종국"   # 있으면 업데이트
print(cabinet)        # {'A-3': '김종국', 'B-100': '김태호', 'C-20': '조세호'}

# 삭제
del cabinet["A-3"]  # {'B-100': '김태호', 'C-20': '조세호'} 

# 키 들만 출력
print(cabinet.keys())   # dict_keys(['B-100', 'C-20'])

# value 들만 출력
print(cabinet.values()) # dict_values(['김태호', '조세호'])

# key, value 쌍으로 출력
print(cabinet.items())  # dict_items([('B-100', '김태호'), ('C-20', '조세호')])

# 목욕탕 폐점
cabinet.clear()
print(cabinet)  # {}


####################################### 튜플 #################################
menu = ("돈까스", "치즈까스")
print(menu[0])  # 돈까스

# menu.add("생선까스") -> error

name = "김종국"
age = 20
hobby = "코딩"
print(name, age, hobby)

# 활용
(name, age, hobby) = ("김종국", 20, "코딩")
print(name, age, hobby)


#################### 집합 (set)  -  중복 안됨, 순서 없음 ########################
my_set = {1, 2, 3, 3, 3}
print(my_set)      # {1, 2, 3}

java = {"유재석", "김태호", "양세형"}
python = set(["유재석", "박명수"])

# 교집합
print(java & python)                # {'유재석'}
print(java.intersection(python))    # {'유재석'}

# 합집합
print(java | python)        # {'박명수', '김태호', '유재석', '양세형'} 
print(java.union(python))   # {'박명수', '김태호', '유재석', '양세형'} 

# 차집합 (java O, python X)
print(java - python)            # {'양세형', '김태호'}
print(java.difference(python))  # {'양세형', '김태호'}

# python 늘어남
python.add("김태호")
print(python)       # {'유재석', '김태호', '박명수'}

# java 까먹음 ㅠ
java.remove("김태호")   # {'유재석', '양세형'}
print(java)

############################ 자료구조의 변경 ##################################
menu = {"커피", "우유", "주스"}
print(menu, type(menu)) # {'커피', '우유', '주스'} <class 'set'> 

menu = list(menu)
print(menu, type(menu)) # ['주스', '우유', '커피'] <class 'list'> 

menu = tuple(menu)
print(menu, type(menu)) # ('우유', '커피', '주스') <class 'tuple'> 

menu = set(menu)
print(menu, type(menu)) # {'우유', '주스', '커피'} <class 'set'> 


############################## 퀴즈 4 #####################################
# 추첨 통해 1명 치킨, 3명 커피
# 조건1 : 댓글 20명 작성, 아이디는 1~20 이라 가정
# 조건2 : 무작위로 추첨, 중복 불가
# 조건3 : random 모듈의 shuffle과 sample 활용

# (활용 에제)
from random import *
lst = [1, 2, 3, 4, 5]
print(lst)
shuffle(lst)
print(lst)
print(sample(lst, 1)) # lst에서 몇 개만큼 무작위 뽑음

# 내 풀이
users = range(1, 21)    # 1 ~ 20
print(type(users))      # <class 'range'>

users = list(users)     # range -> users
shuffle(users)
chicken = users.pop()
coffee = sample(users, 3)

print(" -- 당첨자 발표 --")
print("치킨 당첨자 : {}" .format(chicken))
print("커피 당첨자 : {}" .format(coffee))
print(" -- 축하합니다 --")

# 강의 풀이
users = range(1, 21)    # 1 ~ 20
print(type(users))      # <class 'range'>

users = list(users)     # range -> users
shuffle(users)
winner = sample(users, 4)

print(" -- 당첨자 발표 --")
print("치킨 당첨자 : {0}" .format(winner[0]))
print("커피 당첨자 : {0}" .format(winner[1:]))
print(" -- 축하합니다 --")
