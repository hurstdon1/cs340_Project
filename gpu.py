from flask import Flask, render_template, url_for
from forms import ContactForm, gpuForm, brandForm, chipsetForm
from flask import request
from flask_wtf import FlaskForm
from wtforms import TextField, BooleanField, TextAreaField, SubmitField

# class ContactForm(FlaskForm):
#     name = TextField("Name")
#     email = TextField("Email")
#     subject = TextField("Subject")
#     message = TextAreaField("Message")
#     submit = SubmitField("Send")

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

@app.route("/add")
def add():
	return render_template('add.html', title='Add')

@app.route("/add_gpu", methods=["GET","POST"])
def add_gpu():

	form = gpuForm()

	if request.method == 'POST':
		priceId = request.form["priceIdNumber"]
		memoryType = request.form["memoryType"]
		numberOfCudaCores = request.form["numberOfCudaCores"]
		chipsetId = request.form["chipsetId"]
		res = pd.DataFrame({'priceID':priceID,'memoryType':memoryType, 'numberOfCudaCores':numberOfCudaCores, 'chipsetId':chipsetId}, index=[0])
		res.to_csv('./add_gpu.csv')
		print("The data are saved")

	else:
		return render_template("add_gpu.html", form=form, title="Add a gpu")

@app.route("/add_brand", methods=["GET","POST"])
def add_brand():

	form = brandForm()

	if request.method == 'POST':
		brandName = request.form["brandName"]
		productSeries = request.form["productSeries"]
		model = request.form["model"]
		res = pd.DataFrame({'brandName':brandName, 'productSeries':productSeries, 'model':model}, index=[0])
		res.to_csv('./add_brand.csv')
		print("The data are saved")

	else:
		return render_template("add_brand.html", form=form, title="Add a brand")

@app.route("/add_chipset", methods=["GET","POST"])
def add_chipset():

	form = chipsetForm()

	if request.method == 'POST':
		chipsetManufacturer = request.form["chipsetManufacturer"]
		graphicsCoprocessor = request.form["graphicsCoprocessor"]
		res = pd.DataFrame({'chipsetManufacturer':chipsetManufacturer, 'graphicsCoprocessor':graphicsCoprocessor}, index=[0])
		res.to_csv('./add_chipset.csv')
		print("The data are saved")

	else:
		return render_template("add_chipset.html", form=form, title="Add a chipset")

@app.route("/add_pricing", methods=["GET","POST"])
def add_pricing():
	return render_template("add_pricing.html", title="Add Pricing")

@app.route("/add_benchmarks", methods=["GET","POST"])
def add_benchmarks():
	return render_template("add_benchmarks.html", title="Add Benchmarks")

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