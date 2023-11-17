from flask import Flask

app = Flask(__name__)
@app.route('/alkuluku/<int:luku>')
def alkuluku(luku):

    on_alkuluku = True

    if luku == 1:
        on_alkuluku = False

    else:
        for i in range(2, luku):
            if luku % i == 0:
                on_alkuluku = False
                break
            else:
                on_alkuluku = True

    vastaus = {
        "Number" : luku,
        "isPrime" : on_alkuluku
    }

    return vastaus

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)

