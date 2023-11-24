from flask import Flask, Response

app = Flask(__name__)
@app.route('/summa/<int:luku1>/<int:luku2>')
def summa(luku1, luku2):
    vastaus = {
        'luku1' : luku1,
        'luku2' : luku2,
        'summa' : luku1 + luku2
    }

    return vastaus

if __name__ == '__main__':
    app.run(use_reloader=True, host='localhost', port=3000)