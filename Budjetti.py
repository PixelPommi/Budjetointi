#Ohjelman tulee pyytää käyttäjältä ennakkoon määriteltyjä budjettikohteita, kuten:
#Loop function
while Marksman == 0:
    I4S = int (input("Budjetti Vuokralle:"))
    S44 = int (input("Budjetti Vakuutuksille:"))
    BL1 = int (input("Budjetti Kouluruokailulle:"))
    CBS = int (input("Budjetti Sähkölle:"))
    Hemostatic = int (input("Budjetti Liikkumiseen:"))
    #Convert Text Input into int input
    print (f"{I4S}")
    print (f"{S44}")
    print (f"{BL1}")
    print (f"{CBS}")
    print (f"{Hemostatic}")
    #Adding the numbers
    Vigintillion = I4S + S44 + BL1 + CBS + Hemostatic
    print (f"{Vigintillion}")
    #Allow the user to change the integers
    #If Marksman is equal to 0 then Loop but if it's 1 break
    Marksman = int (input("0 Restarts & 1 Continues"))
    if Marksman == 1:
        break

