# 클래스, _init_, 멤버 변수, 메소드, 상속
# 다중상속, 메소드 오버라이딩, pass, super
# 스타크래프트 프로젝트

### 클래스
class Unit:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage
        print("{0} 유닛이 생성 되었습니다.".format(self.name))
        print("체력 {0}, 공격력 {1}".format(self.hp, self.damage))

marine1 = Unit("마린", 40, 5) # self 제외 넘겨줌
marine2 = Unit("마린", 40, 5)
tank = Unit("탱크", 150, 35)

### __init__ : 생성자
# 객체 : 클래스로부터 만들어진 마린1, 마린2, 탱크
# unit 클래스의 인스턴스 : 마린, 탱크
# 객체 생성시 self 제외 나머지 인자 모두 넘겨줘야함

### 멤버변수
# self.name, self.hp, self.damage
wraith1 = Unit("레이스", 80, 5)
print("유닛 이름 : {0}, 공격력 : {1}".format(wraith1.name, wraith1.damage)) # 외부에서 참조 가능

# 클래스 확장 가능
wraith2 = Unit("빼앗은 레이스", 80, 5)
wraith2.clocking = True
if wraith2.clocking == True:
    print("{0} 는 현재 클로킹 상태입니다.".format(wraith2.name))

# 공격 유닛
class AttackUnit:
    def __init__(self, name, hp, damage):
        self.name = name    # 그냥 name은 넘겨받은 인자
        self.hp = hp
        self.damage = damage
    
    def attack(self, location):
        print("{0} : {1} 방향으로 적군을 공격 합니다. [공격력 : {2}]"\
            .format(self.name, location, self.damage)) # self.무엇 을 통해 자기 자신의 변수 접근함.

    def damaged(self, damage):
        print("{0} : {1} 데미지를 입었습니다." .format(self.name, damage))
        self.hp -= damage
        print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0} : 파괴되었습니다.".format(self.name))

firebat1 = AttackUnit("파이어뱃", 50, 16)
firebat1.attack("5시")

firebat1.damaged(25)
firebat1.damaged(25)