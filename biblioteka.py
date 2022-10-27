import random
from datetime import date

today = date.today()
today = today.strftime("%d.%m.%Y")

class Movie:
    """filmy"""
    def __init__(self, tytul, rok_wydania, gatunek, liczba_odtworzen, content_typ):
        self.tytul = tytul
        self.rok_wydania = rok_wydania
        self.gatunek = gatunek
        self.liczba_odtworzen = liczba_odtworzen
        self.content_typ = content_typ

    def __str__(self):
        return f"{self.tytul} ({self.rok_wydania})"
    
    def play(self):
        """zwieksza liczbe odtworzen o 1"""
        self.liczba_odtworzen += 1
        return self.liczba_odtworzen
    

class Series:
    """seriale"""
    def __init__(self, tytul, rok_wydania, gatunek, nr_odcinka, nr_sezonu, liczba_odtworzen, content_typ):
        self.tytul = tytul
        self.rok_wydania = rok_wydania
        self.gatunek = gatunek
        self.nr_odcinka = nr_odcinka
        self.nr_sezonu = nr_sezonu
        self.liczba_odtworzen = liczba_odtworzen
        self.content_typ = content_typ

    def __str__(self):
        return f"{self.tytul} S{self.nr_sezonu:02d}E{self.nr_odcinka:02d}"

    def play(self):
        """zwieksza liczbe odtworzen o 1"""
        self.liczba_odtworzen += 1
        return self.liczba_odtworzen


def get_movies():
    """filtruje tylko filmy"""
    movies = []
    for movie in movies_and_series:
        if movie.typ == "film":
            movies.append(movie)

    for movie in movies:
        print(movie.tytul)


def get_series():
    """filtruje tylko seriale"""
    series = []
    for serial in movies_and_series:
        if serial.typ == "serial":
            series.append(serial)
    
    for serial in series:
        print(serial.tytul)


def search():
    """funkcja wyszukujaca filmy"""
    title_to_search = input("Podaj tytul filmu\serialu do znalezienia: ")
    title_to_search.lower()
    for i in movies_and_series:
        if i.tytul.lower() == title_to_search:
            print("Tytuł znajduje sie w bibliotece.")
            break
    else: 
        print("Nie ma takiego filmu\serialu")
 

def generate_views():
    """generuje losowo odtworzenia"""
    x = random.choice(movies_and_series)
    quantity = random.randint(1,1001)
    x.liczba_odtworzen += quantity


def repeat_generate_views():
    """funkcja ktora uruchamia funkcje generate_views 10x"""
    for i in range(10):
        generate_views()

    for i in movies_and_series:
        print(i.tytul + " - " + str(i.liczba_odtworzen) + " odtworzeń")


def top_titles():
    """wyświetla trzy najpopularniejsze tytuły"""
    by_popular = sorted(movies_and_series, key=lambda movie: movie.liczba_odtworzen, reverse=True)
    for i in by_popular[0:3]:
        print("-",i.tytul,"-",i.liczba_odtworzen,"odtworzeń")
    

def top_titles_by_type():
    """wyswietla trzy najpopularniejsze tytuly z podzialem na film lub serial"""               
    movies_and_series.sort(key=lambda movie: movie.liczba_odtworzen, reverse=True)
    typ = input("film czy serial?")
    most_popular = []
    for i in movies_and_series:
        if i.content_typ == typ:
            most_popular.append(i)
   
    for i in most_popular[0:3]:
        print(i.tytul,":",i.liczba_odtworzen,"liczba wyswietlen")

shawshank = Movie("The Shawshank Redemption", 1994, "dramat", 0, "film" )
nietykalni = Movie("Intouchables", 2011, "dramat", 10, "film")
wladca = Movie("The Lord Of The Rings: The Return Of The King", 2003, "fantasy", 53, "film")
siedem = Movie("Se7en", 1995, "kryminał", 4, "film")
czarnobyl = Series("Chernobyl", 2019, "dramat", 1, 1, 63, "serial")
got = Series("Game of Thrones", 2011, "fantasy", 5, 3, 22, "serial")
bb = Series("Breaking Bad", 2008, "kryminal", 1, 2, 11, "serial")
biuro = Series("The Office", 2005, "komedia", 5, 8, 121, "serial" )
lustro = Series("Black Mirror", 2011, "Sci-Fi", 6, 2, 22, "serial" )
lew = Movie("The Lion King", 1994, "familijny", 4, "film")


#lista filmow i seriali
movies_and_series = [shawshank, nietykalni, wladca, siedem, czarnobyl, got, bb, biuro, lustro, lew]


repeat_generate_views()
print()
print("-----Biblioteka filmów-----")
print()
print("W bibliotece znajdują sie następujące tytuły:")
for i in movies_and_series:
    print("-",i.tytul)
print()
print(f"Najpopularniejsze filmy i seriale dnia {today} to:")
top_titles()
