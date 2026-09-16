from flask import Flask, jsonify, request
from utils import database, security

app = Flask(__name__)
database.init_db()

@app.route("/proverbes", methods=["GET"])
def get_proverbes():
    data = database.lire_proverbes()
    return jsonify([{"id": p[0], "texte": p[1]} for p in data])

@app.route("/proverbes", methods=["POST"])
def add_proverbe():
    contenu = request.json
    texte = contenu.get("texte")
    if texte:
        database.inserer_proverbe(texte)
        return jsonify({"message": "Proverbe ajouté avec succès"}), 201
    return jsonify({"error": "Texte manquant"}), 400

@app.route("/auth", methods=["POST"])
def auth():
    contenu = request.json
    mot_de_passe = contenu.get("password")
    hashed = security.hash_password(mot_de_passe)
    token = security.generate_token(user_id=1, role="admin")
    return jsonify({"hashed": hashed, "token": token})

if __name__ == "__main__":
    app.run(debug=True)
