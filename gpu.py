from flask import Flask, render_template, url_for, json, redirect
from forms import ContactForm, gpuForm, brandForm, chipsetForm, benchmarkForm, gpuBenchmarkForm, gpuBrandForm, searchForm, updateBenchmarkForm, gpuRemoveForm, outputForm
from flask import request
from flask_wtf import FlaskForm
from wtforms import TextField, BooleanField, TextAreaField, SubmitField
import pandas as pd
import os
import database.db_connector as db

# The following code was borrowed directly from George Kochera's tutorial: https://github.com/gkochera/CS340-demo-flask-app/blob/master/app.py
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

	db_connection = db.connect_to_database()
	form = searchForm()

	if request.method == 'POST':

		gpu = request.form["gpu"]
		chipset = form.chipset.data
		brand = form.brand.data
		maxPrice = request.form["maxPrice"]

		gpuQuery = ""

		if gpu != "":
			gpuQuery = "graphicsCoprocessor LIKE '%%{}%%' AND ".format(gpu)


		# Get the length of the chipset list and instantiate the chipset Query String
		chipset_len = len(chipset) - 1
		chipsetQuery = "("
		
		# IF no values are selected
		if chipset_len == -1:

			# select all by default and update chipset length
			chipset.append("AMD")
			chipset.append("Nvidia")
			chipset_len = len(chipset) - 1


		# For values in the list of chipsets
		for value in chipset:

			# If we've reached the final value
			if chipset.index(value) == chipset_len:
				chipsetQuery += "chipsetManufacturer='" + value + "') AND "
				break
			# If we are still adding more values (using OR statement for next value)
			else:
				chipsetQuery += "chipsetManufacturer='" + value + "' OR "

		# Get the length of the brand list and instantiate the brand Query String
		brand_len = len(brand) - 1
		brandQuery = "("

		# if no values are selected, Add all options to list by default
		if brand_len == -1:

			# select all values by default
			brand_list = ['AMD','ASUS','EVGA','Gigabyte','MSI','NVIDIA','Power VR', 'Sapphire','Via','Zotac']

			# Adding all values to list by default
			for value in brand_list:
				brand.append(value)

			# updating the length of brand list
			brand_len = len(brand) - 1

		# For all values in list of brands
		for value in brand:

			# If we've reached the final value
			if brand.index(value) == brand_len:
				brandQuery += "brandName='" + value + "') AND "
				break

			# If we are still adding more values (using OR statement for next value)
			else:
				brandQuery += "brandName='" + value + "' OR "

		# If empty string was returned (no max price set), set to a default value
		if maxPrice == "":
			maxPrice = 9999

		# Price query declaration
		priceQuery = "averagePrice <= '{}';".format(maxPrice)


		query ="""SELECT chipsetManufacturer, brandName, graphicsCoprocessor, averagePrice, unigineBenchmarkScore, passmarkBenchmarkScore, shadowOfTheTombRaiderFPS, grandTheftAuto5FPS, displayPort, hdmi, vga, dvi
	 		FROM graphicsCards
			INNER JOIN graphicsCard_brands ON graphicsCards.id = graphicsCard_brands.gpuId
			INNER JOIN brands ON graphicsCard_brands.brandId = brands.id
			INNER JOIN graphicsCard_benchmarkValues ON graphicsCards.id = graphicsCard_benchmarkValues.gpuID
			INNER JOIN benchmarkValues ON benchmarkValues.id = graphicsCard_benchmarkValues.benchmarkId
			INNER JOIN chipsets ON graphicsCards.chipset = chipsets.id
			INNER JOIN outputs ON graphicsCards.outputs = outputs.id
			WHERE """ + gpuQuery + chipsetQuery + brandQuery + priceQuery

			# """chipsetManufacturer = '{}' AND brandName = '{}' """

		cursor = db.execute_query(db_connection=db_connection, query=query)

		results = cursor.fetchall()

		print(results)

		return render_template('comparisons.html', title='Comparisons', gpu=results, form=form)

	else:
		return render_template('comparisons.html', title='Comparisons', form=form)

