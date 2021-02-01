from flask import Flask, render_template, url_for
from forms import ContactForm
from flask import request
from flask_wtf import FlaskForm
from wtforms import TextField, BooleanField, TextAreaField, SubmitField

class ContactForm(FlaskForm):
    name = TextField("Name")
    email = TextField("Email")
    subject = TextField("Subject")
    message = TextAreaField("Message")
    submit = SubmitField("Send")

app = Flask(__name__)

app.config['SECRET_KEY'] = 'f5a6c63d94bf77cb2c4845153a56cbba'

@app.route("/")
@app.route("/home")
def hello():
    return render_template('home.html')

@app.route("/about")
def about():
	return render_template('about.html', title='About')

@app.route("/comparisons")
def comparisons():
	return render_template('comparisons.html', title='Comparisons')

@app.route("/contact", methods=["GET","POST"])
def contact():
	form = ContactForm()

	if request.method == 'POST':
		name =  request.form["name"]
		email = request.form["email"]
		subject = request.form["subject"]
		message = request.form["message"]
		res = pd.DataFrame({'name':name, 'email':email, 'subject':subject ,'message':message}, index=[0])
		res.to_csv('./contactusMessage.csv')
		print("The data are saved !")
	else:
		return render_template('contact.html', form=form)

if __name__ == '__main__':
	app.run(debug=True)