import pandas as pd

# Datei einlesen (Pfad ggf. anpassen)
file_path = "human_labelled_with_ati.csv"
df = pd.read_csv(file_path, encoding="utf-8", low_memory=False)

# Hier die Namen der relevanten Text-Spalten eintragen
text_columns = ["Geld - 10. Begründen Sie ihre Entscheidungen. (optional)", 
                "Sport - 10. Begründen Sie ihre Entscheidungen. (optional)", 
                "Gesundheit - 10. Begründen Sie ihre Entscheidungen. (optional)", 
                "Wissen - 10. Begründen Sie ihre Entscheidungen. (optional)", 
                "Haben Sie Vorschläge, wie man die Texte & deren Glaubwürdigkeit verbessern könnte?"]  

# Sicherstellen, dass alle angegebenen Spalten existieren
text_columns = [col for col in text_columns if col in df.columns]

# Nur die gewünschten Spalten auswählen
text_data = df[text_columns]

# Alle Zeilen mit fehlenden Werten entfernen
text_data = text_data.dropna(how="all")

# Ausgabe nach Spalten gruppiert
for col in text_columns:
    print(f"\n🟢 {col}:\n" + "=" * 50)
    spalten_werte = text_data[col].dropna().tolist()  # Leere Werte entfernen
    for antwort in spalten_werte:
        print(f"\n{antwort}")
    print("\n" + "-" * 80)  # Trennlinie zwischen Spalten
