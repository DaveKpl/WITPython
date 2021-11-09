def main():

    lista1=[1,2,3,4,5]
    lista2=[1,2,3,4,5]
    lista3=[1,2,2,3,3,4,5]
    set1=set(lista1)
    set2=set(lista2)
    set3=set(lista3)

    if set1==set2 and set2==set3:
        print("Wszystkie listy zawieraja te same elementy")
    elif set1==set2 and set1!=set3:
        print("Listy lista1 i lista2 zawieraja te same elementy")
    elif set2==set3 and set1!=set3:
        print("Listy lista2 i lista3 zawieraja te same elementy")
    elif set1==set3 and set1!=set2:
        print("Listy lista1 i lista3 zawieraja te same elementy")

    if len(lista1)>len(set1):
        print("Lista1 zawiera duplikaty")
    if len(lista2)>len(set2):
        print("Lista2 zawiera duplikaty")
    if len(lista3)>len(set3):
        print("Lista3 zawiera duplikaty")

main()