@app.route("/add")
def add():
	return render_template('add.html', title='Add')

@app.route("/add_gpu", methods=["GET","POST"])
def add_gpu():

	db_connection = db.connect_to_database()

	# Create a query for the chipsets and run it to get all active chipsets in the DB
	chipsetQuery = "SELECT * from chipsets;"
	cursor = db.execute_query(db_connection=db_connection, query=chipsetQuery)
	chipsetResults = cursor.fetchall()

	# Create tuples for each thing in the db with the id and graphics coprocessor
	chipset_list = [(i["id"], i["graphicsCoprocessor"]) for i in chipsetResults]

	outputQuery = "SELECT * from outputs;"
	cursor = db.execute_query(db_connection=db_connection, query=outputQuery)
	outputResults = cursor.fetchall()

	print(outputResults)

	# Create tuples for each thing in the db with the id 
	output_list = [(i["id"], i["id"]) for i in outputResults]

	print("Output LIST")
	print(output_list)

	form = gpuForm()

	# fill the form the with chipset choices from the list
	form.chipsetId.choices = chipset_list
	form.outputId.choices = output_list

	if request.method == 'POST':

		memoryType = request.form["memoryType"]
		numberOfCudaCores = request.form["numberOfCudaCores"]
		chipsetId = request.form["chipsetId"]
		outputId = request.form["outputId"]
		averagePrice = request.form["averagePrice"]

		# Pandas information borrowed from https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.html
		# We are using this to store data in a comma separated value file for future reference
		res = pd.DataFrame({'memoryType':memoryType, 'numberOfCudaCores':numberOfCudaCores, 'chipsetId':chipsetId, 'outputId': outputId, 'averagePrice':averagePrice}, index=[0])
		res.to_csv('./add_gpu.csv')
		print("The data are saved")

		query = """INSERT INTO graphicsCards(memoryType, numberOfCudaCores, chipset, outputs, averagePrice)
		Values ('{}','{}','{}','{}', '{}')""".format(memoryType, numberOfCudaCores, chipsetId, outputId, averagePrice)

		# Cursor/results are both borrowed from the flask app tutorial: https://github.com/gkochera/CS340-demo-flask-app/blob/master/app.py
		cursor = db.execute_query(db_connection=db_connection, query=query)
		results = cursor.fetchall()

		return(redirect(url_for('add_gpu')))

	else:
		return render_template("add_gpu.html", form=form, title="Add a gpu")

@app.route("/add_brand", methods=["GET","POST"])
def add_brand():

	db_connection = db.connect_to_database()

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

	db_connection = db.connect_to_database()

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

@app.route("/add_output", methods=["GET", "POST"])
def add_output():

	db_connection = db.connect_to_database()

	outputQuery = "SELECT * from outputs"
	cursor = db.execute_query(db_connection=db_connection, query=outputQuery)
	results = cursor.fetchall()

	form = outputForm()

	if request.method == 'POST':

		displayPort = request.form["displayPort"]
		hdmi = request.form["hdmi"]
		vga = request.form["vga"]
		dvi = request.form["dvi"]
		res = pd.DataFrame({'displayPort':displayPort , 'hdmi':hdmi, 'vga':vga, 'dvi':dvi}, index=[0])
		res.to_csv('./add_output.csv')
		print("The data are saved")

		if displayPort == "":
			displayPort = 0
		if hdmi == "":
			hdmi = 0
		if vga == "":
			vga = 0
		if dvi == "":
			dvi = 0


		query = """INSERT INTO outputs (displayPort, hdmi, vga, dvi)
		VALUES (""" + displayPort + "," + hdmi + "," + vga + "," + dvi +")"

		cursor = db.execute_query(db_connection=db_connection, query=query)

		results = cursor.fetchall()

		return(redirect(url_for('add_output')))

	else:
		return render_template("add_output.html", form=form, title="Add outputs", gpu=results)


