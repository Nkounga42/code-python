import os

def analyser_multimedia(chemin):
    fichiers_audio = {'.mp3', '.wav', '.aac', '.flac', '.ogg'}
    fichiers_video = {'.mp4', '.avi', '.mkv', '.mov', '.wmv', '.webm'}
    fichiers_image = {'.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.webp'}

    total_fichiers = 0
    total_taille_mo = 0
    details_fichiers = []

    print(f"Analyse multimédia (hors images) dans : {chemin}\n")

    for racine, dossiers, fichiers in os.walk(chemin):
        for nom_fichier in fichiers:
            extension = os.path.splitext(nom_fichier)[1].lower()
            if (extension in fichiers_audio or extension in fichiers_video) and extension not in fichiers_image:
                chemin_complet = os.path.join(racine, nom_fichier)
                taille = os.path.getsize(chemin_complet)
                taille_mo = taille / (1024 * 1024)
                total_fichiers += 1
                total_taille_mo += taille_mo
                details_fichiers.append((chemin_complet, taille_mo))

    for fichier, taille_mo in details_fichiers:
        print(f"{fichier} ({taille_mo:.2f} Mo)")

    print("\nRésumé :")
    print(f"Nombre total de fichiers multimédia (hors images) : {total_fichiers}")
    print(f"Taille totale : {total_taille_mo:.2f} Mo")


# Exemple d'utilisation
chemin_du_dossier = "C:\/Users\DELL\Music"  # Remplace par le chemin voulu
analyser_multimedia(chemin_du_dossier)
