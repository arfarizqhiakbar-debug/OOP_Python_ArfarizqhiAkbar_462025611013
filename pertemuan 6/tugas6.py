class Champion:
    def __init__(self, name, region):
        self.name = name
        self.region = region

    def info(self):
        print(f"Champion {self.name} berasal dari region {self.region}")

    def role(self):
        print(f"{self.name} memiliki role dasar sebagai petarung")

    def weapon(self):
        print(f"{self.name} menggunakan senjata standar")


class Warrior(Champion):

    def weapon(self):
        print(f"{self.name} menggunakan pedang besar khas ksatria")

    def attack(self):
        print(f"{self.name} menyerang dengan physical damage")

    def weapon_parent(self):
        super().weapon()


class Ultimate(Champion):

    def role(self):
        print(f"{self.name} memiliki ultimate skill yang sangat mematikan")

    def skill(self):
        print(f"{self.name} mengeluarkan ultimate dengan damage besar")

    def role_parent(self):
        super().role()


class BattleMaster(Warrior, Ultimate):

    def combo_skill(self):
        print(f"{self.name} menggabungkan serangan pedang dan ultimate skill")


player1 = BattleMaster("Garen", "Demacia")

player1.info()

player1.weapon()

player1.skill()

player1.combo_skill()

player1.weapon_parent()

player1.role_parent()

print("MRO :", BattleMaster.__mro__)