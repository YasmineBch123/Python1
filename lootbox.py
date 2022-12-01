while True:

 print("Lootbox!")
 import random
 randomize=("Common","common","common","common","Uncommon","Uncommon","Uncommon","Rare","Rare""Rare","Epic","Epic","Legendary")

 begin = input("Wil je de lootbox openen? : ")
 if begin == "ja":
    print("Je hebt een! :")
    print(random.choice(randomize))
 else:
    print("Lootbox denied.")
    break
# 17 Lootbox (2)