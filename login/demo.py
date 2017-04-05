from flask import Flask
from flask import Flask, flash, redirect, render_template, request, session, abort

app = Flask(__name__)
app.secret_key = "singhsecretkey"

@app.route('/')
def home():
    if not session.get('logged_in'):
        return render_template('login.html')
        #flash('singh')
    else:
    	return render_template('landing.html')
 
@app.route('/login', methods=['POST'])
def login():
    if request.form['password'] == 'password' and request.form['username'] == 'admin':
        session['logged_in'] = True
    else:
        flash('wrong password!')
    return home()

@app.route("/logout")
def logout():
    session['logged_in'] = False
    return home()

if __name__ == "__main__":
	app.run()

