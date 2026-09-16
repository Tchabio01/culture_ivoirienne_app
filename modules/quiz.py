questions = [
    {"q": "Quelle est la capitale politique de la Côte d’Ivoire ?", "a": "Yamoussoukro"},
    {"q": "Quel est le plat populaire appelé 'Garba' ?", "a": "Attiéké avec thon frit"},
    {"q": "Qui est l’artiste ivoirien connu pour le titre 'Premier Gaou' ?", "a": "Magic System"},
    {"q": "Dans quelle ville se déroule le FEMUA ?", "a": "Abidjan"},
    {"q": "Quelle reine est associée au sacrifice fondateur du peuple Baoulé ?", "a": "Pokou"}
]

def lancer_quiz():
    print("\n=== Quiz Culture Ivoirienne ===")
    score = 0
    for q in questions:
        reponse = input(q["q"] + " : ")
        if reponse.lower().strip() == q["a"].lower().strip():
            print("✅ Correct !")
            score += 1
        else:
            print(f"❌ Faux. Réponse attendue: {q['a']}")
    print(f"\nScore final: {score}/{len(questions)}")
