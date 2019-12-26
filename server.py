from flask import Flask, render_template, url_for, request, redirect
import csv
app = Flask(__name__)

# the html file will be searched by render_template in a template folder (thus move html file to template)
# have to give a name after the IP adress
@app.route('/')
def my_home():
    return render_template('index.html')

@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)

# create a database.txt before running this file
def write_to_file(data):
	with open('database.txt', mode='a') as database:
		# write to these three elements
		email = data["email"]
		subject = data["subject"]
		message  = data["message"]
		# use the f string to write to the elements within the curly brackets
		file = database.write(f'\n{email},{subject},{message}')

def write_to_csv(data):
	with open('database.csv', mode='a') as database2:
		# write to these three elements
		email = data["email"]
		subject = data["subject"]
		message  = data["message"]
		# use the f string to write to the elements within the curly brackets
		csv_writer = csv.writer(database2,delimiter=',',quotechar='"',quoting = csv.QUOTE_MINIMAL)	
		csv_writer.writerow([email,subject,message])
		
		
# POST = browser wants us to save data , GET = browser wants us to sent data
@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
	if request.method == 'POST':
		try:
			# request the data and use the dictionary function
			data = request.form.to_dict()
			# write to the file
			write_to_csv(data)
			print(data)
			# sent a message back to thank it
			return redirect('/thankyou.html')
		except:
			return 'did not save to database'
	else:
		# if it doesnt work wirte message that it doesnt work
		return 'something went wrong'