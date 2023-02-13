"""
Esercizio

Realizzare un server web con flask che offra le seguenti funzionalità:

1. La home page deve fornire una breve descrizione delle caratteristiche della città di Milano

2. al link <nome sito>/immagini devono essere visualizzate le immagini di 4 monumenti di Milano (Controllare sul sito del prof come si fa a mettere le immagini)

3. Fare in modo che cliccando su un'immagine si venga mandati ad un breve testo descrittivo del documento (Controllare sempre sul sito del docente come si fa')

La repository che conterrà il sito si chiamerà "FlaskMilano"

"""

from flask import Flask, render_template
app = Flask(__name__)

@app.route('/', methods=['GET'])
def hello_world():
  return render_template("home.html")

@app.route('/it', methods=['GET'])
def ciao_mondo():
  return ('<h1>Ciao, mondo!</h1>')

@app.route('/immagini', methods=['GET'])
def benvenuto():
  return render_template('immagini.html')
if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)