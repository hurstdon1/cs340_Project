from flask import Flask, render_template, url_for, json, redirect
from forms import ContactForm, gpuForm, brandForm, chipsetForm, pricingForm, benchmarkForm, gpuBenchmarkForm, gpuBrandForm, searchForm
from flask import request
from flask_wtf import FlaskForm
from wtforms import TextField, BooleanField, TextAreaField, SubmitField
import pandas as pd
import os
import database.db_connector as db

app = Flask(__name__)

db_connection = db.connect_to_database()

app.config['SECRET_KEY'] = 'f5a6c63d94bf77cb2c4845153a56cbba'

@app.route("/")
@app.route("/home")
def hello():
    return render_template('home.html')

@app.route("/about")
def about():
	return render_template('about.html', title='About')

@app.route("/comparisons", methods=["GET","POST"])
def comparisons():

	form = searchForm()

	if request.method == 'POST':

		gpu = request.form["gpu"]
		chipset = request.form["chipset"]
		brand = request.form["brand"]
		maxPrice = request.form["maxPrice"]

		query ="""SELECT chipsetManufacturer, brandName, graphicsCoprocessor, averagePrice, unigineBenchmarkScore, passmarkBenchmarkScore, shadowOfTheTombRaiderFPS, grandTheftAuto5FPS 
	 		FROM graphicsCards
			INNER JOIN graphicsCard_brands ON graphicsCards.id = graphicsCard_brands.gpuId
			INNER JOIN brands ON graphicsCard_brands.gpuId = brands.id
			INNER JOIN graphicsCard_benchmarkValues ON graphicsCards.id = graphicsCard_benchmarkValues.gpuID
			INNER JOIN benchmarkValues ON benchmarkValues.id = graphicsCard_benchmarkValues.benchmarkId
			INNER JOIN chipsets ON chipsets.id = graphicsCards.chipset
			WHERE chipsetManufacturer = '{}' AND brandName = '{}' """.format(chipset, brand)

		cursor = db.execute_query(db_connection=db_connection, query=query)

		results = cursor.fetchall()

		return render_template('comparisons.html', title='Comparisons', gpu=results, form=form)

	else:
		return render_template('comparisons.html', title='Comparisons', form=form)

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

		query = """INSERT INTO brands (brandName, productSeries, model)
		VALUES ('{}', '{}', '{}')""".format(brandName, productSeries, model)

		cursor = db.execute_query(db_connection=db_connection, query=query)

		results = cursor.fetchall()

		return(redirect(url_for('add_brand')))

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

		query = """INSERT INTO chipsets (chipsetManufacturer, graphicsCoprocessor)
		VALUES ('{}','{}')""".format(chipsetManufacturer, graphicsCoprocessor)

		cursor = db.execute_query(db_connection=db_connection, query=query)

		results = cursor.fetchall()

		return(redirect(url_for('add_chipset')))	

	else:
		return render_template("add_chipset.html", form=form, title="Add a chipset")

@app.route("/add_pricing", methods=["GET","POST"])
def add_pricing():

	form = pricingForm()

	if request.method == 'POST':
		averagePrice = request.form["averagePrice"]
		res = pd.DataFrame({'averagePrice':averagePrice}, index=[0])
		res.to_csv('./add_pricing.csv')
		print("The data are saved")

	else:
		return render_template("add_pricing.html", form=form, title="Add Pricing")

@app.route("/add_benchmarks", methods=["GET","POST"])
def add_benchmarks():

	form = benchmarkForm()
	
	if request.method =='POST':
		unigine = request.form["unigine"]
		passmark = request.form["passmark"]
		shadow = request.form["shadow"]
		gta = request.form["gta"]
		res=pd.DataFrame({'unigine':unigine, 'passmark':passmark, 'shadow':shadow, 'gta':gta}, index=[0])
		res.to_csv('./add_benchmarks.csv')
		print("The data are saved")

		query = """INSERT INTO benchmarkValues (unigineBenchmarkScore, passmarkBenchmarkScore, shadowOfTheTombRaiderFPS, grandTheftAuto5FPS)
		VALUES (""" + unigine + "," + passmark + "," + shadow + "," + gta +")"

		cursor = db.execute_query(db_connection=db_connection, query=query)

		results = cursor.fetchall()

		return(redirect(url_for('add_benchmarks')))

	else:
		return render_template("add_benchmarks.html", form=form, title="Add Benchmarks")

@app.route("/add_gpu_benchmarks")
def add_gpu_benchmarks():

	form = gpuBenchmarkForm()

	if request.method == 'POST':
		gpuIdNumber = request.form["gpuIdNumber"]
		benchmarkIdnumber = request.form["benchmarkIdNumber"]
		res=pd.DataFrame({'gpuIdNumber':gpuIdNumber, 'benchmarkIdnumber':benchmarkIdnumber}, index=[0])
		res.to_csv('./add_gpu_benchmarks.csv')
		print("The data are saved")

	else:
		return render_template("add_gpu_benchmarks.html", form=form, title="Add GPU Benchmarks")

@app.route("/add_gpu_brand")
def add_gpu_brand():

	form = gpuBrandForm()

	if request.method == 'POST':
		gpuIdNumber = request.form["gpuIdNumber"]
		brandIdNumber = request.form["brandIdNumber"]
		res=pd.DataFrame({'gpuIdNumber': gpuIdNumber, 'brandIdNumber':brandIdNumber}, index=[0])
		res.to_csv('./add_gpu_brand.csv')
		print("The data are saved")
		
	else:
		return render_template("add_gpu_brand.html", form=form, title="Add GPU Brands")

@app.route("/update_benchmarks", methods=["GET","POST"])
def update_benchmarks():

        form = benchmarkForm()

        if request.method =='POST':
                unigine = request.form["unigine"]
                passmark = request.form["passmark"]
                shadow = request.form["shadow"]
                gta = request.form["gta"]
                res=pd.DataFrame({'unigine':unigine, 'passmark':passmark, 'shadow':shadow, 'gta':gta}, index=[0])
                res.to_csv('./update_benchmarks.csv')
                print("The data are saved")

        else:
                return render_template("update_benchmarks.html", form=form, title="Update Benchmarks")

@app.route("/remove_gpu")
def remove_gpu():
        return render_template("remove_gpu.html", title="Remove GPU")

@app.route("/contact", methods=["GET","POST"])
def contact():

	form = ContactForm()

	if request.method == 'POST':
		name =  request.form["name"]
		email = request.form["email"]
		subject = request.form["subject"]
		message = request.form["message"]
		res = pd.DataFrame({'name':name, 'email':email, 'subject':subject ,'message':message}, index=[0])
		print("The data are saved !")
		return redirect(url_for('contact'))
	else:
		return render_template('contact.html', form=form)

if __name__ == '__main__':
        port = int(os.environ.get('PORT', 8993))
        app.run(port=port, debug=True)

