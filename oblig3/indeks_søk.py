from ferdig_indeks import last_in_indeks


def finn_unike_ord_i_streng(streng):
    """
    Lag en mengde med alle ordene som dukker opp i strengen.
    
    Pass på at strengen kun inneholder små bokstaver (hvis store bokstaver
    er med i strengen skal de bli gjort om til små bokstaver). Mellomrom
    på slutten og starten av linjer skal også fjernes.
    
    De følgende spesialtegn må og fjernes:
    ``[',', '.', '"', '\'', ':', ';', '(', ')', '-', '?', '!']``
    
    Arguments
    ---------
    streng : str
        Strengen vi vil finne unike tegn i.
    
    Returns
    -------
    ord_i_streng : Set[str]
        Mengden med unike ord i strengen.
    
    Notes
    -----
    Se forelesningvideoen for 13. mars og 19. mars.

    Vi kan splitte opp strenger med ``split`` funksjonen.

    >>> tekst = 'abc 123'
    >>> print(tekst.split(' '))
    ['abc', '123']

    Examples
    --------
    >>> streng = "Nå arbeider vi med INF120. Faktisk arbeider vi med siste oblig i INF120!"
    >>> finn_unike_ord_i_streng(streng)
    {'nå', 'arbeider', 'vi', 'med', 'inf120', 'faktisk', 'siste', 'oblig', 'i'}
    
    Merk at rekkefølgen på ordene ikke spiller noen rolle!
    """
    unike_ord = None  # Slett denne linja
    # Skriv kode her

    return unike_ord

def fjern_spesialtegn(streng):
    r"""
    Fjern de følgende spesialtegnene fra input strengen:
        ``[',', '.', '"', '\'', ':', ';', '(', ')', '-', '?', '!']``
    
    Arguments
    ---------
    streng : str
        Input strengen som spesialtegn skal fjernes fra
    
    Returns
    -------
    ren_streng : str
        Strengen etter at spesialtegn er fjernet.
    
    Notes
    -----
    Se forelesningen den 20. mars.

    Vi kan bruke ``replace`` funksjonen for å bytte substrenger med
    andre strenger. 

    >>> streng = "abc123abc"
    >>> streng.replace('a', 'e')
    ebc123ebc

    Examples
    --------
    >>> streng = "abc1, hei på deg. Hva heter du?"
    >>> fjern_spesialtegn(streng)
    "abc1 hei på deg Hva heter du"

    >>> streng = "  Hei på deg!!!\n"
    >>> fjern_spesialtegn(streng)
    "Hei på deg"
    """
    # Skriv kode her

    return streng


def finn_felles_ellement_i_flere_mengder(liste_av_mengder):
    """
    Lag en funksjon som finner felles element i en samling av mengder (set).
    
    Arguments
    ---------
    liste_av_mengder : List[Set]
        En liste hvor hvert element er en mengde (set på engelsk).
    
    Returns
    -------
    snitt_av_mengder : Set[str]
        En mengde som kun inneholder de elementene som er del av ALLE
        mengdene i ``liste_av_mengder``.
    
    Notes
    -----
    Vi kan finne snittet mellom to mengder med ``intersection`` funksjonen.

    >>> mengde1 = {1, 2, 3}
    >>> mengde2 = {2, 3, 4}
    >>> mengde1.intersection(mengde2)
    {2, 3}
    
    Om vi tar snittet mellom en mengde og seg selv så endres ingen ting.

    >>> mengde1 = {1, 2, 3}
    >>> mengde1 = mengde1.intersection(mengde1)
    >>> print(mengde1)
    {1, 2, 3}

    Examples
    -------
    >>> mengde1 = {1, 2, 3}
    >>> mengde2 = {2, 3, 4}
    >>> liste_av_mengder = [mengde1, mengde2]
    >>> finn_felles_element_i_flere_mengder(liste_av_mengder)
    {2, 3}
    >>> mengde3 = {3, 4, 5}
    >>> liste_av_mengder = [mengde1, mengde2, mengde3]
    >>> finn_felles_element_i_flere_mengder(liste_av_mengder)
    {3}
    """
    felles_element = None  # Slett denne linja
    # Skriv kode her
        
    return felles_element