@app.route("/add_benchmarks", methods=["GET","POST"])
def add_benchmarks():

	db_connection = db.connect_to_database()

	# Benchmark query for a dynamic drop-down
	benchmarkQuery = "SELECT * from benchmarkValues"
	cursor = db.execute_query(db_connection=db_connection, query=benchmarkQuery)
	results = cursor.fetchall()

	form = benchmarkForm()
	
	if request.method =='POST':
		unigine = request.form["unigine"]
		passmark = request.form["passmark"]
		shadow = request.form["shadow"]
		gta = request.form["gta"]
		res=pd.DataFrame({'unigine':unigine, 'passmark':passmark, 'shadow':shadow, 'gta':gta}, index=[0])
		res.to_csv('./add_benchmarks.csv')
		print("The data are saved")

		if unigine == "":
			unigine = 'NULL';

		if passmark == "":
			passmark = "NULL"

		if shadow == "":
			shadow = "NULL"

		if gta == "":
			gta = "NULL"



		query = """INSERT INTO benchmarkValues (unigineBenchmarkScore, passmarkBenchmarkScore, shadowOfTheTombRaiderFPS, grandTheftAuto5FPS)
		VALUES (""" + unigine + "," + passmark + "," + shadow + "," + gta +")"

		cursor = db.execute_query(db_connection=db_connection, query=query)

		results = cursor.fetchall()

		return(redirect(url_for('add_benchmarks')))

	else:
		return render_template("add_benchmarks.html", form=form, title="Add Benchmarks", gpu=results)

@app.route("/add_gpu_benchmarks", methods=["GET","POST"])
def add_gpu_benchmarks():

	db_connection = db.connect_to_database()

	# Create a query for the gpu and run it to get all active chipsets in the DB
	gpuQuery = "SELECT * from graphicsCards;"
	cursor = db.execute_query(db_connection=db_connection, query=gpuQuery)
	gpuResults = cursor.fetchall()

	# Create tuples for each thing in the db with the id and graphics coprocessor
	gpu_list = [(i["id"], i["id"]) for i in gpuResults]

	# Create a query for the benchmarks and run it to get all active benchmarks in the DB
	benchmarkQuery = "SELECT * from benchmarkValues"
	cursor = db.execute_query(db_connection=db_connection, query=benchmarkQuery)
	benchmarkResults = cursor.fetchall()

	# Create tuples for each thing in the db with the id and graphics coprocessor
	benchmark_list = [(i["id"], i["id"]) for i in benchmarkResults]


	form = gpuBenchmarkForm()

	form.gpuIdNumber.choices = gpu_list
	form.benchmarkIdNumber.choices = benchmark_list

	if request.method == 'POST':
		gpuIdNumber = request.form["gpuIdNumber"]
		benchmarkIdNumber = request.form["benchmarkIdNumber"]
		res=pd.DataFrame({'gpuIdNumber':gpuIdNumber, 'benchmarkIdNumber':benchmarkIdNumber}, index=[0])
		res.to_csv('./add_gpu_benchmarks.csv')
		print("The data are saved")

		query = """INSERT INTO graphicsCard_benchmarkValues(gpuID, benchmarkID)
		VALUES ({},{})""".format(gpuIdNumber, benchmarkIdNumber)

		cursor = db.execute_query(db_connection=db_connection, query=query)

		results = cursor.fetchall()
		return(redirect(url_for('add_gpu_benchmarks')))

	else:
		return render_template("add_gpu_benchmarks.html", form=form, title="Add GPU Benchmarks")

