# 챕터 7 - 함수, 전달값과 반환값, 기본값, 키워드값, 가변인자, 지역변수와 전역변수

### 기본값
def profile(name, age=17, main_lang="파이썬"):
    print("이름 : {0}\t나이 : {1}\t주 사용 언어 : {2}"\
        .format(name, age, main_lang))
    
profile("유재석", 20, "자바")
profile("김태호")
profile(main_lang="자바", age=25, name="조세호")

### 가변 인자
# def profile(name, age, lang1, lang2, lang3, lang4, lang5):
#     print("이름 : {0}\t나이 : {1}\t".format(name, age), end=" ") # end : 줄바꿈 없이 ""로 끝남.
#     print(lang1, lang2, lang3, lang4, lang5)
def profile(name, age, *language):
    print("이름 : {0}\t나이 : {1}\t".format(name, age), end=" ") # end : 줄바꿈 없이 ""로 끝남.
    for lang in language:
        print(lang, end=" ")
    print()

profile("유재석", 20, "Python", "Java", "C", "C++", "C#", "JavaScript")
profile("김태호", 25, "Kotlin", "Swift", "", "", "")

### 전역변수 - 사용 선호X
gun = 10
def checkpoint(soldiers):
    global gun
    gun = gun - soldiers
    print(gun)

def checkpoint_ret(gun, soldiers):
    gun = gun - soldiers
    print(gun)
    return gun

checkpoint(2)
gun = checkpoint_ret(gun, 2)


### 퀴즈6 - 표준 체중 구하기
# 남자 : 키(m) x 키(m) x 22
# 여자 : 키(m) x 키(m) x 21

def std_weight(height, gender):
    if gender == "남자":
        print("키 {0}cm 남자의 표준 체중은 {1}kg 입니다.".format(height, round(height*height*22, 3)))
    else:
        print("키 {0}cm 여자의 표준 체중은 {1}kg 입니다.".format(height, round(height*height*21, 2)))
    
std_weight(1.67, "여자")

def std_weight(height, gender):
    if gender == "남자":
        return height * height * 22
    else:
        return height * height * 21

height = 167
gender = "여자"
weight = round(std_weight(height / 100, gender), 2)
print("키 {0}cm {1}의 표준 체중은 {2}kg 입니다.".format(height, gender, weight))