def søk_i_indeks_med_mengde(indeks, mengde_av_søkeord):
    """
    Finn alle dokument som inneholder alle søkeordene i ``mengde_av_søkeord``.

    Denne funksjonen skal ta to argument som input, en søkeindeks og 
    en mengde med søkeord.

    Søkeindeksen er en dictionary med engelske ord som nøkler og mengden med alle
    dokument som inneholder det ordet som verdi.

    Mengden med søkeord er en mengde (set på Engelsk) som beskriver hva
    som søkes etter.

    Det som returneres er mengden med dokument som inneholder ALLE søkeordene.

    Arguments
    ---------
    indeks : dict[str] -> Set[str]
        Søkeindeksen.
    mengde_av_søkeord : Set[str]
        Mengden med søkeord.

    Returns
    -------
    relevante_bøker : Set[str]
        Mengden med bøker som inneholder alle ordene i ``mengde_av_søkeord``.

    Notes
    -----
    Husk ``finn_felles_ellement_i_flere_mengder`` funksjonen din.

    Vi kan lage en tom mengde med ``set`` funksjonen.

    >>> tom_mengde = set()
    >>> print(tom_mengde)
    {}

    Examples
    --------
    >>> søk_i_indeks_med_streng(indeks, {"sherlock", "holmes", "scarlet")
    {'Chronicles_of_Martin_Hewitt.bok', 'The_Hound_of_the_Baskervilles.bok'}
    >>> søk_i_indeks_med_streng(indeks, {"Dette", "er", "ikke", "i", "indeksen"})
    {}
    """
    mulige_bøker = None  # Slett denne linja
    # Skriv kode her

    return mulige_bøker


def klargjør_søkestreng(søkestreng):
    r"""
    Ta inn en søkestreng og klargjør den for å søke i en søkeindeks.

    Strengen skal behandles på samme måte som vi behandler nye strenger
    som skal indekseres. Store bokstaver skal gjøres om til små,
    spesialtegn skal fjernes og "whitespace" tegn på starten og slutten
    av strengen skal fjernes. Til slutt skal strengen splittes ved 
    alle mellomrom og duplikatord skal fjernes.

    Arguments
    ---------
    søkestreng : str
        Strengen vi vil finne unike tegn i.
    
    Returns
    -------
    ord_i_streng : Set[str]
        Mengden med unike ord i strengen.
    
    Notes
    -----
    Kan du gjenbruke en funksjon du lagde tidligere i obligen?

    Examples
    --------
    >>> streng = "abc1, hei på deg. Hva heter du?"
    >>> fjern_spesialtegn(streng)
    "abc1 hei på deg Hva heter du"

    >>> streng = "  Hei på deg!!!\n"
    >>> fjern_spesialtegn(streng)
    "Hei på deg"
    """
    klargjort_streng = None  # Slett denne linja
    # Skriv kode her

    return klargjort_streng


def søk_i_indeks_med_streng(indeks, søkestreng):
    """
    Finn alle dokument som inneholder alle søkeordene i ``søkestreng``.

    Denne funksjonen skal ta to argument som input, en søkeindeks og 
    en mengde med søkeord.

    Søkeindeksen er en dictionary med engelske ord som nøkler og mengden med alle
    dokument som inneholder det ordet som verdi.

    Søkestrengen skal først klargjøres. Dette gjøres ved å gjøre strengen til
    små bokstaver og å fjerne spesialtegn. I tillegg skal og whitespace på 
    starten og slutten av strengen fjernes. Deretter skal hvert ord i 
    søkestrengen hentes ut. Disse ordene brukes når det skal søkes i
    de indekserte dokumentene.

    Det som returneres er mengden med dokument som inneholder ALLE søkeordene.

    Arguments
    ---------
    indeks : dict
        Søkeindeksen.
    mengde_av_søkeord : str
        Mengden med søkeord.

    Returns
    -------
    relevante_bøker : Set[str]
        Mengden med bøker som inneholder alle ordene i ``mengde_av_søkeord``.

    Notes
    -----
    Husk ``søk_i_indeks_med_mengde`` funksjonen din.

    Examples
    --------
    >>> søk_i_indeks_med_streng(indeks, "Sherlock Holmes, scarlet")
    {'Chronicles_of_Martin_Hewitt.bok', 'The_Hound_of_the_Baskervilles.bok'}
    >>> søk_i_indeks_med_streng(indeks, "Dette er ikke i indeksen")
    {}
    """
    mulige_bøker = None  # Slett denne linja
    # Skriv kode her

    return mulige_bøker


if __name__ == "__main__":
    søkestreng = "Sherlock Holmes, scarlet"
    indeks = last_in_indeks()

    print(søk_i_indeks_med_streng(indeks, søkestreng))