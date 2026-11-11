import config 
from Darstellung import schreibtisch_ui 

if __name__ == "__main__":
    schreibtisch_ui.app.run(port=config.PORT, debug=True)