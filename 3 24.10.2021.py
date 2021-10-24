predkosc=int(input("Jaka jest średnia prędkość na tej trasie? "))

dlugosc=int(250*60/predkosc)

if (dlugosc< 165):
    print ("Samochodem dojedziesz szybciej niż pociągiem, czyli w " + str(dlugosc) + " minut.")
elif (dlugosc==165):
    print ("Samochodem dojedziesz tak samo szybko jak pociągiem, czyli w " + str(dlugosc) + " minut.")
else:
    print("Samochodem dojedziesz wolniej niż pociągiem, czyli w " + str(dlugosc) + " minut.")
