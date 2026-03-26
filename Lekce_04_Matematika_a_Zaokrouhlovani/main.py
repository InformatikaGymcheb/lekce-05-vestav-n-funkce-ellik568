# ÚLOHA 1: Zvětšovač (použij +=)
cislo = int(input("Zadej číslo: "))
# Sem doplň kód:
cislo = int(input("3"))
cislo += 10
print("Výsledek:", cislo)


# ÚLOHA 2: Útrata (zaokrouhli na 2 místa)
celkem = float(input("Celková suma (Kč): "))
lidi = int(input("Počet lidí: "))
# Sem doplň výpočet a print s round():

celkem = float(input("Celková suma (Kč): 240.0"))
lidi = int(input("Počet lidí: 3"))
na_osobu = celkem / lidi
print("Každý zaplatí:", round(na_osobu, 2), "Kč")


# ÚLOHA 3: Plocha kruhu (zaokrouhli na celé číslo)
r = float(input("Zadej poloměr: "))
# plocha = 3.14 * r * r
# Sem doplň kód:
r = float(input("Zadej poloměr: 30"))
plocha = 3.14 * r * r
print(f"Plocha je {round(plocha)} Kč")
