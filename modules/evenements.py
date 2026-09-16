def afficher_evenements():
    print("\n=== Événements Culturels en Côte d’Ivoire ===")
    evenements = [
        {"nom": "Festival des Masques", "lieu": "Man", "periode": "Décembre"},
        {"nom": "FEMUA (Festival des Musiques Urbaines d’Anoumabo)", "lieu": "Abidjan", "periode": "Avril"},
        {"nom": "Popo Carnaval", "lieu": "Bonoua", "periode": "Mars"},
        {"nom": "Festival du Fromager", "lieu": "Abengourou", "periode": "Août"},
        {"nom": "Festival des Arts et de la Culture Baoulé", "lieu": "Bouaké", "periode": "Septembre"}
    ]
    for e in evenements:
        print(f"- {e['nom']} ({e['lieu']}, {e['periode']})")
