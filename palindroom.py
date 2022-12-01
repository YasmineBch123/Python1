new_str = input("Voer een woord in")
empty_string = ""

for m in new_str:
    empty_string = m + empty_string
print("Omdraaien! :  ", empty_string)

if(new_str == empty_string):
   print("het is een palindrome string")
else:
   print("het is geen palindroom string")

#14 palindroom (2)
#.....