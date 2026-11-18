import config 
import requests
import urllib.request 
from Darstellung import schreibtisch_ui 

PORT = 23125

if __name__ == "__main__":
    # with urllib.request.urlopen("http://localhost:23123") as f:
    #     enc = f.headers.get("Content-Encoding")
    #     data = f.read()
    #     print(data.decode("utf-8"))
    schreibtisch_ui.app.run(port=PORT, debug=True)
