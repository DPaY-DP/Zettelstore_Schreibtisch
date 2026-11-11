import requests
import config


class ZettelstoreFehler(Exception):
    


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
        return zettel