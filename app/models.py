from app import db

class Post(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	datetime = db.Column(db.TIMESTAMP)
	title = db.Column(db.String(120), index=True)
	content= db.Column(db.Text)

	def __repr__(self):
		return '<Post %r>' % (self.id)