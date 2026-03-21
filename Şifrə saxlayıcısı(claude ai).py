# Copyright (c) 2026 Naun Rahimli
# Licensed under the MIT License

import random
import string
import json
import os

# Fayldan şifrələri yüklə
def yuklə():
    if os.path.exists("sifreler.json"):
        with open("sifreler.json", "r") as f:
            content = f.read()
            if content.strip() == "":
                return []
            return json.loads(content)
    return []

# Şifrələri fayla saxla
def saxla(sifreler):
    with open("sifreler.json", "w") as f:
        json.dump(sifreler, f, ensure_ascii=False, indent=2)

# Şifrə yarat
def sifre_yarat():
    uzunluq = int(input("Şifrə neçə simvol olsun? "))
    simvollar = string.ascii_letters + string.digits + string.punctuation
    sifre = ""
    for i in range(uzunluq):
        sifre = sifre + random.choice(simvollar)
    print("Yaradılan şifrə:", sifre)

# Şifrə əlavə et
def elave_et(sifreler):
    sayt = input("Sayt ünvanı: ")
    istifadeci = input("İstifadəçi adı / Gmail: ")
    sifre = input("Şifrə: ")
    isim = input("Bu şablona bir isim ver: ")
    sifreler.append({
        "isim": isim,
        "sayt": sayt,
        "istifadeci": istifadeci,
        "sifre": sifre
    })
    saxla(sifreler)
    print("✅ Əlavə edildi!")

# Şifrələri göstər
def goster(sifreler):
    if len(sifreler) == 0:
        print("Heç bir şifrə yoxdur.")
        return
    print("\n--- Saxlanmış Şifrələr ---")
    for i in range(len(sifreler)):
        print(f"{i+1}. {sifreler[i]['isim']}")
    
    secim = int(input("\nHansını görmək istəyirsən? (rəqəm yaz): "))
    s = sifreler[secim - 1]
    print(f"\nİsim: {s['isim']}")
    print(f"Sayt: {s['sayt']}")
    print(f"İstifadəçi: {s['istifadeci']}")
    print(f"Şifrə: {s['sifre']}")

# Şifrə sil
def sil(sifreler):
    if len(sifreler) == 0:
        print("Heç bir şifrə yoxdur.")
        return
    print("\n--- Saxlanmış Şifrələr ---")
    for i in range(len(sifreler)):
        print(f"{i+1}. {sifreler[i]['isim']}")
    
    secim = int(input("\nHansını silmək istəyirsən? (rəqəm yaz): "))
    silinen = sifreler.pop(secim - 1)
    saxla(sifreler)
    print(f"✅ '{silinen['isim']}' silindi!")

# Ana menyu
sifreler = yuklə()

while True:
    print("\n=== Şifrə Saxlayıcısı ===")
    print("1. Şifrə yarat")
    print("2. Şifrə əlavə et")
    print("3. Şifrələri göstər")
    print("4. Şifrə sil")
    print("5. Çıx")
    
    secim = input("\nSeçimini yaz: ")
    
    if secim == "1":
        sifre_yarat()
    elif secim == "2":
        elave_et(sifreler)
    elif secim == "3":
        goster(sifreler)
    elif secim == "4":
        sil(sifreler)
    elif secim == "5":
        print("Çüüş! 👋")
        break
    else:
        print("Yanlış seçim, yenidən cəhd et.")
