# 챕터8 - 표준입출력, 다양한 출력포맷, 파일입출력, pickle, with

### 표준출력
# sep: 출력시 사이에 ""를 넣음, end: 마지막에 ""로 끝남
print("Python", "Java", "JavaScript", sep=",", end="?") 
print()

import sys
print("Python", "Java", file=sys.stdout)
print("Python", "Java", file=sys.stderr)

# 시험 성적
scores = {"수학":0, "영어":50, "코딩":100}
for subject, score in scores.items():
    # 왼쪽으로 8칸 확보, 왼쪽 정렬 // 오른 정렬 4칸
    print(subject.ljust(8), str(score).rjust(4)) 

# 001, 002, 003 , ...
for num in range(1, 21):
    # 3개의 공간에 대해 빈 공간은 0으로 채움
    print("대기번호 : " + str(num).zfill(3))

### 표준 입력
answer = input("아무 값이나 입력하쇼 : ")
print("입력한 값은 : " + answer)
print(type(answer)) # string !

### 다양한 출력포맷
# 빈 자리는 빈공간으로 두고, 오른쪽 정렬을 하되, 총 10자리 공간 확보
print("{0: >10}".format(500)) # >, < 가 오른쪽, 왼쪽 정렬 방향
# 양수일 땐 +로 표시, 음수일 땐 -로 표시
print("{0: >+10}".format(500))
print("{0: >+10}".format(-500))
# 왼쪽 정렬하고, 빈칸으로 _로 채움
print("{0:_<+10}".format(500)) # : 다음이 표시할 것
# 3자리 마다 콤마를 찍어주기
print("{0:,}".format(100000000000))
# 3자리 마다 콤마를 찍어주기, +- 부호도 붙이기
print("{0:+,}".format(100000000000))
print("{0:+,}".format(-100000000000))
# 3자리 마다 콤마를 찍어주기, +- 부호도 붙이기, 자릿수 확보하기
# 빈 자리는 ^ 채워주기
print("{0:^<+30,}".format(100000000000))
# 소수점 출력
print("{0:f}".format(5/3))
# 소수점 특정 자리수 까지만 표시
print("{0:.2f}".format(5/3)) # 1.67

### 파일 입출력
score_file = open("score.txt", "w", encoding="utf8") # utf8 : 한글
print("수학 : 0", file=score_file)
print("영어 : 50", file=score_file)
score_file.close()

score_file = open("score.txt", "a", encoding="utf8") # a : append, 이어서 씀
score_file.write("과학 : 80")
score_file.write("\n코딩 : 100")
score_file.close()

score_file = open("score.txt", "r", encoding="utf8")
print(score_file.read())
score_file.close()

score_file = open("score.txt", "r", encoding="utf8")
print(score_file.readline(), end="") # 줄별로 읽기, 한 줄 읽고 커서는 다음 줄로 이동
print(score_file.readline(), end="")
print(score_file.readline(), end="")
print(score_file.readline(), end="")
score_file.close()

score_file = open("score.txt", "r", encoding="utf8")
while True:
    line = score_file.readline()
    if not line:
        break
    print(line, end="")
score_file.close()

score_file = open("score.txt", "r", encoding="utf8")
lines = score_file.readlines()
for line in lines:
    print(line, end="")
score_file.close()

## pickle - 가진 정보를 pickle 파일에 저장, 후에 다시 읽어올 수 있음
import pickle
profile_file = open("profile.pickle", "wb") # pickle은 항상 b(binary), encoding은 필요 없음
profile = {"이름":"박명수", "나이":30, "취미":["축구", "골프", "코딩"]}
print(profile)
pickle.dump(profile, profile_file) # profile 에 있는 정보를 file에 저장
profile_file.close()

profile_file = open("profile.pickle", "rb")
profile = pickle.load(profile_file) # file에 있는 정보를 profile에 불러오기
print(profile)
profile_file.close()

## with - 파일 입출력을 더 쉽게
import pickle

with open("profile.pickle", "rb") as profile_file:
    print(pickle.load(profile_file))
    # close 필요 x, with 나가면 자동으로 close

with open("study.txt", "w", encoding="utf8") as study_file:
    study_file.write("파이썬을 열심히 공부하고 있어요")

with open("study.txt", "r", encoding="utf8") as study_file:
    print(study_file.read())

### 퀴즈 8 - 보고서 양식
for i in range(1, 3):
    with open(str(i) + "주차.txt", "w", encoding="utf8") as report_file:
        report_file.write(" - {0} 주차 주간보고 - ".format(i))
        report_file.write("\n부서 :")
        report_file.write("\n이름 :")
        report_file.write("\n업무 요약 :")
