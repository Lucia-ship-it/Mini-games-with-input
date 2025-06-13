# import random

# def random_number (min,max):
#     """vrati nahodne cislo v rozsahu, ktory mu nastavim"""
#     return random.randint(min, max)

# print(random_number(1,10))

# Import modulu
import random 

# Definice funkce
def nahodne_cislo(min, max):
   return random.randint(min, max)

# Volání funkce s různými rozsahy
print(f"Náhodné číslo mezi 1 a 10: {nahodne_cislo(1, 10)}")
