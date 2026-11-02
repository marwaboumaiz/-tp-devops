from flask import Flask, jsonify, request
 
app = Flask(__name__)
taches = []
 
 
@app.get("/")
def accueil():
    return jsonify(message="API de gestion de tâches")
 
 
@app.get("/taches")
def lister_taches():
    return jsonify(taches)
 
 
@app.post("/taches")
def ajouter_tache():
    donnees = request.get_json()
    tache = {"id": len(taches) + 1, "titre": donnees["titre"]}
    taches.append(tache)
    return jsonify(tache), 201
 
 
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)