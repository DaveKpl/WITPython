wiek=int(input("Ile masz lat?"))

if (wiek>=21):
    print("Możesz prowadzić samochód oraz głosować w wyborach")
elif(wiek>17):
    print("Możesz prowadzić samochód")
else:
    print("Nie możesz głosować ani prowadzić samochodu")