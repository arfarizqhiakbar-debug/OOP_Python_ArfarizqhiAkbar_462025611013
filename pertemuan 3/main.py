class champion:
    def __init__(self, nama, region, lore):
        self.name = nama
        self.region = region
        self.lore = lore

    def tampilkan_data(self):
        print("Nama     :", self.name)
        print("Region   :", self.region)
        print("Lore     :", self.lore)

    def region_info(self):
        print(f"{self.name} berasal dari {self.region}.")
        
    def runeterra(self):
        print("Runeterra adalah dunia tempat para champion berjuang.")
        
champion1 = champion("Garen", "Demacia", "Seorang prajurit yang setia kepada Demacia.")
champion2 = champion("Darius", "Noxus", "Seorang pejuang yang kuat dan berjiwa besar.")


print("=== Champion 1 ===")
champion1.tampilkan_data()
champion1.region_info()

print()

print("=== Champion 2 ===")
champion2.tampilkan_data()
champion2.region_info()
champion2.runeterra()

print()

champion.runeterra()

champion1.runeterra()