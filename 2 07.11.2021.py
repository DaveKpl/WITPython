def main():

    lista=[1,2,3,4,5]

    pierwsza_najwieksza,druga_najwieksza,temp=0,0,0

    for c in lista:
        if c>druga_najwieksza: druga_najwieksza=c
        if druga_najwieksza>pierwsza_najwieksza:
            temp=druga_najwieksza
            druga_najwieksza=pierwsza_najwieksza
            pierwsza_najwieksza=temp

    print(f"{pierwsza_najwieksza}\t{druga_najwieksza}")

main()
