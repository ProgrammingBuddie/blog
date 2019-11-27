from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'

db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)


    def __repr__(self):
        return '<User %r>' % self.username
	


@app.route('/')
@app.route('/hello')
def hello():
	return "Hello World"

@app.route('/html')
def hi():
	return render_template('file2.html',name= "Shankar Kumar",data = data)

if __name__ == "__main__":
	app.run(debug=True)
