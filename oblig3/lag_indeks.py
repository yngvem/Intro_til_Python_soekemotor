from pathlib import Path
import indeks_søk    # Kanskje du skal bruke noen av funksjonene du lagde her?


def finn_alle_unike_ord_i_liste_av_strenger(liste_av_strenger):
    """
    Lag en mengde med alle ordene som dukker opp i strengene i lista.
    
    Pass på at strengene kun inneholder små bokstaver (hvis store bokstaver
    er med i strengene skal de bli gjort om til små bokstaver). Mellomrom
    på slutten og starten av strengene skal også fjernes.
    
    De følgende spesialtegn må og fjernes:
    ``[',', '.', '"', '\'', ':', ';', '(', ')', '-', '?', '!']``
    
    Arguments
    ---------
    liste_av_strenger : str
        Strengene vi vil finne unike tegn i.
    
    Returns
    -------
    ord_i_streng : Set[str]
        Mengden med unike ord i alle strengene.
    
    Notes
    -----
    Vi kan oppdatere en tom mengde med ``set`` funksjonen og legge til
    mange element om gangen med ``update`` funksjonen.

    >>> mengde = set()
    >>> print(mengde)
    {}
    >>> mengde.update([1, 2, 'a'])
    >>> print(mengde)
    {1, 2, 'a'}
    >>> mengde.update([2, 'a', 'b', 1])
    >>> print(mengde)
    {'b', 1, 2, 'a'}

    Se forelesningvideoen for 13. mars og 19. mars.
    
    Husk ``finn_unike_ord_i_streng`` du lagde før denne!

    Examples
    --------
    >>> strenger = ["Nå arbeider vi med INF120.", "Faktisk arbeider vi med siste oblig i INF120!"]
    >>> finn_alle_unike_ord_i_liste_av_strenger(strenger)
    {'nå', 'arbeider', 'vi', 'med', 'inf120', 'faktisk', 'siste', 'oblig', 'i'}
    
    Merk at rekkefølgen på ordene ikke spiller noen rolle!
    """
    unike_ord = None  # Slett denne linja
    # Skriv kode her

    return unike_ord


def finn_unike_ord_i_bok(bokfil):
    """
    Lag en mengde med alle ordene som dukker opp i en bok.
    
    Pass på at strengen kun inneholder små bokstaver, og at mellomrom
    på slutten og starten av linjer er fjernet.
    
    De følgende spesialtegnene skal og fjernes:
    ``[',', '.', '"', '\'', ':', ';', '(', ')', '-', '?', '!']``
    
    Arguments
    ---------
    bokfil : str eller pathlib.Path
        Filen som inneholder boka.
    
    Returns
    -------
    ord_i_bok : Set[str]
        Mengden med unike ord i boka
    
    Notes
    -----
    Om du prøver å gjøre et Path objekt om til en Path så endrer du ingen ting.

    >>> fil = 'bøker/The_Works_of_Edgar_Allan_Poe.txt'
    >>> fil = Path(fil)
    >>> fil
    WindowsPath('bøker/The_Works_of_Edgar_Allan_Poe.txt')
    >>> fil = Path(fil)
    >>> fil
    WindowsPath('bøker/The_Works_of_Edgar_Allan_Poe.txt')

    MERK: Om du bruker Mac eller Linux vil det være en UnixPath istedenfor
    en WindowsPath.

    Husk: Du lagde en funksjon som finner unike ord i en liste av strenger!

    >>> indeks_søk.finn_unike_ord_i_streng("Hei, hei, på deg.")
    {'hei', 'på', 'deg'}
    """ 
    ord_i_bok = None  # Slett denne linja
    # Skriv kode her

    return ord_i_bok


