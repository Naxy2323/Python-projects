import random
import string

print("Şifrə generatoru")

uzunluq = int(input("Şifrə neçə simvol olsun?"))

simvollar = string.ascii_letters + string.digits + string.punctuation

sifre = ""

for i in range(uzunluq):
    sifre = sifre + random.choice(simvollar)
    
print("Şifrəniz:", sifre)

"""
sadəcə idle ilə işləyir!!!!!
"""
