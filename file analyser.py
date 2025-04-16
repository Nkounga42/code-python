import os

def analyser_dossier(chemin):
    total_fichiers = 0
    total_taille = 0
    fichiers_par_extension = {}

    print(f"Analyse du dossier : {chemin}\n")

    for racine, dossiers, fichiers in os.walk(chemin):
        print(f"Dossier : {racine}")
        for nom_fichier in fichiers:
            chemin_complet = os.path.join(racine, nom_fichier)
            taille = os.path.getsize(chemin_complet)
            total_fichiers += 1
            total_taille += taille

            # Extension du fichier
            extension = os.path.splitext(nom_fichier)[1].lower()
            fichiers_par_extension[extension] = fichiers_par_extension.get(extension, 0) + 1

            print(f"  Fichier : {nom_fichier} ({taille} octets)")

    print("\nRésumé :")
    print(f"Nombre total de fichiers : {total_fichiers}")
    print(f"Taille totale : {total_taille} octets")
    print("Fichiers par extension :")
    for ext, count in fichiers_par_extension.items():
        print(f"  {ext or 'Sans extension'} : {count}")

# Exemple d'utilisation :
chemin_du_dossier = "D:\C++ Code"  # à adapter
analyser_dossier(chemin_du_dossier)
