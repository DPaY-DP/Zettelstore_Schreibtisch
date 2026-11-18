VERFUEGBARE_KLASSEN = ["Projekt", "Aufgabe", "Notiz", "System"]
_zettel_zuordnungen = {}

def klasse_zuordnen(zettel_id, klassenname):
    if not zettel_id or klassenname not in VERFUEGBARE_KLASSEN:
        return False
    _zettel_zuordnungen[zettel_id] = klassenname
    return True

def klasse_entfernen(zettel_id):
    if zettel_id in _zettel_zuordnungen:
        del _zettel_zuordnungen[zettel_id]
        return True
    return False

def klassen_anwenden(zettel_liste):
    for zettel in zettel_liste:
        z_id = zettel.get("id", "")
        if z_id in _zettel_zuordnungen:
            zettel["klasse"] = _zettel_zuordnungen[z_id]
        elif z_id.startswith("0000"):
            zettel["klasse"] = "System"
        else: zettel["klasse"] = None
    return zettel_liste

