from flask import Flask, render_template, request, redirect, session
import random
app = Flask(__name__)
app.secret_key = 'i wish i had a witty pun about numbers for this key'

@app.route('/', methods=['GET'])
def index():
    if 'secret_number' not in session:
        session['secret_number'] = random.randint(1,100)
    ## print(session['secret_number'])
    return render_template('index.html')

@app.route('/play', methods=['POST'])
def play():
    session['user_guess'] = int(request.form['user_guess'])
    return redirect('/')


@app.route('/reset')
def reset():
    session.clear()
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)
