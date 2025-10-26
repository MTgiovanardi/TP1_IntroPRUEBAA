from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "Hola, Flask está funcionando!"

@app.route("/saludo")
def saludo():
    return "Hola desde el backend!"

@app.route("/usuarios")
def usuarios():
    data = [
        {"id": 1, "nombre": "Máximo"},
        {"id": 2, "nombre": "Sofía"}
    ]
    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True)
