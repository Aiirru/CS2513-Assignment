#Student Number: 125521049

def check_text(value, label):
    if not isinstance(value, str) or not value.strip():
        raise ValueError(f"{label}, must not be empty")
    return value.strip()

def check_number(value, label,low, high):
    if not isinstance(value, int) or not low <= value <= high:
        raise ValueError(f'{label} must be a whole number between {low} and {high}')
    return value



class Instruments:
    def __init__(self, name, family="Any"): 
        self._name = check_text(name, "Instrument Name")
        self._family = check_text(family, "Instrument Family")

    @property
    def name(self):
        return self._name 

    def description(self):
        return f"{self._name}, {self._family}"
    
class StringInstrument(Instruments):
    def __init__(self, name):
        super().__init__(name, "String")  


class KeyInstrument(Instruments):
    def __init__(self, name):
        super().__init__(name, "Keyboard")



class Mood:
    def __init__(self, name, energy, description="None"):
        self._name = check_text(name, "Mood Name")
        self._energy = check_number(energy, "Energy", 1, 10)
        self._description = check_text(description, "Mood description")


    @property
    def name(self):
        """name inputted through other file"""
        return self._name

    @property
    def energy(self):
        return self._energy

    @property
    def energy_setter(self, value):
        self._energy = check_number(value, "Energy", 1, 10)


    @property
    def description(self):
        return self._description

    def mood_descirption(self):
        return f"{self._name} , Energy Level:{self._energy}, {self.description}"


class Artist:
    def __init__(self, name):
        self._name = check_text(name, "Artist Name")
        self._genre = []
        self._instruments = []

    @property
    def name(self):
        return self._name

    

    @property
    def gernres(self):
        return list(self._genre)

    def add_genre(self, genre):
        self._genre.append(genre)

    @property
    def instruments(self):
        return list(self._instruments)
    
    def add_instrument(self, instrument):
        self._instruments.append(instrument)

    def describe(self):
        return f"{self._name} (solo artist)"

    

class Artist_Group(Artist):
    def __init__(self, name, members):
        super().__init__(name)
        if not members:
            raise ValueError("Group needs atleast 1 member.")

        self._members = [check_text(member, "Member Name") for member in members]

    def describe(self):
        return f"{self._name} (Group: {', '.join(self._members)})"



class Genre:
    def __init__(self, name):
        self._name = check_text(name, "Genre Name")
        self._artists = []
        self._moods = []

    @property
    def name(self):
        return self._name

    @property
    def artists(self):
        return list(self._artists)

    @property
    def moods(self):
        return list(self._moods)


    def add_artist(self, artist):
        if not isinstance(artist, Artist):
            raise TypeError("Only artists cna be added")
        self._artists.append(artist)

    def add_mood(self,mood):
        if not isinstance(mood,Mood):
            raise TypeError("Only moods can be added")
        self._moods.append(mood)



class GenreList:
    def __init__(self):
        self._genres = {}

    def add_genre(self, genre):
        if not isinstance(genre, Genre):
            raise TypeError("Only Genres can be added")
        if genre.name.lower() in self._genres:
            raise ValueError(f"{genre.name} is already in the catalogue.")
        self._genres[genre.name.lower()] = genre

    def get_genre(self, name):
        genre = self._genres.get(check_text(name, "Genre Name").lower())
        if genre is None:
            raise ValueError(f"No genre called '{name}'")
        return genre

    @property
    def genres(self):
        return list(self._genres.values())