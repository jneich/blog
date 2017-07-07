from flask import render_template, flash, redirect
from app import app, db
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
	if form.validate_on_submit():
		flash('Thanks for your comment, "%s". You wanted to let Jonas know "%s" ' % 
			(form.name.data, form.comment.data))

		return redirect('/index')
	return render_template('contact_me.html',
							title='Contact Me',
							form=form)
