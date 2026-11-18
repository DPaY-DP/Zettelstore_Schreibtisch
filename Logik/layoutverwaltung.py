from Daten import zettelstore_adapter
import config

DatenquelleFehler = zettelstore_adapter.ZettelstoreFehler

SPALTEN = 5
ABSTAND_X = 220
ABSTAND_Y = 120


def zettel_fuer_schreibtisch():
    """Liefert alle Zettel mit Position: {"id", "titel", "x", "y"}."""
    zettel = zettelstore_adapter.alle_zettel_laden()
    zettel.sort(key=lambda z: z["id"])

    for nummer, z in enumerate(zettel):
        z["x"] = (nummer % SPALTEN) * ABSTAND_X
        z["y"] = (nummer // SPALTEN) * ABSTAND_Y
        z["link"] = link_alte_ansicht(z["id"])        
    return zettel

def link_alte_ansicht(zettel_id=None):
    """Liefert den Link zur alten Ansicht, optional direkt zu einem Zettel."""
    adresse = config.ZETTELSTORE_URL
    if zettel_id is None: 
        return adresse 
    else: 
        return f"{adresse}/h/{zettel_id}"
    
def anzahl_zettel_ermitteln(zettel):
    return len(zettel)
