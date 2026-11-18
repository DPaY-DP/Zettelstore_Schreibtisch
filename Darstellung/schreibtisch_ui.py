from flask import Flask, render_template

import config 
from Logik import layoutverwaltung 

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def startseite():
    try:
        zettel = layoutverwaltung.zettel_fuer_schreibtisch()
        fehler = None 
    except layoutverwaltung.DatenquelleFehler as e:
        zettel, fehler = [], str(e)

    return render_template(
        "index.html",
        zettel=zettel,
        fehler=fehler,
        #alte_ansicht_url=config.ZETTELSTORE_URL,
    )