import os 

ZETTELSTORE_URL = os.environ.get("ZETTELSTORE", "http://127.0.0.1:23123")

PORT = int(os.environ.get("SCHREIBTISCH_PORT", "5000"))