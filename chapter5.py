# 챕터5  - if, for, while, continue와 break, 한 줄 for

# if
weather = input("오늘 날씨는 어때요? ") # 사용자 입력 받은 후 str 으로 반환
if weather == "비" or weather == "눈":
    print("우산 챙기라우")
elif weather == "미세먼지":
    print("마스크 챙기라우")
else:
    print("걍 ㄱㄱ")


# for
for waiting_no in [0, 1, 2, 3, 4]:      # range(5) : 0~4, range(1, 6) : 1~5
    print("대기번호 : {0}" .format(waiting_no))

absent = [2, 5]
no_book = [7]
for student in range(1, 11):
    if student in absent:
        continue
    elif student in no_book:
        print("오늘 수업 여기까지. {0}는 교무실로 따라와" .format(no_book))
        break
    print("{0}, 책 읽어보소" .format(student))

# 1, 2, 3, 4, 5 --> 101, 102, 103, 104, 105
students = [1, 2, 3, 4, 5]
students = [i+100 for i in students]
print(students)


# 퀴즈 5
# 50명의 승객과 매칭 기회가 있을 때, 총 탑승 승객 수를 구하는 프로그램

# 조건1 : 승객별 운행 소요 시간은 5분 ~ 50분 사이의 난수
# 조건2 : 소요 시간 5분 ~ 15분 사이의 승객만 매칭해야 함

from random import *

cnt = 0
for i in range(1, 51):
    time = randint(5, 50)
    if( 5 <= time <= 15):
        match = "O"
        cnt += 1
    else:
        match = " "
    print("[{0}] {1}번째 손님 (소요시간 : {2}분)" .format(match, i, time))

print("총 탑승 승객 : {0} 분" .format(cnt))

