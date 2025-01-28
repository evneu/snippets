# Literaturliste ist im Format Kurztitel - Zeilenumbruch - Komplettangabe
dateiname = "bibl.txt"
# Name der Ausgabedatei
ausgabedatei = "bibl-bereinigt.txt"

# Datei wird gelesen
def extrahiere_titel(dateiname):
    with open(dateiname, "r", encoding="utf-8") as datei:
        inhalt = datei.readlines()
    
    full_citations = []
    for i in range(1, len(inhalt), 2):  # Beginne mit der zweiten Zeile
        full_citations.append(inhalt[i].strip())
    
    return full_citations

# Volle Zitation wird extrahiert
full_citations = extrahiere_titel(dateiname)

# Exportieren der Titel
with open(ausgabedatei, "w", encoding="utf-8") as datei:
    for titel in full_citations:
        datei.write(titel + "\n\n")  # Zwei Zeilenumbrüche zwischen den Titeln

print(f"Die vollständigen Titel wurden als '{ausgabedatei}' exportiert.")
