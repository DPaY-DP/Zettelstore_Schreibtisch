from Daten import zettelstore_adapter

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
    return zettel