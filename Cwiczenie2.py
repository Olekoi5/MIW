import math as mt

def lista(a_lista, b_lista):
    lista = [a_lista[i] for i in range(len(a_lista)) if i%2==0]
    lista = lista + [b_lista[i] for i in range(len(b_lista)) if i%2!=0]
    return lista

print(lista([4,5,6,7,2,3], [5,78,45,3,9]))


def dict(data_text):
    dict = {"lenght":len(data_text), "letters":data_text.count("g"), "big_letters":data_text.upper(), "small_letters":data_text.lower()}
    return dict

word = "AsdRtGfdYUIe GjRyTcbghU ggguty"
properties = dict(word);
print("lenght: " + str(properties["lenght"]))
print("letters: " + str(properties["letters"]))
print("big_letters: " + properties["big_letters"])
print("small_letters: " + properties["small_letters"])


def exchange(temperature_type):
    print("Temperatura w stopniach Celsjusza: " + str(temperature_type) + "°C")
    K = temperature_type + 273,15
    if temperature_type >= -273.15:
        print("W stopniach Kelwina: " + K + "°K")
    else:
        print("W stopniach Kelwina: " + str(0) + "°K")
    F = 9/5*temperature_type + 32
    print("W stopniach Fahrenheita: " + str(F) + "°F")

exchange(-280)


class Calculator:
    def __init__(self, liczba_1, liczba_2):
        self.liczba_1 = liczba_1
        self.liczba_2 = liczba_2
    def Add(self):
        return self.liczba_1 + self.liczba_2
    def Difference(self):
        return self.liczba_1 - self.liczba_2
    def Multiply(self):
        return self.liczba_1 * self.liczba_2
    def Divide(self):
        return self.liczba_1 / self.liczba_2

calcu = Calculator(20,2)
print("dodawanie: " + str(calcu.Add()))
print("odejmowanie: " + str(calcu.Difference()))
print("dzielenie: " + str(calcu.Divide()))
print("mnożenie: " + str(calcu.Multiply()))

class ScienceCalculator(Calculator):
    def __init__(self, liczba_1, liczba_2):
        return super().__init__(liczba_1, liczba_2)
    def power(self):
        return self.liczba_1**self.liczba_2
    def sqrt(self):
        return mt.sqrt(self.liczba_1)

calcu2 = ScienceCalculator(6,2)
print("dodawanie: " + str(calcu2.Add()))
print("potęgowanie: " + str(calcu2.power()))
print("pierwiastek: " + str(calcu2.sqrt()))


def odTylu(text):
    return text[::-1]

word = "Aleksander"
print(odTylu(word))





