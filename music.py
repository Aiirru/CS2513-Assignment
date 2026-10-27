#Student Number: 125521049

from main import (Instruments, StringInstrument, KeyInstrument, Mood, Artist, Artist_Group,
                  Genre, GenreList)


#Instruments
guitar = StringInstrument("Guitar")
bass = StringInstrument("Bass")
piano  = KeyInstrument("Piano")
drums = Instruments("Drums")
saxophone = Instruments("Saxophone")
trumpet = Instruments("Trumpet")

#Artists
miles_davis = Artist("Miles Davis")
for i in(trumpet,saxophone,piano):
    miles_davis.add_instrument(i)

john_coltrane = Artist("John Coltrane")
john_coltrane.add_instrument(saxophone)

dangelo = Artist("D'Angelo")
for i in (guitar,bass,drums,saxophone,trumpet):
    dangelo.add_instrument(i)

stevie_wonder = Artist("Stevie Wonder")
for i in (piano, bass, drums, guitar):
    stevie_wonder.add_instrument(i)

minnie_riperton = Artist("Minnie Riperton")
for i in (piano,guitar,bass,drums,saxophone):
    minnie_riperton.add_instrument(i)

TCQ = Artist_Group("A Tribe Called Quest", ["Q-Tip", "Ali Shaheed Muhammad", "Jarobi White", "Phife Dawg"])
for i in (drums, bass, piano, guitar, saxophone, trumpet):
    TCQ.add_instrument(i)

radiohead = Artist_Group("Radiohead", ["Thom Yorke", "Jonny Greenwood", "Colin Greenwood", "Philip Selway", "Ed O'Brien"])
for i in (guitar, bass, piano, drums):
    radiohead.add_instrument(i)

thundercat = Artist("Thundercat")
thundercat.add_instrument(bass)


#Genre
jazz = Genre("Jazz")
for artist in (miles_davis, john_coltrane, dangelo, stevie_wonder, minnie_riperton, TCQ, thundercat):
    jazz.add_artist(artist)
jazz.add_mood(Mood("Peaceful", 3))
jazz.add_mood(Mood("Upbeat", 7))
jazz.add_mood(Mood("Frantic", 9))

rock = Genre("Rock")
rock.add_artist(radiohead)
rock.add_mood(Mood("Energetic", 8))
rock.add_mood(Mood("Mellow", 5))

soul = Genre("Soul")
for artist in (dangelo, stevie_wonder, minnie_riperton, thundercat):
    soul.add_artist(artist)
soul.add_mood(Mood("Soulful", 6))
soul.add_mood(Mood("Mellow", 5))
soul.add_mood(Mood("Funky", 8))

hip_hop = Genre("Hip-Hop")
hip_hop.add_artist(TCQ)
hip_hop.add_mood(Mood("Energetic", 9))
hip_hop.add_mood(Mood("Soulful", 6))
hip_hop.add_mood(Mood("Jazzy", 6))
hip_hop.add_mood(Mood("Intense", 9 ))

#Genre List
glist = GenreList()
glist.add_genre(jazz)
glist.add_genre(rock)
glist.add_genre(soul)
glist.add_genre(hip_hop)

for genre in glist.genres:
    print(f"Genre: {genre.name}")
    for artist in genre.artists:
        print(artist.describe())
    print("Moods:", ", ".join(f"{i.name} ({i.energy}/10)" for i in genre.moods))




#some tests
if __name__ == "__main__":
    try:
        if Instruments("Drums").description() == "Drums, Any":
            print("Pass: Instrument")
    except Exception as e:
        print("Fail", e)

    try:
        if StringInstrument("Guitar").description() == "Guitar, String":
            print("Pass: StringInstrument")
    except Exception as e:
        print("Fail", e)

    try:
        mood = Mood("Upbeat", 7)
        mood.energy = 7
        if mood.energy == 7:
            print("Pass: energy setter")
    except Exception as e:
        print("Fail", e)

    try:
        if Artist("Thundercat").describe() == "Thundercat (solo artist)":
            print("Pass: Artist describe")
    except Exception as e:
        print("Fail", e)

    try:
        group = Artist_Group("Radiohead", ["Thom Yorke", "Jonny Greenwood"])
        if group.describe() == "Radiohead (Group: Thom Yorke, Jonny Greenwood)":
            print("Pass: Artist_Group")
    except Exception as e:
        print("Fail", e)

    try:
        Mood("Bad", 11)
        print("Fail")
    except ValueError:
        print("Pass: energy 11 rejected")

    try:
        Instruments("")
        print("Fail")
    except ValueError:
        print("Pass: blankrejected")