import sys 

print( "Tere! Olen sinu uus sõber - Python!")
nimi = str(input("Mis on sinu nimi?"))
print (nimi,", oi kui ilus nimi!")

jahei = int(input(f" {nimi}! Kas leian Sinu keha indeksi?  0-ei, 1-jah =>"))

if jahei == 1:
    print("Väga hea! Lähme edasi küsimusele!")
    pikkus = (input("Mis on sinu pikkus?"))
    if pikkus.isalpha() == True:
        print("ValueError")
    else:
        mass = (input("Mis on sinu mass?"))
        if mass.isalpha() == True:
            print("ValueError")
        else:
            pikkus = float(pikkus)
            mass = float(mass)
            indeks = round(mass/(0.01*pikkus)**2, 1)

if jahei == 0:
    print("Kahju! See on väga kasulik info!")
    