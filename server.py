from flask import Flask, render_template, request ,redirect, session
import random 	

app = Flask(__name__)
app.secret_key = 'clavesecreta' # asignar una clave secreta por motivos de seguridad



@app.route('/')
def begin_game():
    if 'guess' not in session:  
        numero =  random.randint(1, 100) 
        print(f"-------------{numero} --------------")
        session['guess'] = numero
        session['display'] = "none"
        return render_template("index.html", high_HTML = "none", low_HTML = "none", correct_HTML = "none", block_HTML = "yes")

    if session['display'] == "none":
        return render_template("index.html", high_HTML = "none", low_HTML = "none", correct_HTML = "none" , block_HTML = "yes")

    if session['display'] == "high":
        return render_template("index.html", high_HTML = "yes", low_HTML = "none", correct_HTML = "none")

    if session['display'] == "low":
        return render_template("index.html", high_HTML = "none", low_HTML = "yes", correct_HTML = "none")

    if session['display'] == "correct":
        return render_template("index.html", high_HTML = "none", low_HTML = "none", correct_HTML = "yes", block_HTML = "none")

    print(session)
    return render_template("index.html")


@app.route('/guess', methods= ['POST'])
def verify():
    if int(session['guess']) == int(request.form["number_guess"]):
       print("adivinó!!")
       session['display'] = "correct"
       return redirect('/win')

    elif int(session['guess']) < int(request.form["number_guess"]):
        session['display'] = "high"
        print("Muy Alto!!")

    elif int(session['guess']) > int(request.form["number_guess"]):
        session['display'] = "low"
        print("Muy Bajo!!")
 
    return redirect('/')

@app.route('/win')
def win():
    
    return render_template("index.html", high_HTML = "none", low_HTML = "none", correct_HTML = "yes", block_HTML = "none")




@app.route('/reset')
def reset_game():
    session.clear()
    return redirect('/')







if __name__ == "__main__":
    app.run(debug=True)