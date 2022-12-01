import random

print("Welkom bij mijn dobbelsteen")

while True:
    
    numberPicked = int(input("kies tussen de 1 en 10000"))
    if(numberPicked > 0 and numberPicked < 10000):
      break

def rollDice(amountOfDice):
    totalSum = 0
    possibleFaces = [1,2,3,4,5,6]
    for dice in range (amountOfDice):
        roll = random.choice(possibleFaces)
        print("Nummer ", dice + 1,":", roll)
        totalSum += roll        
                                
    print("totale som", totalSum)
                                 
                                 
    rollDice(numberPicked)       

