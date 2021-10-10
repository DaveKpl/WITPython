Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
name, age=input("Jak masz na imię? "),input( "Ile masz lat? ")
Jak masz na imię? David
Ile masz lat? 29
type(age)
<class 'str'>
age=int(age)
age
29
type(age)
<class 'int'>
print("Twoje imię to {} i masz {} lat". format(name,str(age)))
Twoje imię to David i masz 29 lat
