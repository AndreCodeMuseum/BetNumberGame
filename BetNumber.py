import random

randomNumber= random.randint(1,100)


chances = 6
betList = []
while chances > 0:
    
    
    bet = int(input("Bet a number between 1 to 100: "))
    if bet <= 100:

        betList.append(bet)
        print() 
        chances-=1
    
        if bet == randomNumber:
            print("You've got it!")
            print(randomNumber, "is the correct bet!")
            break

        else:
            
            print("Try again!")
            print("You've got", chances, "chance(s) left")
            print("Your last bet(s):")
            for elements in reversed(betList):
                print(elements, end=" ")
            print()
 
        if bet < randomNumber:
            print("Try a number higer!")
            print()
        else:
            print("Try a number lower!")
            print()
        
        if chances == 0:
            print()
            print("Your chances are over")
            print("The number was", randomNumber)
            print("Sorry, maybe next time!")
            break 
    else:
        print("Please insert a number equal or lower than 100")




