def afficher_playlist():
    print("\n=== Musique Ivoirienne ===")
    playlist = [
        {"genre": "Zouglou", "artiste": "Magic System", "titre": "Premier Gaou"},
        {"genre": "Coupé-Décalé", "artiste": "DJ Arafat", "titre": "Dosabado"},
        {"genre": "Reggae", "artiste": "Alpha Blondy", "titre": "Jerusalem"},
        {"genre": "Mandingo", "artiste": "Tiken Jah Fakoly", "titre": "Plus rien ne m’étonne"},
        {"genre": "Rap Ivoire", "artiste": "Didi B", "titre": "Big Boss"}
    ]
    for m in playlist:
        print(f"🎶 {m['genre']} – {m['artiste']} : {m['titre']}")
