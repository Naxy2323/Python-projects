# Copyright (c) 2026 Naun Rahimli
# Licensed under the MIT License

"""
sadəcə idle ilə işləyir!!!!!
"""


import random

seçimlər = ["daş", "kağız", "qayçı"]

print("Oyuna xoş gəldin!")

kompüter = random.choice(seçimlər)
oyunçu = input("Seçimini yaz (daş / kağız / qayçı): ")

print("Sən seçdin:", oyunçu)
print("Kompüter seçdi:", kompüter)

if oyunçu == kompüter :
    print("Bərabərə!")
elif oyunçu == "daş" and kompüter == "qayçı":
    print("Sən qazan!")
elif oyunçu == "kağız" and kompüter == "daş":
    print("Sən qazan!")
elif oyunçu == "qayçı" and kompüter == "kağız":
    print("Sən qazan!")
else:
    print("Kompüter qazandı!")