@app.route("/add_gpu_brand", methods=["GET","POST"])
def add_gpu_brand():

	db_connection = db.connect_to_database()

	# Create a query for the gpu and run it to get all active chipsets in the DB
	gpuQuery = "SELECT * from graphicsCards;"
	cursor = db.execute_query(db_connection=db_connection, query=gpuQuery)
	gpuResults = cursor.fetchall()

	# Create tuples for each thing in the db with the id and graphics coprocessor
	gpu_list = [(i["id"], i["id"]) for i in gpuResults]

	# Create a query for the benchmarks and run it to get all active benchmarks in the DB
	brandQuery = "SELECT * from brands"
	cursor = db.execute_query(db_connection=db_connection, query=brandQuery)
	brandResults = cursor.fetchall()

	# Create tuples for each thing in the db with the id and graphics coprocessor
	brand_list = [(i["id"], i["id"]) for i in brandResults]


	form = gpuBrandForm()

	form.gpuIdNumber.choices = gpu_list
	form.brandIdNumber.choices = brand_list


	if request.method == 'POST':
		gpuIdNumber = request.form["gpuIdNumber"]
		brandIdNumber = request.form["brandIdNumber"]
		res=pd.DataFrame({'gpuIdNumber': gpuIdNumber, 'brandIdNumber':brandIdNumber}, index=[0])
		res.to_csv('./add_gpu_brand.csv')
		print("The data are saved")

		query = """INSERT INTO graphicsCard_brands(gpuID, brandID)
		VALUES ({},{})""".format(gpuIdNumber, brandIdNumber)

		cursor = db.execute_query(db_connection=db_connection, query=query)

		results = cursor.fetchall()
		return(redirect(url_for('add_gpu_brand')))
		
	else:
		return render_template("add_gpu_brand.html", form=form, title="Add GPU Brands")

@app.route("/update_benchmarks", methods=["GET","POST"])
def update_benchmarks():

	db_connection = db.connect_to_database()

	# Benchmark query for a dynamic drop-down
	benchmarkQuery = "SELECT * from benchmarkValues"
	cursor = db.execute_query(db_connection=db_connection, query=benchmarkQuery)
	benchmarkResults = cursor.fetchall()

	# Create tuples for each thing in the db with the id and graphics coprocessor
	benchmark_list = [(i["id"], i["id"]) for i in benchmarkResults]
	form = updateBenchmarkForm()
	form.benchmarkIdNumber.choices = benchmark_list

	query = """SELECT chipsetManufacturer, brandName, graphicsCoprocessor, averagePrice, benchmarkValues.id, unigineBenchmarkScore, passmarkBenchmarkScore, shadowOfTheTombRaiderFPS, grandTheftAuto5FPS 
	 		FROM graphicsCards
			INNER JOIN graphicsCard_brands ON graphicsCards.id = graphicsCard_brands.gpuId
			INNER JOIN brands ON graphicsCard_brands.brandId = brands.id
			INNER JOIN graphicsCard_benchmarkValues ON graphicsCards.id = graphicsCard_benchmarkValues.gpuID
			INNER JOIN benchmarkValues ON benchmarkValues.id = graphicsCard_benchmarkValues.benchmarkId
			INNER JOIN chipsets ON graphicsCards.chipset = chipsets.id"""

	newcursor = db.execute_query(db_connection=db_connection, query=query)

	results = newcursor.fetchall()
	if request.method =='POST':
		benchmarkIdNumber = request.form["benchmarkIdNumber"]
		unigine = request.form["unigine"]
		passmark = request.form["passmark"]
		shadow = request.form["shadow"]
		gta = request.form["gta"]
		res=pd.DataFrame({'benchmarkIdNumber':benchmarkIdNumber,'unigine':unigine, 'passmark':passmark, 'shadow':shadow, 'gta':gta}, index=[0])
		res.to_csv('./update_benchmarks.csv')
		print("The data are saved")

		# Run a query to get the previous results in our target row and store them in variables
		currentQuery = "SELECT unigineBenchmarkScore, passmarkBenchmarkScore, shadowOfTheTombRaiderFPS, grandTheftAuto5FPS FROM benchmarkValues WHERE id={}".format(benchmarkIdNumber)
		cursor = db.execute_query(db_connection=db_connection, query=currentQuery)
		results=cursor.fetchall()

		prevUnigine = results[0]['unigineBenchmarkScore']
		prevPass = results[0]['passmarkBenchmarkScore']
		prevShadow = results[0]['shadowOfTheTombRaiderFPS']
		prevGta = results[0]['grandTheftAuto5FPS']

		# If no input was passed, use the same values that were already in the row
		if unigine == "":
			unigine = prevUnigine

		if passmark == "":
			passmark = prevPass

		if shadow == "":
			shadow = prevShadow

		if gta == "":
			gta = prevGta

		updateQuery = """UPDATE benchmarkValues 
		SET unigineBenchmarkScore={}, passmarkBenchmarkScore={},shadowOfTheTombRaiderFPS={}, grandTheftAuto5FPS={}
        WHERE id={}""".format(unigine, passmark, shadow, gta, benchmarkIdNumber)

		cursor = db.execute_query(db_connection=db_connection, query=updateQuery)
      
		return redirect(url_for('update_benchmarks'))
	else:
		return render_template("update_benchmarks.html", form=form, title="Update Benchmarks", gpu=results)

