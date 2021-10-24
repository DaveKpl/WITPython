a=int(24)
b=int(36)

i=int(1)
j=int(1)

wynikA=int(24)
wynikB=int(36)

while not(wynikA==wynikB):
    wynikA=a*i
    wynikB=b*j
    if (wynikA>wynikB):
        j+=1
    elif (wynikA<wynikB):
        i+=1

print("Najmniejsza wspólna wielokrotność to " + str(wynikA))
