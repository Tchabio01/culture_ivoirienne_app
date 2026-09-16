from modules import traditions, gastronomie, musique, evenements, quiz
from utils import security

def afficher_menu():
    print("\n=== Application Culture Ivoirienne ===")
    print("1. Traditions")
    print("2. Gastronomie")
    print("3. Musique")
    print("4. Événements")
    print("5. Quiz éducatif")
    print("6. Sécurité (test mot de passe)")
    print("0. Quitter")

def main():
    while True:
        afficher_menu()
        choix = input("Choisissez une option: ")

        if choix == "1":
            traditions.afficher_traditions()
        elif choix == "2":
            gastronomie.afficher_recettes()
        elif choix == "3":
            musique.afficher_playlist()
        elif choix == "4":
            evenements.afficher_evenements()
        elif choix == "5":
            quiz.lancer_quiz()
        elif choix == "6":
            mot_de_passe = input("Entrez un mot de passe: ")
            hashed = security.hash_password(mot_de_passe)
            print("Mot de passe haché:", hashed)
            print("Vérification:", security.check_password(mot_de_passe, hashed))
        elif choix == "0":
            print("Au revoir !")
            break
        else:
            print("❌ Option invalide, réessayez.")

if __name__ == "__main__":
    main()
