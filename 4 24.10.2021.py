kapital=float(input("Jaki jest twoj kapital poczatkowy? "))
wplywy=float(input("Jakie sa miesieczne wpływy? "))
okres=float(input("Jaki jest okres inwestowania w miesiącach? "))
wartosc_pozadana=float(input("Jaka jest pożądana końcowa wartość inwestycji? "))

wartosc=float(kapital+(wplywy*okres))
profit=float(0.02 * wartosc)

wartosc_calkowita=float(wartosc+profit)

print("Końcowa wartość inwestycji to " + str(wartosc_calkowita))
if(wartosc_calkowita<wartosc_pozadana):
    print("Końcowa wartość inwestycji jest mniejsza niż pożądana wartość")
elif(wartosc_calkowita==wartosc_pozadana):
    print("Końcowa wartość inwestycji jest równa wartości pożądanej")
else:
    print("Końcowa wartość inwestycji jest większa niż wartość pożądana")

