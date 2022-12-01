#18. Faculteit (1)                                       
# je moet input gebruiken omdat je het zelf moet invoeren
# int om het in hele getallen te krijgen                 
nummer = int(input("voer een nummer in"))                
faculteit = 1                                            
if nummer < 0:                                           
   print("faculteit bestaat niet")                       
elif nummer == 0:                                        
   print("de faculteit van 0 is 1")                      
else:                                                         
   for i in range(1,nummer + 1):                         
       faculteit = faculteit*i                    
       print("faculteit van",nummer,"is",faculteit)
       