@app.route("/remove_gpu", methods=["GET","POST"])
def remove_gpu():

	db_connection = db.connect_to_database()

	# Create a query for the gpu and run it to get all active chipsets in the DB
	gpuQuery = "SELECT * from graphicsCards;"
	cursor = db.execute_query(db_connection=db_connection, query=gpuQuery)
	gpuResults = cursor.fetchall()

	# Create tuples for each thing in the db with the id and graphics coprocessor
	gpu_list = [(i["id"], i["id"]) for i in gpuResults]

	form = gpuRemoveForm()

	form.gpuIdNumber.choices = gpu_list

	if  request.method =='POST':
		gpuIdNumber = request.form["gpuIdNumber"]
		res=pd.DataFrame({'gpuIdNumber': gpuIdNumber}, index=[0])
		res.to_csv('./remove_gpu.csv')
		print("The data are saved")

		query = """DELETE FROM graphicsCards
		WHERE {} = graphicsCards.id;""".format(gpuIdNumber)
		
		cursor = db.execute_query(db_connection=db_connection, query=query)
		cursor.close()
		cursor = db_connection.cursor()

		query = """DELETE FROM graphicsCard_brands
		WHERE {} = graphicsCard_brands.gpuId;""".format(gpuIdNumber)
		cursor = db.execute_query(db_connection=db_connection, query=query)
		cursor.close()
		cursor = db_connection.cursor()
		
		query = """DELETE FROM graphicsCard_benchmarkValues
		WHERE {} = graphicsCard_benchmarkValues.gpuID 
		""".format(gpuIdNumber)

		cursor = db.execute_query(db_connection=db_connection, query=query)

		results = cursor.fetchall()
		return(redirect(url_for('remove_gpu')))
	else:
        	return render_template("remove_gpu.html", form=form, title="Remove GPU", gpu=gpuResults)

@app.route("/contact", methods=["GET","POST"])
def contact():
	
	db_connection = db.connect_to_database()

	form = ContactForm()

	if request.method == 'POST':
		name =  request.form["name"]
		email = request.form["email"]
		subject = request.form["subject"]
		message = request.form["message"]
		res = pd.DataFrame({'name':name, 'email':email, 'subject':subject ,'message':message}, index=[0])
		res.to_csv('./contactUsMessage.csv')
		print("The data are saved !")
		return redirect(url_for('contact'))
	else:
		return render_template('contact.html', form=form)

if __name__ == '__main__':
        port = int(os.environ.get('PORT', 8994))
        app.run(port=port, debug=True)

