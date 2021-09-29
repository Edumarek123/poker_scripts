#Poker Theory and Analytics

#Functions

def win_Percentage():
    n_cards=int(input("Draw Pool Number: ")) #cards needed
    cards_bf=0
    while(cards_bf!=1 and cards_bf!=2):
    	cards_bf=int(input("Cards Before You Fold: "))

    if(cards_bf==1):
    	win_p=n_cards*2
    else:
    	win_p=n-cards*4

    print("Win Percentage: " + str(round(win_p, 2)) + "%")

    return(win_p)

def Mratio():
    stack=float(input("Stack: "))
    sb=float(input("Small Blind: "))
    bb=float(input("Big Blind: "))
    Santes=float(input("Antes Sum: "))

    players=int(input("Current Players Number: "))
    Splayers=int(input("Players Number Sum: "))

    M=stack/(sb+bb+Santes)
    Me=M*(players/Splayers)

    print("M-ratio: "+ str(round(M, 2)))
    print("Effective M-ratio: "+ str(round(Me, 2)))

def expected_Value():
    win_p=float(input("Win Percentage: "))
    lose_p=100-win_p
    win_amt=float(input("Win Amount: "))
    lose_amt=float(input("Lose Amount: "))

    EV=(win_p*win_amt)-(lose_p*lose_amt)

    print("Expected Value: $" + str(round(EV, 2)))

def potNimplied_Odds(win_p):
    pot=float(input("Pot Amount: "))
    bet_amt=float(input("Bet Amount: "))
    call_amt=float(input("Call Amount: "))

    sum_amt=pot+bet_amt+call_amt
    odds=call_amt/sum_amt
    implied=(bet_amt/(win_p/100))-sum_amt

    print("Win Percentage: " + str(round(win_p, 2)) + "%")
    print("Pot Odds: " + str(round(odds*100, 2)) + "%")
    print("Implied Odds: $" + str(round(implied, 2)))

def max_Bet(win_p):
    pot=float(input("Pot Amount: "))

    lose_p=100-win_p
    max_bet=((win_p*pot)/(lose_p-win_p))

    print("The Maximum Bet Call Is: $" + str(max_bet))
    #return(max_bet)

#Main
potNimplied_Odds(win_Percentage())
