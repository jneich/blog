from flask import render_template
from app import app

@app.route('/') 
def base():
	return render_template('base.html', title="Jonas' Blog")
@app.route('/index')
def index():
    return render_template('index.html', title='Home')



