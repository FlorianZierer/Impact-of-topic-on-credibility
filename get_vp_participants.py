import csv

# Funktion zum Extrahieren der Namen und Matrikelnummern aus einer CSV-Datei
def extract_names_and_ids(file_path):
    names_and_ids = []
    with open(file_path, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file, delimiter=';' if 'human_labelled' in file_path else ',')
        for row in reader:
            name = row.get('Geben Sie Ihren Vor- & Nachnamen an. (nur nötig für VP Stunden)', '').strip()
            matrikelnummer = row.get('Geben Sie Ihre Matrikelnummer an (nur nötig für VP Stunden)', '').strip()
            if name and matrikelnummer:
                # Entferne das Komma und konvertiere die Matrikelnummer in einen Integer, um das ".0" zu entfernen
                matrikelnummer = matrikelnummer.replace(',', '')
                matrikelnummer = str(int(float(matrikelnummer)))  # Konvertiere zuerst zu float, dann zu int, dann zu string
                names_and_ids.append((name, matrikelnummer))
    return names_and_ids

# Pfade zu den CSV-Dateien
ai_labelled_file = 'ai_labelled.csv'
human_labelled_file = 'human_labelled.csv'

# Namen und Matrikelnummern aus beiden Dateien extrahieren
ai_names_and_ids = extract_names_and_ids(ai_labelled_file)
human_names_and_ids = extract_names_and_ids(human_labelled_file)

# Kombiniere die Listen und entferne Duplikate
all_names_and_ids = list(set(ai_names_and_ids + human_names_and_ids))

# Neue CSV-Datei schreiben
output_file = 'teilnehmer.csv'
with open(output_file, mode='w', encoding='utf-8', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Name', 'Matrikelnummer'])  # Header schreiben
    writer.writerows(all_names_and_ids)

print(f"Die Namen und Matrikelnummern wurden erfolgreich in '{output_file}' gespeichert.")