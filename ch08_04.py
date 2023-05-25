import random

class Monster:
    max_num = 1000
    def __init__(self, name, health, attack):
        self.name = name
        self.health = health
        self.attack = attack
        Monster.max_num -=1
        print(f"가능한 몬스터 수 : {Monster.max_num}")
    def move(self):
        print(f"{self.name} 지상에서 이동하기")
#eagle에 속성 3개 추가하기 #생성자 오버라이딩
class Wolf(Monster):
    pass
class Shark(Monster):
    def __init__(self, name, health, attack):
        super().__init__(name, health, attack)
        self.skills = ("돌진하기","하늘로 공중부양","몸통박치기")
    def mov(self):
        print(f"[{self.name}] 헤엄치기")
    def skill(self):
        print(f"[{self.name}]의 회심의 공격: {self.skills[random.randint(0,2)]}")

class eagle(Monster):
    def __init__(self, name, health, attack):
        super().__init__(name, health, attack)
        self.skills = ("박치기","날아서찌르기","발톱공격")

    def mov(self):
        print(f"[{self.name}] 하늘 한 바퀴 돌기")
    def skill(self):
        print(f"[{self.name}]의 회심의 공격: {self.skills[random.randint(0,2)]}")

bald_eagle = eagle("대머리독수리",8000,2000)
bald_eagle.skill()
print(Monster.max_num)

shark = Shark("백상아리",100000,2000)
shark.skill()

red_shark = Shark("붉은상아리",100000,2000)
shark.skill()