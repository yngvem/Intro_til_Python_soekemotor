from pathlib import Path
import re


def klargjør_linje(linje):
    # Bruk regulære uttrykk for å fjerne uønskede karakterer
    unicode_accent_letters = '\u00c0-\u00d6\u00d8-\u00f6\u00f8-\u02af\u1d00-\u1d25\u1d62-\u1d65\u1d6b-\u1d77\u1d79-\u1d9a\u1e00-\u1eff\u2090-\u2094\u2184-\u2184\u2488-\u2490\u271d-\u271d\u2c60-\u2c7c\u2c7e-\u2c7f\ua722-\ua76f\ua771-\ua787\ua78b-\ua78c\ua7fb-\ua7ff\ufb00-\ufb06'
    return re.sub(f'[^a-zA-Z0-9.,."\':;()-?! \n{unicode_accent_letters}]', '', linje)


def klargjør_bokfil(bokfil):
    parse = False
    linjer = []

    for linje in bokfil.readlines():
        if linje.startswith("Title: "):
            title = linje[7:]
            linjer.append(title)
        elif linje.startswith("*** START OF THIS PROJECT GUTENBERG EBOOK"):
            parse=True
            continue
        
        if parse is not True:
            continue
        
        linje = klargjør_linje(linje)
        linjer.append(linje)

        if linje.startswith("*** END OF THIS PROJECT GUTENBERG EBOOK"):
            return linjer


def klargjør_tittel(tittel):
    tittel = tittel.replace(" ", "_")
    tittel = tittel.replace(",", "")
    tittel = tittel.replace("'", "")
    tittel = tittel.strip()

    return tittel


def preprosesser_bøker_i_mappe(mappe):
    mappe = Path(mappe)
    preprossesert_mappe = mappe/".."
    if not preprossesert_mappe.is_dir():
        preprossesert_mappe.mkdir()
    
    for bokfil in mappe.glob("*.txt"):
        with bokfil.open(encoding="utf8") as bokfil:
            output_bok = klargjør_bokfil(bokfil)
        tittel = klargjør_tittel(output_bok[0])

        preprossesert_bok = preprossesert_mappe/f"{tittel}.bok"
        with preprossesert_bok.open("w") as nybok:
            nybok.writelines(output_bok)


def preprosesser_bøker_i_undermapper(mappe):
    mappe = Path(mappe)
    for undermappe in mappe.iterdir():
        if undermappe.is_dir():
            preprosesser_bøker_i_mappe(undermappe)


if __name__ == "__main__":
    preprosesser_bøker_i_undermapper("bøker")