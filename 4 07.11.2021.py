def main():

    dane_logowania={'Admin':'1234'}
    myLogin,myPass="",""
    counter=0

    while dane_logowania.get(myLogin)!=myPass:
        if counter>0: print("Bledne dane, wprowadz ponownie")
        myLogin = input("Podaj login: ")
        myPass = input("Podaj haslo: ")
        counter+=1

    print("Logowanie poprawne")
main()