def legg_til_bok_i_indeks(indeks, bokfil):
    """
    Denne funksjonen skal legge til en ny bok i indeksen.

    Måten denne nye boken skal legges til i indeksen er følgende
    
    1. Finn de unike ordene i boka.
    2. Iterer gjennom hvert unikt ord og sjekk om det er del av indeksen 
       allerede.

       * Hvis det er del av indeksen skal tittelen på denne bokfilen legges
         til i den korresponderende mengden med filnavn.
       * Hvis det ikke er del av søkeindeksen, så skal legges til som nøkkel
         i søkeindeksen, hvis korresponderende verdi skal være mengden som
         inneholder tittelen på denne bokfilen.

    Arguments
    ---------
    indeks : Dictionary[str] -> Set[str]
        En søkeindeks. Hver nøkkel er engelske ord som forekommer i minst
        en av bøkene som er indeksert. Nøkkelen "sherlock" peker på en
        mengde som inneholder filnavnet til alle bøker som inneholder
        ordet "sherlock".
    bokfil : Path or str
        Filplasseringen til bokfilen som skal legges til i søkeindeksen.
    
    Returns
    -------
    indeks : Dictionary[str] -> Set[str]
        En oppdatert søkeindeks. Hver nøkkel er engelske ord som forekommer i minst
        en av bøkene som er indeksert. Nøkkelen "sherlock" peker på en
        mengde som inneholder filnavnet til alle bøker som inneholder
        ordet "sherlock".
    
    Notes
    -----
    Vi kan legge til nye element i en mengde ved å bruke ``mengde.add`` 
    funksjonen.

    >>> mengde = set(['a', 'hei', 'hei', 'a'])
    >>> print(mengde)
    {'a', 'hei'}
    >>> mengde.add('b')
    >>> print(mengde)
    {'a', 'hei', 'b'}
    >>> mengde.add('a')
    {'a', 'hei', 'b'}

    Når du sjekker om et element er en del av en dictionary så sjekker du
    om det elementet er en nøkkel i den dictionaryen.

    >>> indeks = {'a': {'bok1.bok', 'bok2.bok'}, 'is': {'bok1.bok'}}
    >>> 'a' in indeks
    True
    >>> 'c' in indeks
    False

    Vi kan få filnavnet til en path ved å se på ``name`` attributten.

    >>> bokfil = Path('bøker/Benefactor.bok')
    >>> bokfil.name
    Benefactor.bok
    """
    # Skriv kode her

    return indeks


def indekser_bøker(mappe):
    r"""
    Lag en søkeindeks med alle filene i den spesifiserte mappen.

    Her skal du starte med å lage en tom søkeindeks, det vil si en tom 
    dictionary. Så skal du iterere gjennom hver bokfil i den spesifiserte
    mappen og legge alle til i indeksen.
    
    Arguments
    ---------
    mappe : Path or str
        Mappen vi skal søke etter filer i. Hvis denne er en streng skal den
        gjøres om til en Path.
    
    Returns
    -------
    indeks : Dictionary[str] -> Set[str]
        En søkeindeks over alle bokfiler i den spesifiserte mappen.
    
    Notes
    -----
    Se forelesningsvideoen den 27. mars.
    
    Om du prøver å gjøre et Path objekt om til en Path så endrer du ingen ting.

    >>> fil = 'bøker/The_Works_of_Edgar_Allan_Poe.bok'
    >>> fil = Path(fil)
    >>> fil
    WindowsPath('bøker/The_Works_of_Edgar_Allan_Poe.bok')
    >>> fil = Path(fil)
    >>> fil
    WindowsPath('bøker/The_Works_of_Edgar_Allan_Poe.bok')


    MERK: Om du bruker Mac eller Linux vil det være en UnixPath istedenfor
    en WindowsPath, men funksjonaliteten er den samme.

    Du kan iterere gjennom alle filer med en spesifikk filtype med ``Path.glob``
    funksjonen

    >>> mappe = Path('bøker')
    >>> for bokfil in mappe.glob('\*.bok'):
    ...     print(bokfil)
    bøker\A_Journey_to_the_Centre_of_the_Earth.bok
    bøker\Benefactor.bok
    ...
    bøker\Vulcans_Workshop.bok
    """
    indeks = None  # Slett denne linja
    # Skriv kode her

    return indeks


if __name__ == "__main__":
    indeks = indekser_bøker('bøker')
    print(indeks_søk.søk_i_indeks_med_streng(indeks, 'hound, sherlock'))
