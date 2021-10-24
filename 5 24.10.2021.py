username="Admin"
password="1234"
canLogIn=bool(False)

while(canLogIn == False):
    tempUsername=input("Podaj username: ")
    tempPassword=input("Podaj hasło: ")
    if (tempUsername==username and tempPassword==password):
        canLogIn=True
        print ("Podano poprawne dane logowania")

