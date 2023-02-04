from checker import handleInputInteger
from logicNiederlassung import getNiederlassung
from logicMitarbeiter import getMitarbeiter
from logicAuftrag import buchenErledigung, getAuftrag, anlegenAuftrag, getAuftragErsatzteile, planenAuftrag
from logicErsatzteilliste import anzeigeErsatzteilliste

# Aufruf der Ablauflogik
while True:
    print('')
    print('1 - Daten anzeigen')
    print('2 - Neuen Auftrag anlegen')
    print('3 - Auftrag planen')
    print('4 - Ersatzteilliste anzeigen')
    print('5 - Erledigung buchen')

    wastun = handleInputInteger('Aktion wählen')
    print()
    
    if wastun == 1:
        nlnr = getNiederlassung()            # Niederlassung aus Niederlassungsliste auswählen
        while nlnr > 0:
            print()
            mitnr = getMitarbeiter(nlnr)     # Mitarbeiter aus Mitarbeiterliste auswählen
            while mitnr > 0:
                print()
                getAuftrag(mitnr)            # Aufträge des Mitarbeiters anzeigen
                eingabe_aufnr = handleInputInteger('Ort eingeben (Nr)')
                while eingabe_aufnr > 0:
                    print()
                    getAuftragErsatzteile(eingabe_aufnr)
                    eingabe_aufnr = 0
                mitnr = getMitarbeiter(nlnr) # neuen Mitarbeiter aus Mitarbeiterliste auswählen
            nlnr = getNiederlassung()        # neue Niederlassung aus Niederlassungsliste auswählen

    elif wastun == 2:
        print('Daten einfügen')
        anlegenAuftrag()
        
    elif wastun == 3:
        print('Auftrag planen')
        planenAuftrag()

    elif wastun == 4:
        print('Ersatzteilliste anzeigen')
        anzeigeErsatzteilliste()

    elif wastun == 5:
        print('Erledigung buchen')
        buchenErledigung()
    
    else:
        break

