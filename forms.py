from flask_wtf import FlaskForm
from wtforms import TextField, BooleanField, TextAreaField, SubmitField, IntegerField, SelectField, SelectMultipleField, widgets, validators
from wtforms.validators import InputRequired

# This Multicheckbox field was borrowed from https://gist.github.com/llloo/d4b12ca9e98723e5f523573058a8c0c6
# This class works to give checkbox widgets that the user can select to make choices for the search
class MultiCheckboxField(SelectMultipleField):
    widget = widgets.ListWidget(prefix_label=False)
    option_widget = widgets.CheckboxInput()

class searchForm(FlaskForm):
	gpu = TextField("Graphics Card")
	chipset = MultiCheckboxField(u'Chipset',choices = [('Nvidia', 'Nvidia'), ('AMD', 'AMD')], validators=[InputRequired()], default=['Nvidia'])
	brand = MultiCheckboxField(u'Brand', choices = [('AMD', 'AMD'), ('ASUS', 'ASUS'), ('EVGA', 'EVGA'), ('Gigabyte', 'Gigabyte'), ('MSI', 'MSI'), ('NVIDIA', 'NVIDIA'), ('Power VR', 'Power VR'), ('Sapphire', 'Sapphire'), ('Via', 'Via'), ('Zotac', 'Zotac')], validators=[InputRequired()], default=['ASUS'])
	maxPrice = IntegerField("Maximum Price")
	submit = SubmitField("Submit")

class ContactForm(FlaskForm):
    name = TextField("Name", validators=[InputRequired()])
    email = TextField("Email", validators=[InputRequired()])
    subject = TextField("Subject", validators=[InputRequired()])
    message = TextAreaField("Message")
    submit = SubmitField("Send")

class gpuForm(FlaskForm):
	memoryType = TextField("Memory Type", validators=[InputRequired()])
	numberOfCudaCores = IntegerField("Number Of Cuda Cores", validators=[InputRequired()])
	chipsetId = SelectField(u"Chipset", coerce=int, validators=[InputRequired()])
	outputId = SelectField(u"Output id", coerce=int, validators=[InputRequired()])
	averagePrice = IntegerField("Average Price", validators=[InputRequired()])
	submit = SubmitField("Submit")


class brandForm(FlaskForm):
	brandName = SelectField("Brand Name", choices = [('AMD', 'AMD'), ('ASUS', 'ASUS'), ('EVGA', 'EVGA'), ('Gigabyte', 'Gigabyte'), ('MSI', 'MSI'), ('NVIDIA', 'NVIDIA'), ('Power VR', 'Power VR'), ('Sapphire', 'Sapphire'), ('Via', 'Via'), ('Zotac', 'Zotac')], validators=[InputRequired()])
	productSeries = TextField("Product Series", validators=[InputRequired()])
	model = TextField("Model Name", validators=[InputRequired()])
	submit = SubmitField("Submit")

class chipsetForm(FlaskForm):
	chipsetManufacturer=SelectField("Chipset Manufacturer", choices = [('Nvidia', 'Nvidia'), ('AMD', 'AMD')], validators=[InputRequired()])
	graphicsCoprocessor = TextField("Graphics Coprocessor", validators=[InputRequired()])
	submit = SubmitField("Submit")

class outputForm(FlaskForm):
	displayPort = IntegerField("displayPort", validators=[InputRequired()])
	hdmi = IntegerField("hdmi", validators=[InputRequired()])
	vga = IntegerField("vga", validators=[InputRequired()])
	dvi = IntegerField('dvi', validators=[InputRequired()])
	submit = SubmitField("Submit")

class benchmarkForm(FlaskForm):
	unigine = IntegerField("Unigine score")
	passmark = IntegerField("Passmark score")
	shadow = IntegerField("Shadow of the Tomb Raider FPS")
	gta = IntegerField("GTA 5 FPS")
	submit = SubmitField("Submit")

class gpuBenchmarkForm(FlaskForm):
	gpuIdNumber = SelectField(u"GPU ID Number", coerce=int, validators=[InputRequired()])
	benchmarkIdNumber = SelectField(u"Bechmark ID Number", coerce=int, validators=[InputRequired()])
	submit = SubmitField("Submit")

class gpuBrandForm(FlaskForm):
	gpuIdNumber = SelectField(u"GPU ID Number", coerce=int, validators=[InputRequired()])
	brandIdNumber = SelectField(u"Brand ID Number", coerce=int, validators=[InputRequired()])
	submit = SubmitField("Submit")

class updateBenchmarkForm(FlaskForm):
	benchmarkIdNumber = SelectField(u"Benchmark ID Number", coerce=int)
	unigine = IntegerField("Unigine score")
	passmark = IntegerField("Passmark score")
	shadow = IntegerField("Shadow of the Tomb Raider FPS")
	gta = IntegerField("GTA 5 FPS")
	submit = SubmitField("Submit")

class gpuRemoveForm(FlaskForm):
	gpuIdNumber = SelectField(u"GPU ID Number", coerce=int)
	submit = SubmitField("Submit")
