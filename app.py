from flask import Flask,render_template, request
app=Flask(__name__)

@app.route('/')
def index():
	fruits=["a,b,c,d"]
	return render_template('index.html',fruits=fruits)
@app.route('/ind')
def ind():
	
	return render_template('home.html')

@app.route('/der')
def dere():
	return "heyy"
@app.route('/login',methods=["post","get"])
def login():
	error=None
	if request.method=='POST':
		if request.form['email']!='sanchita.nandi13@gmail.com' or request.form['password']!='dash':
			error='email or password does not match'
		else:
			return render_template('home.html')
		return render_template('login.html',error=error)
	return render_template('login.html')

if __name__=='__main__':
	app.jinja_env.globals.update(chr=chr)
	app.run(host="localhost",port=8000,debug=True,threaded=True)

