from abc import ABC, abstractmethod
from datetime import date, datetime

class Szoba(ABC):
    def __init__(self, ar, szobaszam):
        self.ar = ar
        self.szobaszam = szobaszam

    @abstractmethod
    def get_info(self):
        pass

class EgyagyasSzoba(Szoba):
    def __init__(self, szobaszam):
        super().__init__(ar=15000, szobaszam=szobaszam)
        self.tipus = "Egyágyas"

    def get_info(self):
        return f"Szoba szám: {self.szobaszam}, Típus: {self.tipus}, Ár: {self.ar} Ft"

class KetagyasSzoba(Szoba):
    def __init__(self, szobaszam):
        super().__init__(ar=25000, szobaszam=szobaszam)
        self.tipus = "Kétágyas"

    def get_info(self):
        return f"Szoba szám: {self.szobaszam}, Típus: {self.tipus}, Ár: {self.ar} Ft"

class Szalloda:
    def __init__(self, nev, cim, szobak):
        self.nev = nev
        self.cim = cim
        self.szobak = szobak
        self.foglalasok = []

    def szalloda_info(self):
        info = f"Szálloda neve: {self.nev}\nCíme: {self.cim}\nSzobák:\n"
        for szoba in self.szobak:
            info += szoba.get_info() + "\n"
        return info

    def foglalas_hozzaadasa(self, foglalas):
        self.foglalasok.append(foglalas)

    def foglalasok(self):
        foglalasok_info = [foglalas.get_info() for foglalas in self.foglalasok]
        info = "Foglalások:\n" + "\n".join(foglalasok_info)
        return info

    def foglalasok_listazas(self):
        if not self.foglalasok:
            return "Nincsenek foglalások."
        info = "Foglalások listája:\n"
        for foglalas in self.foglalasok:
            info += foglalas.get_info() + "\n"
        return info

    def szoba_foglalas(self, nev, szoba_szam, datum):
        if datum <= date.today():
            return f"A dátum érvénytelen. Kérjük, válasszon egy jövőbeni dátumot."

        for foglalas in self.foglalasok:
            if foglalas.szoba.szobaszam == szoba_szam and foglalas.datum == datum:
                return f"A {szoba_szam} számú szoba már foglalt a {datum} dátumra."
        
        for szoba in self.szobak:
            if szoba.szobaszam == szoba_szam:
                uj_foglalas = Foglalas(nev, szoba, datum)
                self.foglalas_hozzaadasa(uj_foglalas)
                return f"A {szoba_szam} számú szoba foglalása sikeres. Ár: {szoba.ar} Ft."

        return f"A {szoba_szam} számú szoba nem található."

    def szoba_lemondas(self, szoba_szam, datum):
        for foglalas in self.foglalasok:
            if foglalas.szoba.szobaszam == szoba_szam and foglalas.datum == datum:
                self.foglalasok.remove(foglalas)
                return f"A {szoba_szam} számú szoba foglalása lemondva a {datum} dátumra."
        return f"A {szoba_szam} számú szoba nem volt foglalva a {datum} dátumra."

class Foglalas:
    def __init__(self, nev, szoba, datum):
        self.nev = nev
        self.szoba = szoba
        self.datum = datum

    def get_info(self):
        return f"Név: {self.nev}, Szoba szám: {self.szoba.szobaszam}, Dátum: {self.datum}"

def main():
    egyAgyasSzobak = [EgyagyasSzoba(101), EgyagyasSzoba(102)]
    ketAgyasSzobak = [KetagyasSzoba(206)]

    szobak = egyAgyasSzobak + ketAgyasSzobak

    szalloda = Szalloda("Hotel Tlanna", "3071 Őrmező utca 12.", szobak)

    while True:
        print("\nVálasszon egy műveletet:")
        print("1. Szoba foglalása")
        print("2. Szoba lemondása")
        print("3. Foglalások listázása")
        print("4. Szálloda információk megtekintése")
        print("5. Kilépés")

        valasztas = input("Adja meg a választott művelet számát: ")

        if valasztas == "1":
            nev = input("Adja meg a nevét: ")
            szoba_szam = int(input("Adja meg a szoba számát: "))
            datum_str = input("Adja meg a dátumot (ÉÉÉÉ-HH-NN formátumban): ")
            datum = datetime.strptime(datum_str, "%Y-%m-%d").date()
            eredmeny = szalloda.szoba_foglalas(nev, szoba_szam, datum)
            print(eredmeny)

        elif valasztas == "2":
            szoba_szam = int(input("Adja meg a szoba számát: "))
            datum_str = input("Adja meg a dátumot (ÉÉÉÉ-HH-NN formátumban): ")
            datum = datetime.strptime(datum_str, "%Y-%m-%d").date()
            eredmeny = szalloda.szoba_lemondas(szoba_szam, datum)
            print(eredmeny)

        elif valasztas == "3":
            print(szalloda.listaz_foglalasok())

        elif valasztas == "4":
            print(szalloda.get_szalloda_info())

        elif valasztas == "5":
            print("Kilépés...")
            break

        else:
            print("Érvénytelen választás, próbálja újra.")

if __name__ == "__main__":
    main()
