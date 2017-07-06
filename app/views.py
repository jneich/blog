from app import app

@app.route('/')
def 
@app.route('/index')
def index():
    return render_template('index.html', title='Home')

