from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "<h1>Bravo ! Exercice DevOps reussi !</h1><p>Le conteneur Docker tourne via GitHub Actions et est expose par Ngrok.</p>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
