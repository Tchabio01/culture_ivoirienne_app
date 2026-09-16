def afficher_traditions():
    print("\n=== Traditions Ivoiriennes ===")
    proverbes = [
        "Quand la chèvre est présente, on ne parle pas de corde.",
        "Le fleuve ne rejette pas la pluie.",
        "Celui qui veut tuer un oiseau ne regarde pas le ciel."
    ]
    contes = [
        "Le roi et le griot – symbole de sagesse et de transmission.",
        "L’histoire de la tortue et du léopard – le triomphe de l’intelligence sur la force.",
        "La légende de la reine Pokou – sacrifice et fondation du peuple Baoulé."
    ]
    print("📜 Proverbes :")
    for p in proverbes:
        print("-", p)
    print("\n📖 Contes :")
    for c in contes:
        print("-", c)
