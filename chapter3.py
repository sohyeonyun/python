# 챕터 3 - 문자열, 슬라이싱, 문자열처리함수, 문자열포맷, 탈출문자

## 문자열
sentence = """
안녕하세요,
반가워요
"""
print(sentence)

## 슬라이싱
jumin = "991231-1234567"
print("성별 : " + jumin[7])
print("연 : " + jumin[0:2])
print("월 : " + jumin[2:4])
print("생년월일 : " + jumin[:6])
print("뒤 7자리 : " + jumin[7:])
print("뒤 7자리 (뒤에부터) : " + jumin[-7:]) # 맨 뒤에서 7번째까지 1234567

## 문자열처리함수
python = "Python is Amazing"
print(python.lower())
print(python.upper())
print(python[0].isupper())
print(len(python))
print(python.replace("Python", "Java"))

index = python.index("n") # 첫 번째 n
print(index)
index = python.index("n", index + 1) # 두 번째 n
print(index)

print(python.find("n"))
print(python.find("Java")) # 없음 -> -1
# print(python.index("Java")) # 없음 -> error

print(python.count("n")) # 2

## 문자열 포맷
# 방법 1
print("나는 %d살입니다." % 22) # %s 도 가능
print("나는 %s를 좋아해요." % "오버워치")
print("Overwatch은 %c로 시작해요." % 'O') # %s 도 가능
print("나는 %s와 %s 캐릭터를 좋아해요." % ("아나", "젠야타"))

# 방법 2
print("나는 {}살입니다." .format(22))
print("나는 {}와 {} 캐릭터를 좋아해요. " .format("아나", "젠야타"))
print("나는 {0}와 {1} 캐릭터를 좋아해요. " .format("아나", "젠야타")) # 0, 1번째
print("나는 {1}와 {0} 캐릭터를 좋아해요. " .format("아나", "젠야타"))

# 방법 3
print("나는 {age}살이며, {game} 게임을 좋아해요." .format(age=22, game="오버워치"))
print("나는 {age}살이며, {game} 게임을 좋아해요." .format(game="오버워치", age=22))

# 방법 4 (v3.6 이상~)
age = 22
game = "오버워치"
print(f"나는 {age}살이며, {game} 게임을 좋아해요.")


## 탈출문자
# \n : 줄바꿈
print("백문이 불여일견\n백견이 불여일타")
# \" \' : 문장 내에서 따옴표
print("저는 \"윤소현\"입니다.")
# \\ : 문장 내에서 \
print("C:\\Users\\Desktop")
# \r : 커서를 맨 앞으로 이동
print("Red Apple\rPine")
# \b : 백스페이스 (한 글자 삭제)
print("Redd\bApple")
# \t : 탭
print("Red\tApple")


## 퀴즈 3
# 사이트별 비밀번호 만들어주는 프로그램
# 예) http://naver.com 
# 규칙1 : http:// 부분 제외 => naver.com
# 규칙2 : 처음 만나는 점(.) 이후 부분 제외 => naver
# 규칙3 : 남은 글자 중 처음 세 자리(nav) + 글자 개수(5) + 글자 내 'e' 개수(1) + "!" 로 구성
# 예) 생성된 비밀번호 : nav51!

url = "http://naver.com"
url = url[7 : url.index('.')]
password = url[:3] + str(len(url)) + str(url.count("e")) + "!"
print(password)

url = "http://naver.com"
my_str = url.replace("http://", "") # 규칙1
my_str = my_str[:my_str.index(".")] # 규칙2
password = my_str[:3] + str(len(my_str)) + str(my_str.count("e")) + "!"
print("{0} 의 비밀번호는 {1} 입니다." .format(url, password))

