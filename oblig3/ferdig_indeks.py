from pathlib import Path
import pickle

def last_in_indeks(indeksfil=None):
    if indeksfil is None:
        indeksfil = Path(__file__).parent/"indeks.p"
    
    indeksfil = Path(indeksfil)
    with indeksfil.open('rb') as indeks_fil:
        return pickle.load(indeks_fil)