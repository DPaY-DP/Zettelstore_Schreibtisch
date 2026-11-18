import requests
import config

platzhalter = "(ohne Titel)"
max_titellaenge = 256

class ZettelstoreFehler(Exception):
     pass 

def alle_zettel_laden():
        
        try:
            antwort = requests.get(f"{config.ZETTELSTORE_URL}/z", timeout=5)
            antwort.raise_for_status()
        except requests.RequestException as fehler:
            raise ZettelstoreFehler(str(fehler)) from fehler

        zettel = []
        for zeile in antwort.text.splitlines():
            if len(zeile) < 14:
                continue
            zettel.append({"id": zeile[:14], "titel": zeile[15:]})
        titel_bereinigen(zettel)
        return zettel

def titel_bereinigen(zettel):
    for eintrag in zettel:
        titel = eintrag["titel"].strip()
        titel = " ".join(titel.split())
        if len(titel) == 0:
            titel = platzhalter
        elif len(titel) > max_titellaenge:
            titel = titel[:max_titellaenge - 3] + "..."
        eintrag["titel"] = titel
    return zettel