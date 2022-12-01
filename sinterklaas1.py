#12. Sinterklaas verlanglijst (2)
# creating an empty list                        
lijst = []

while not ("KLAAR!") in lijst:
 lijst.append(input("Welke item wil je : "))
else:
    lijst.remove("KLAAR!")
    print("Uw lijst is : ", sorted(lijst))

