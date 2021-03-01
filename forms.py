from flask_wtf import FlaskForm
from wtforms import TextField, BooleanField, TextAreaField, SubmitField, IntegerField, SelectField, SelectMultipleField, widgets, validators
from wtforms.validators import InputRequired

# This Multicheckbox field was borrowed from https://gist.github.com/llloo/d4b12ca9e98723e5f523573058a8c0c6
class MultiCheckboxField(SelectMultipleField):
    widget = widgets.ListWidget(prefix_label=False)
    option_widget = widgets.CheckboxInput()

class searchForm(FlaskForm):
	gpu = TextField("Graphics Card")
	chipset = MultiCheckboxField(u'Chipset',choices = [('Nvidia', 'Nvidia'), ('AMD', 'AMD')], validators=[InputRequired()], default=['Nvidia'])
	brand = MultiCheckboxField(u'Brand', choices = [('AMD', 'AMD'), ('ASUS', 'ASUS'), ('EVGA', 'EVGA'), ('Gigabyte', 'Gigabyte'), ('MSI', 'MSI'), ('NVIDIA', 'NVIDIA'), ('Power VR', 'Power VR'), ('Sapphire', 'Sapphire'), ('Via', 'Via'), ('Zotac', 'Zotac') ], validators=[InputRequired()], default=['ASUS'])
	maxPrice = IntegerField("Maximum Price")
	submit = SubmitField("Submit")

class ContactForm(FlaskForm):
    name = TextField("Name")
    email = TextField("Email")
    subject = TextField("Subject")
    message = TextAreaField("Message")
    submit = SubmitField("Send")

class gpuForm(FlaskForm):
	memoryType = TextField("Memory Type")
	numberOfCudaCores = IntegerField("Number Of Cuda Cores")
	chipsetId = IntegerField("Chipset Id Number")
	averagePrice = IntegerField("Average Price")
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
