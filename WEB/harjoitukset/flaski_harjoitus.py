from flask import Flask

app = Flask(__name__)
@app.route('/summa/<luku1>/<luku2>')
def kaiku(luku1, luku2):

    summa = int(luku1) + int(luku2)

    vastaus = {
        "luku1" : luku1,
        "luku2" : luku2,
        "summa" : summa
    }

    return vastaus

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)
