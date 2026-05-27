class Champion:
    def __init__(self, nama, region, hubungan):
        self.nama = nama
        self.region = region
        self.hubungan = hubungan

    def __str__(self):
        return (
            f"{self.nama} berasal dari {self.region} "
            f"dan memiliki hubungan sebagai {self.hubungan}"
        )

    def __eq__(self, other):
        return self.hubungan == other.hubungan

    def __lt__(self, other):
        return self.hubungan < other.hubungan

    def __gt__(self, other):
        return self.hubungan > other.hubungan

champion1 = Champion("Garen", "Demacia", "Kakak")
champion2 = Champion("Katarina", "Noxus", "Kekasih")
champion3 = Champion("Lux", "Demacia", "Adik")

print(champion1)
print(champion2)
print(champion3)

print()

print("Apakah hubungan Garen == Lux?", champion1 == champion3)
print("Apakah hubungan Garen < Katarina?", champion1 < champion2)
print("Apakah hubungan Katarina > Lux?", champion2 > champion3)