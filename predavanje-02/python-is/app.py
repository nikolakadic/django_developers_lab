'''
Ovaj program nam napravi IS biblioteke. Pokaze nam koje knjige imamo, 
gdje se nalaze cijena knjige itd.
Takodje nam pokaze informacije u raznim policama gdje se nalaze knjige.
Imamo i podatke ko su radnici koji rade tu.
Sve to na kraju stavlja u txt fajl "knjige.txt" kao json.


Sto se tice unos podataka moze da se napravi input gdje korisnik moze
da sam kreira knjige, police i radnike. 
Za to bi nam trebao prvo da ga pitamo koliko knjige planira da kreira, 
koliko polica i koliko radnika. 
I posle toga ide for petla koja sve dok koris
'''

LISTA_KNJIGA = []

class Knjiga:
    
    def __init__(self, id, ime, autor, godina, strana, cijena, lokacija_knjige):
        self.id = id
        self.ime = ime
        self.autor = autor
        self.godina = godina
        self.strana = strana
        self.cijena = cijena
        self.lokacija_knjige = lokacija_knjige

        dict_1 = {
            'ID': self.id,
            'ime': self.ime,
            'autor': self.autor,
            'godina': self.godina,
            'strana': self.strana,
            'cijena': self.cijena,
            'lokacija_knjige': self.lokacija_knjige
        }
        LISTA_KNJIGA.append(dict_1)

    
    def __repr__(self):
        return f'Ime knjige je {self.ime}. Cijena je {self.cijena}$. Lokacija knjige je {self.lokacija_knjige}.'
        

        

LISTA_POLICA = []

class Polica:
    
    def __init__(self, id, kapacitet, spratnost, knjige_unutra, lokacija_police):
        self.id = id
        self.kapacitet = kapacitet
        self.spratnost = spratnost
        self.knjige_unutra = knjige_unutra
        self.lokacija_police = lokacija_police

        dict2 ={
            'ID': self.id,
            'kapacitet': self.kapacitet,
            'spratnost': self.spratnost,
            'knjiga_unutra': self.knjige_unutra,
            'lokacija_police': self.lokacija_police,   
            'slobodno_mjesta': self.kapacitet-self.knjige_unutra
        }
        LISTA_POLICA.append(dict2)

    def __repr__(self):
        return f'ID police je {self.id}. Ima jos {self.kapacitet - self.knjige_unutra} slobodnih mjesta. Lokacija police je {self.lokacija_police}.'


LISTA_RADNIKA = []

class Radnik:
    
    def __init__(self, id, ime, godina, smjena, plata, sati_rada):
        self.id = id
        self.ime = ime
        self.godina = godina
        self.smjena = smjena
        self.plata = plata
        self.sati_rada = sati_rada

        dict2 ={
            'ID': self.id,
            'ime': self.ime,
            'godina': self.godina,
            'smjena': self.smjena,
            'plata': self.plata,   
            'sati_rada': self.sati_rada
        }
        LISTA_RADNIKA.append(dict2)
    
    def set_ime(self,ime):
        """
        Setter metod postavlja vrijednost atributa uz prethodnu obradu/provjeru
        """
        if not ime.isalnum():
            print('Unijeli ste nevalidno ime')
            self.ime = 'Marko'
        else:
            self.ime = ime

    def __repr__(self):
        return f'Ime radnika/ce {self.ime}. Radi u {self.smjena} smijeni.'
   

knjiga1 = Knjiga(1,'Blerdijan', 'Kolic', 2020, 234, 1.20, 'A3')
knjiga2 = Knjiga(2,'Beni', 'Dob', 1999, 102, 9.90, 'B3')
knjiga3 = Knjiga(3,'Dovla', 'Bor', 2000, 34, 10.90, 'C4')


polica1= Polica(1,300,4,200, 'Desno')
polica2= Polica(2,200,1,200, 'Lijevo')

radnik1= Radnik(1,"Marko",1980,1,500,8)
radnik2= Radnik(2,"Igor",1950,2,700,10)
radnik2.set_ime('%%') 

print(radnik2.ime)


# f=open("knjige.txt",'a')
# f.write(str(LISTA_KNJIGA))
# f.write("\n")
# f.write(str(LISTA_POLICA))
# f.write("\n")
# f.write(str(LISTA_RADNIKA))
# f.close()
