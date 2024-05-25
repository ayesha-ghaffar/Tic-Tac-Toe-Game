
print("WELCOME   TO   TICK-TAC-TOE   GAME")
print("\n","                      MENU                      ", "\n")     #menu
print("1)  Press 1 to Play Game.","\n", "2)  press 2 to Exit")
print("  ")
option=eval(input("Enter your desired option here 1 or 2 :"))
while (option != 1) and (option!=2) :       # for wrong option 
    print("  ")
    print ("Wrong Input ! Please Enter 1 or 2 to proceed...")
    print(" ")
    option=eval(input("Enter your desired option here 1 or 2 : "))
while option==1 :
    print("\n", "Game Starts", "\n")       # Game starts 
    player1= input("Enter the name of Player 1 : ")         #Player 1 name
    player2= input("Enter the name of Player 2 : ")          #Player 2 name
    print ("  ")
    symbol1=input(player1 + " Enter your symbol here  (X or O) : ")      # Player 1 symbol
    symbol1=symbol1.capitalize()
    print("  ")
    while (symbol1!="O"  and symbol1!="X"):    # For wrong symbol
            print("   ")
            print ("Symbol is invalid !")
            print("   ")
            symbol1=input("Symbol of Player 1 (X or O) : ")
            symbol1=symbol1.capitalize()
    if symbol1=="X":                                    # Player 2 symbol
        symbol2="O"
        print("       ")
        print(player1, "'s symbol  is ",symbol1)
        print(player2,"'s symbol  is ",symbol2)
        print("       ")
    elif symbol1=="O":
        symbol2="X"
        print(player1, "'s symbol  is ",symbol1)
        print(player2,"'s symbol  is ",symbol2)
    print ("   ")
    print("Let's have a toss")             # Toss
    print("    ")
    import random
    num=random.randint(0,1)
    print(num)
    if num==0:
        toss1='head'
        toss2='heads'
        toss3='HEAD'
        toss4='HEADS'
        toss5='Head'
        toss6='Heads'
    elif num==1:
        toss1='tail'
        toss2='tails'
        toss3='TAIL'
        toss4='TAILS'
        toss5='Tail'
        toss6='Tails'
    guess1=input("Guess of toss by "+ player1 + ": ")       #  Toss Guess 
    print(toss3)
    if (guess1==toss1) or (guess1==toss2) or (guess1==toss3) or (guess1==toss4) or (guess1==toss5) or (guess1==toss6):
        Player1=player1
        Player2=player2
        Symbol1=symbol1                                      # Swapping according to need
        Symbol2=symbol2
    elif (guess1!=toss1) or (guess1!=toss2) or (guess1!=toss3) or (guess1!=toss4) or (guess1!=toss5) or (guess1!=toss6):
        Player1=player2
        Player2=player1
        Symbol1=symbol2
        Symbol2=symbol1
    print ("  ")
    print (Player1, " won the toss ! and got 1st move  ")
    print ("  ")
    num1, num2, num3, num4, num5, num6, num7, num8, num9 = 1, 2, 3, 4, 5, 6, 7, 8, 9
    for i in range (1,6):     # Outer loop taking 5 turns out of 9
        print (num1," | ",  num2, " | ",  num3)
        print("---", "-----", "---")
        print(num4, " | ",  num5, " | ",  num6)      # Grid
        print("---", "-----", "---")
        print(num7, " | ",  num8, " | ",  num9)
        m1=str(input(Player1+"'s turn.....Please Choose between 1 to 9 :"))  # Taking turn
        while m1!="1" and m1!="2" and m1!="3"  and m1!="4" and m1!="5" and m1!="6" and m1!="7" and m1!="8" and m1!="9"  :
            print("  ")
            print("Wrong Input ! Please choose between 1 to 9 : ")
            print("  ")
            m1=str(input(Player1+"'s turn.....Please Choose between 1 to 9 :"))
        m1=int(m1)
            # Conditions for replacing input position with symbol
        if m1==1  and num1!=1:
            print("Please choose another position. This is already occupied ! ")
            continue
        elif m1==1  and num1 ==1:
            num1=Symbol1
        if m1==2   and num2!=2:
            print("Please choose another position. This is already occupied ! ")
            continue
        elif m1==2  and num2 ==2:
            num2=Symbol1
        if m1==3   and num3!=3:
            print("Please choose another position. This is already occupied ! ")
            continue
        elif m1==3  and num3 ==3:
            num3=Symbol1
        if m1==4   and num4!=4:
            print("Please choose another position. This is already occupied ! ")
            continue
        elif m1==4   and num4 ==4:
            num4=Symbol1
        if m1==5  and num5!=5 :
            print("Please choose another position. This is already occupied ! ")
            continue
        elif m1==5  and num5 ==5:
            num5=Symbol1
        if m1==6   and num6!=6 :
            print("Please choose another position. This is already occupied ! ")
            continue
        elif m1==6  and num6 ==6:
            num6=Symbol1
        if m1==7  and num7!=7 :
            print("Please choose another position. This is already occupied ! ")
            continue
        elif m1==7  and num7==7:
            num7=Symbol1
        if m1==8   and num8!=8:
            print("Please choose another position. This is already occupied ! ")
            continue
        elif m1==8 and num8 ==8:
            num8=Symbol1
        if m1==9  and num9!=9 :
            print("Please choose another position. This is already occupied ! ")
            continue
        elif m1==9  and num9 ==9 :
            num9=Symbol1
            # Winning condition if player 1 wins
        if (num1==num2==num3==Symbol1) or (num4==num5==num6==Symbol1) or (num7==num8==num9==Symbol1 )or(num1==num4==num7==Symbol1) or (num2==num5==num8==Symbol1) or (num3==num6==num9==Symbol1 ) or (num1==num5==num9==Symbol1) or (num3==num5==num7==Symbol1):
            print("CONGRATULATIONS !  ", Player1, "WON THE GAME !")
            print (num1," | ",  num2, " | ",  num3)
            print("---", "-----", "---")
            print(num4, " | ",  num5, " | ",  num6)
            print("---", "-----", "---")
            print(num7, " | ",  num8, " | ",  num9)
            print(" ")
            print ("Enter Y to play another game...")     # Asking for another game
            print ("Enter  Z to exit the game...")
            choice=(input())
            choice=choice.capitalize()
            while (choice !="y") and (choice!="Y") and (choice != "z") and (choice !="Z") :
                print ("Invalid input ! Please enter Y or Z to proceed ....")
                choice=input()
                choice=choice.capitalize()
            if choice=="Y":
                option=1
                break
            elif choice=="Z":
                option=2
                break
            # Winning conditions if Player 2 wins
        elif (num1==num2==num3==Symbol2) or (num4==num5==num6==Symbol2) or (num7==num8==num9==Symbol2) or (num1==num4==num7==Symbol2) or (num2==num5==num8==Symbol2) or (num3==num6==num9==Symbol2 ) or (num1==num5==num9==Symbol2) or (num3==num5==num7==Symbol2):
            print ("CONGRATULATIONS ! ", Player2, " WON THE GAME !")
            print (num1," | ",  num2, " | ",  num3)
            print ("---", "-----", "---")
            print (num4, " | ",  num5, " | ",  num6)
            print ("---", "-----", "---")
            print (num7, " | ",  num8, " | ",  num9)
            print (" ")
            print ("Enter Y to play another game...")
            print ("Enter  Z to exit the game...")
            choice=(input())
            choice=choice.capitalize()
            while (choice !="y") and (choice!="Y") and (choice != "z") and (choice !="Z") :
                print ("Invalid input ! Please enter Y or Z to proceed ....")
                choice=input()
                choice=choice.capitalize()
            if choice=="Y":
                option=1
                break
            elif choice=="Z":
                option=2
                break
            # Inner loop taking 4 turns
        for j in range (1,5):
            if i==5 :
                print("GAME IS DRAW !")            #Game draw condition if overall it's 9th turn and yet no one wins 
                print ("Enter Y to play another game...")
                print ("Enter  Z to exit the game...")
                choice=input()
                choice=choice.capitalize()
                if choice=="Y":
                    option=1
                    break
                elif choice=="Z":
                    option=2
                    break
            print (num1," | ",  num2, " | ",  num3)
            print("---", "-----", "---")
            print(num4, " | ",  num5, " | ",  num6)
            print("---", "-----",  "---")
            print(num7, " | ",  num8, " | ",  num9)
            m2=str(input(Player2+"'s turn.....Please Choose between 1 to 9 :"))
            # Replacing Symbols
            while  m2!="1" and m2!="2" and m2!="3"  and m2!="4" and m2!="5" and m2!="6" and m2!="7" and m2!="8" and m2!="9" :
                print(" ")
                print ("Wrong Input ! Please choose between 1 to 9")
                print(" ")
                m2=str(input(Player2+"'s turn.....Please Choose between 1 to 9 :"))
            m2=int(m2)
            if m2==1   and num1!=1 :
                print("Please choose another position. This is already occupied ! ")
                continue
            elif m2==1  and num1 == 1 :
                num1=Symbol2
                break
            if m2==2  and num2!=2 :
                print("Please choose another position. This is already occupied ! ")
                continue
            elif m2==2   and num2 ==2:
                num2=Symbol2
                break
            if m2==3  and num3!=3:
                print("Please choose another position. This is already occupied ! ")
                continue
            elif m2==3 and num3 ==3:
                num3=Symbol2
                break
            if m2==4 and num4!=4:
                print("Please choose another position. This is already occupied ! ")
                continue
            elif m2==4 and num4 ==4:
                num4=Symbol2
                break
            if  m2==5  and num5!=5:
                print("Please choose another position. This is already occupied ! ")
                continue
            elif m2==5  and num5 ==5:
                num5=Symbol2
                break
            if m2==6  and num6!=6 :
                print("Please choose another position. This is already occupied ! ")
                continue
            elif m2==6  and num6 ==6:
                num6=Symbol2
                break
            if m2==7   and num7!=7:
                print("Please choose another position. This is already occupied ! ")
                continue
            elif m2==7   and num7==7:
                num7=Symbol2
                break
            if m2==8  and num8!=8 :
                print("Please choose another position. This is already occupied ! ")
                continue
            elif m2==8   and num8 ==8:
                num8=Symbol2
                break
            if m2==9  and num9!=9:
                print("Please choose another position. This is already occupied ! ")
                continue
            elif m2==9   and num9 ==9 :
                num9=Symbol2
                break
            # Winning conditions for Player 1
        if (num1 == num2 == num3 == Symbol1) or (num4 == num5 == num6 == Symbol1) or (num7 == num8 == num9 == Symbol1) or (num1 == num4 == num7 == Symbol1) or (num2 == num5 == num8 == Symbol1) or (num3 == num6==num9==Symbol1 ) or (num1==num5==num9==Symbol1) or (num3==num5==num7==Symbol1):
            print("CONGRATULATIONS ! ", Player1, " WON THE GAME !")
            print (num1," | ",  num2, " | ",  num3)
            print("---", "-----", "---")
            print(num4, " | ",  num5, " | ",  num6)
            print("---", "-----", "---")
            print(num7, " | ",  num8, " | ",  num9)
            print(" ")
            print ("Enter Y to play another game...")          # Asking for another game
            print ("Enter  Z to exit the game...")
            choice=(input())
            choice=choice.capitalize()
            while (choice !="y") and (choice!="Y") and (choice != "z") and (choice !="Z") :
                print ("Invalid input ! Please enter Y or Z to proceed ....")
                choice=input()
                choice=choice.capitalize()
            if choice=="Y":
                option=1
                break
            elif choice=="Z":
                option=2
                break
            #Winning conditions for Player 2
        elif (num1 == num2 == num3 == Symbol2) or (num4 == num5 == num6 == Symbol2) or (num7 == num8 == num9 == Symbol2)or(num1 == num4 == num7 == Symbol2) or (num2 == num5 == num8 == Symbol2) or (num3 == num6 == num9 == Symbol2 ) or (num1 == num5 == num9 == Symbol2) or (num3 == num5==num7==Symbol2):
            print("CONGRATULATIONS ! ", Player2, " WON THE GAME !")
            print (num1," | ",  num2, " | ",  num3)
            print("---", "-----", "---")
            print(num4, " | ",  num5, " | ",  num6)
            print("---", "-----", "---")
            print(num7, " | ",  num8, " | ",  num9)
            print(" ")
            print(" ")
            print ("Enter Y to play another game...")
            print ("Enter  Z to exit the game...")
            choice=(input())
            choice=choice.capitalize()
            while (choice !="y") and (choice!="Y") and (choice != "z") and (choice !="Z") :
                print ("Invalid input ! Please enter Y or Z to proceed ....")
                choice=input()
                choice=choice.capitalize()
            if choice=="Y":
                option=1
                break
            elif choice=="Z":
                option=2
                break
            
print("GAME EXIT !")
                    
