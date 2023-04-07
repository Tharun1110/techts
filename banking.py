bal=270000
def balinfo():
    print("current balance =",bal)
def withdraw(w):
    global bal
    if(w<bal):
        bal=bal-w
        print("debited amount=",w)
        print("current balance=",bal)
    else:
        print("insufficient balance")
def deposit(d):
    global bal
    bal=bal+d
    print("credited amount=",d)
    print("current balance=",bal)