#Student Number: 125521049

"""Project based on genres, their moods, common instruments and artists"""



def check_text(value, label):
    """Validating that the string isnt blank and strips it
    Arguments: 
        value: value being checked
        label: name of the label, used for error message

    Returns: 
        validated string with any blank space removed

    Exceptions:
        raises ValueError if value isnt a string or is empty
    """
    if not isinstance(value, str) or not value.strip():
        raise ValueError(f"{label}, must not be empty")
    return value.strip()

def check_number(value, label,low, high):
    """Validating that the value is an int in its range (range used to cap energy from 1-10)
    Arguments:
        value: value/int being checked
        label: name of the label, used for error message
        low: sets the smallest int value allowed
        high: sets the highest int value allowed
    
    Returns:
        validated int within range 
    
    Exceptions:
        raises ValueError if value is not an int thats between the range limits
    """
    if not isinstance(value, int) or not low <= value <= high:
        raise ValueError(f'{label} must be a whole number between {low} and {high}')
    return value



class Instruments:
    """Class representing instruments. Takes in instruments and is used for general instruments (e.g drums). Assigns to a family
    
        Used as parent/base class for StringInstruments and KeyboardInstruments"""

    def __init__(self, name, family="Any"): 
        """Arguments:
                name: name of the instrument
                family: set to any as used for general instruments
            
            Exceptions:
                raises ValueError through check_text if value isnt a string or is blank"""
        self._name = check_text(name, "Instrument Name")
        self._family = check_text(family, "Instrument Family")

    @property
    def name(self):
        """returns instrument name"""
        return self._name 

    def description(self):
        """returns instrument in form of name then family"""
        return f"{self._name}, {self._family}"
    
class StringInstrument(Instruments):
    """Instrument that has and primarily uses strings. Inherits Instrument class"""

    def __init__(self, name):
        """ Arguments:
                name: instrument name
                
            Exceptions:
                raises ValueError if name is not a string or is blank"""
        super().__init__(name, "String")  


class KeyInstrument(Instruments):
    """Instrument that uses keys (e.g piano, organ). Inherits Instrument class"""
    def __init__(self, name):
        """Arguments
                name: name of instrument
                
            Exceptions:
                raises ValueError if name is not a string or is blank"""
        super().__init__(name, "Keyboard")



class Mood:
    """Mood of a genre with an energy level"""

    def __init__(self, name, energy, description="None"):
        """Arguments:
                name: Mood name
                energy: Energy level between 1-10
                description: Set to none so it can be blank and read in if wanted. Short description of the mood
            
            Exceptions:
                raises ValueError for if name/description isnt a string or is blank
                raises ValueError if energy is not an int or not between 1-10
                """
        self._name = check_text(name, "Mood Name")
        self._energy = check_number(energy, "Energy", 1, 10)
        self._description = check_text(description, "Mood description")


    @property
    def name(self):
        """name inputted through other file"""
        """ returns name of mood """
        return self._name

    @property
    def energy(self):
        """returns int between 1-10 showing energy level"""
        return self._energy

    @energy.setter #    @property   def energy_setter(self, value) wasnt working so has to work around using this 
    def energy(self, value):
        """function to set energy level, must be between 1-10"""
        self._energy = check_number(value, "Energy", 1, 10)


    @property
    def description(self):
        """reads mood description"""
        return self._description

    def mood_description(self):
        """returns description of the mood"""
        return f"{self._name} , Energy Level:{self._energy}, {self.description}"


class Artist:
    """Solo artist (not a group) who plays instrument(s) and plays genres """

    def __init__(self, name):
        """Arguments:
                name: artist name
            
            Exceptions:
                raises ValueError if name is not a string or is blank"""
        
        self._name = check_text(name, "Artist Name")
        self._genre = []
        self._instruments = []

    @property
    def name(self):
        """Artist name"""
        return self._name

    @property
    def genres(self):
        """returns a list of genres an artist uses"""
        return list(self._genre)

    def add_genre(self, genre):
        """adds genres to artists list of genres
        
        Argument:
            genre: the genre being added"""
        
        self._genre.append(genre)

    @property
    def instruments(self):
        """list of instruments an artist plays"""
        return list(self._instruments)
    
    def add_instrument(self, instrument):
        """adds instruments to artists list of instruments
        
        Argument:
            instrument: instrument being added"""
        self._instruments.append(instrument)

    def describe(self):
        """returns artists name and describing as a solo artist"""
        return f"{self._name} (solo artist)"

    

class Artist_Group(Artist):
    """Group of artists forming band or group. Made of different members. Inherits Artist class"""
    def __init__(self, name, members):
        """Arguments:
                name: Group name
                members: Names of members in group
                
            Exceptions:
                raises Value error if group name or member name is blank
                raises ValueError if members is member list is blank
                raises ValueError if anything isnt a string"""
        
        super().__init__(name)
        if not members:
            raise ValueError("Group needs atleast 1 member.")

        """validates each member and returns them stripped of any spaces etc"""
        self._members = [check_text(member, "Member Name") for member in members]

    def describe(self):
        """Description of group. Group's name then its members
        
            inherits from Artist and overrides to work for group"""
        return f"{self._name} (Group: {', '.join(self._members)})"



class Genre:
    """Music genre, contains artists that play it and common moods"""
    def __init__(self, name):
        """Arguments:
                name: Genre name
                
            Exceptions:
                raises ValueError if name isnt a string or is blank"""
        self._name = check_text(name, "Genre Name")
        self._artists = []
        self._moods = []

    @property
    def name(self):
        """name of genre"""
        return self._name

    @property
    def artists(self):
        """list of artists in genre"""
        return list(self._artists)

    @property
    def moods(self):
        """list of common moods"""
        return list(self._moods)


    def add_artist(self, artist):
        """adds artist to list
        
        Argument:
            artist: artist or group being added
            
        Exceptions:
            raises TypeError if whats being added isnt an artist"""
        
        if not isinstance(artist, Artist):
            raise TypeError("Only artists cna be added")
        self._artists.append(artist)

    def add_mood(self,mood):
        """Adds a mood to genre
        
        Arguments:
            mood: Mood being added

        Exceptions:
            raises TypeError if whats being added isnt a mood"""
        if not isinstance(mood,Mood):
            raise TypeError("Only moods can be added")
        self._moods.append(mood)



class GenreList:
    """List of genres by name"""

    def __init__(self):
        self._genres = {}

    def add_genre(self, genre):
        """adds genre to list
        
        Arguments:
            genre: genre being added
            
        Exceptions:
            raises TypeError if genre isnt a genre
            raises ValueError if genre is already in list """
        if not isinstance(genre, Genre):
            raise TypeError("Only Genres can be added")
        if genre.name.lower() in self._genres:
            raise ValueError(f"{genre.name} is already in the catalogue.")
        self._genres[genre.name.lower()] = genre

    def get_genre(self, name):
        """Returns the genre of given name
        
        Arguments:
            name: Name of genre being found
            
        Returns:
            the genre searched for
            
        Exceptions:
            raises ValueError if no genre with name found or is blank"""
        genre = self._genres.get(check_text(name, "Genre Name").lower())
        if genre is None:
            raise ValueError(f"No genre called '{name}'")
        return genre

    @property
    def genres(self):
        """list of genres in list"""
        return list(self._genres.values())


