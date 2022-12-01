#rijbewijs nr2 ()
from datetime import date

birth_day=int(input("Enter your day of birth: "))
birth_month=int(input("Enter your month of birth: "))
birth_year=int(input("Enter your year of birth: "))

current_day=date.today().day
current_month=date.today().month
current_year=date.today().year


date.today().year

from datetime import date

def Calculate_Age(birthdate):
 current_date=date.today()
 Age=current_date. year-birthdate.year
 return Age

age=Calculate_Age(date(2005,10,4))
print(f"Je bent: {age} jaar")

age = int(input('Please enter your age.'))

if age < 16: print('not allowed driving motor vehicles ')
if age > 15: print('allowed driving scooter')
if age > 20: print('allowd driving motor')
if age > 17: print('allowed driving car.')