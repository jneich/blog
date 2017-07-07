from flask import render_template, flash, redirect
from app import app
from .forms import ContactMeForm

@app.route('/') 
@app.route('/index')
def index():
    return render_template('index.html', title='Home')

@app.route('/blog')
def blog():
	return render_template('blog.html', title='Blog')


@app.route('/contact', methods=['GET', 'POST'])
def contact():
	form = ContactMeForm()
	return render_template('contact_me.html',
							title='Contact Me',
							form=form)
