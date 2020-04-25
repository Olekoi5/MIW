Tekst = "Lorem Ipsum jest tekstem stosowanym jako przykładowy wypełniacz w przemyśle poligraficznym. Został po raz pierwszy użyty w XV w. przez nieznanego drukarza do wypełnienia tekstem próbnej książki. Pięć wieków później zaczął być używany przemyśle elektronicznym, pozostając praktycznie niezmienionym. Spopularyzował się w latach 60. XX w. wraz z publikacją arkuszy Letrasetu, zawierających fragmenty Lorem Ipsum, a ostatnio z zawierającym różne wersje Lorem Ipsum oprogramowaniem przeznaczonym do realizacji druków na komputerach osobistych, jak Aldus PageMaker"
imie = "Aleksander";
nazwisko = "Kościjańczuk";

litera_1 = nazwisko[3]
litera_2 = imie[2]

ileLiter_1 = Tekst.count(litera_1)
ileLiter_2 = Tekst.count(litera_2)

print("W tekście litera " + litera_1 + " występuje " + str(ileLiter_1) + " razy, a litera " + litera_2 + " występuje " + str(ileLiter_2) + " razy");

print(dir(imie))
help(imie.isalnum)

print(imie[::-1].capitalize() + " " + nazwisko[::-1].capitalize())

lista = [1,2,3,4,5,6,7,8,9,10];
lista_1 = lista[0:5];
lista_2 = lista[5:10];
print(lista)
print(lista_1)
print(lista_2)

wynik = lista_2 + lista_1
wynik = wynik + [0]
wynik.sort(reverse=True)
print(wynik)

listaStudentow = []
krotka1 = (45321,"Jan","Kowalski")
krotka2 = (45567,"Adam","Nowak")
krotka3 = (45786,"Paweł","Nowakowski")
listaStudentow.append(krotka1)
listaStudentow.append(krotka2)
listaStudentow.append(krotka3)
print(listaStudentow)

slownik = {45321:("Jan","Kowalski"), 45567:("Adam","Nowak"), 45786:("Paweł","Nowakowski")}
print(slownik[45567])
slownik[45362] = ("Filip","Walerianski",18,"jjfhd@jdhfn.com",1998,"Owocowa 3 13-100 Nidzica")
print(slownik.values())

for i in range(1,11,1):
    print(i)

for i in range(100,15,-5):
    print(i)

