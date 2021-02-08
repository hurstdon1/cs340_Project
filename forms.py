from flask_wtf import FlaskForm
from wtforms import TextField, BooleanField, TextAreaField, SubmitField, IntegerField

class ContactForm(FlaskForm):
    name = TextField("Name")
    email = TextField("Email")
    subject = TextField("Subject")
    message = TextAreaField("Message")
    submit = SubmitField("Send")

class gpuForm(FlaskForm):
	priceId = IntegerField("Price Id Number")
	memoryType = TextField("Memory Type")
	numberOfCudaCores = IntegerField("Number Of Cuda Cores")
	chipsetId = IntegerField("Chipset Id Number")
	submit = SubmitField("Submit")


class brandForm(FlaskForm):
	brandName = TextField("Brand Name")
	productSeries = TextField("Product Series")
	model = TextField("Model Name")
	submit = SubmitField("Submit")

class chipsetForm(FlaskForm):
	chipsetManufacturer=TextField("Chipset Manufacturer")
	graphicsCoprocessor = TextField("Graphics Coprocessor")
	submit = SubmitField("Submit")

class pricingForm(FlaskForm):
	averagePrice = IntegerField("Average Price")
	submit = SubmitField("Submit")

class benchmarkForm(FlaskForm):
	unigine = IntegerField("Unigine score")
	passmark = IntegerField("Passmark score")
	shadow = IntegerField("Shadow of the Tomb Raider FPS")
	gta = IntegerField("GTA 5 FPS")
	submit = SubmitField("Submit")

class gpuBenchmarkForm(FlaskForm):
	gpuIdNumber = IntegerField("GPU ID Number")
	benchmarkIdNumber = IntegerField("Bechmark ID Number")
	submit = SubmitField("Submit")

class gpuBrandForm(FlaskForm):
	gpuIdNumber = IntegerField("GPU ID Number")
	brandIdNumber = IntegerField("Brand ID Number")
	submit = SubmitField("Submit")
