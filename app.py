from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return "Seja bem-vindo ao mundo Python/Flask e outros bichos!" 

@app.route('/pessoas')
def pessoas():
    return render_template('pessoas.html',**locals())

@app.route('/pessoa/<id>')
def pessoa(id):
    return render_template('pessoas.html',**locals())

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)