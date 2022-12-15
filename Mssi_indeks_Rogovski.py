
print( "Tere! Olen sinu uus sõber - Python!")
nimi = str(input("Mis on sinu nimi?"))
if nimi.isalpha() == False:
    print("ValueError")
else:
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
                if pikkus<0.1:
                    print("ValueError")
                elif mass<0.1:
                    print("ValueError")
                elif mass>1000:
                    print("ValueError")
                elif pikkus>1000:
                    print("ValueError")
                else:
                    indeks = round(mass/(0.01*pikkus)**2, 1) 
                    print (f"{nimi}! Sinu keha indeks on: {indeks}")
                    if  indeks<16:
                        print ("Tervisele ohtlik alakaal")
                    elif indeks>16 and indeks<19:
                        print("Alakaal")
                    elif indeks>19 and indeks<25:
                        print("Normaalkaal")
                    elif indeks>25 and indeks<30:
                        print("Ülekaal")
                    elif indeks>30 and indeks<35:
                        print("Rasvumine")
                    elif indeks>35 and indeks<40:
                        print("Tugev rasvumine")
                    else:
                        print ("Sinu indeks on vali")
                tabel = int(input("Kas sa tahad vaata indeksi tabel? 0-ei, 1-jah =>"))
                if tabel == 1:
                    print("Tervisele ohtlik alakaal	      < 16\n Alakaal	                                16 - 19\n Normaalkaal	                        19 - 25\n Ülekaal	                                25 - 30\n Rasvumine	                        30 - 35\n Tugev rasvumine	                 35 - 40\n Tervisele ohtlik rasvumine      > 40")
    else:
                        print("kahju! see on väga kasulik info!\n")
print("Kohtumiseni, " + nimi + "! Igavesti Sinu, Python!")
    #if jahei == 0:
    #    print("kahju! see on väga kasulik info!")