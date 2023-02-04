from dbConnect import sessionLoader
from mapper import Ersatzteil
from checker import handleInputInteger, handleInputDatum
import datetime
from sqlalchemy import exc, or_


def anzeigeErsatzteilliste():
    session = sessionLoader()
    ersatzteile = session.query(Ersatzteil).all()  # Alle Ersatzteile abrufen

    if len(ersatzteile) > 0:  # Überprüfung, ob Ersatzteile in der Datenbank vorliegen
        print('(ID | Bezeichnung | Preis | Anzahl | Hersteller):')
        for et in ersatzteile:
            # Ausgabe der Ersatzteil-Daten
            print(f'{et.EtID} - {et.Bezeichnung} {et.Preis} {et.Anzahl} {et.Hersteller}')
    else:
        print('Es sind keine Ersatzteile in der Datenbank enthalten.')
    session.close()