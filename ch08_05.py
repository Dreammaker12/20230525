class item():
    def __init__(self, name, price, weight, isdroppable):
        self.name = name
        self.price = price
        self.weight = weight
        self.isdroppable = isdroppable
    
    def items(self):
        print(f"이름은 {self.name} 가격은 {self.price}원 무게는 {self.weight}kg")

    def discard(self):
        if self.isdroppable:
            print(f"{self.name} 버릴 수 있습니다.")
        else:
            print(f"{self.name} 버릴 수 없습니다.")


class WearableItem(item):
    def __init__(self, name, price, weight, isdroppable, effect):
        super().__init__(name,price, weight, isdroppable)
        self.effect = effect
    def wear(self):
        print(f"{self.name}을 착용했습니다.{self.effect}")
class UsableItem(item):
    def __init__(self, name, price, weight, isdroppable, effect):
        super().__init__(name,price, weight, isdroppable)
        self.effect = effect
    def wear(self):
        print(f"{self.name}을 사용했습니다.{self.effect}")

#인스턴스 생성 
sword = WearableItem("닌자의 검", 3000, 2.5,True,"체력 5000증가, 마력 5000증가" )
sword.wear()
sword.items()
sword.discard()

potion = UsableItem("신비한투명물약",150000,0.1,False,"투명효과 300초 지속")
potion.wear()
potion.items()
potion.discard()
