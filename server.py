from flask import Flask, render_template, request, redirect
import csv
app = Flask(__name__)

@app.route("/")
def my_home():
    return render_template("index.html") #"<p>Hello, Monjurul Islam Shakil!</p>"

@app.route("/<string:page_name>")
def my_works(page_name):
    return render_template(page_name)

# @app.route("/about.html")
# def about():
#     return render_template("about.html")

# @app.route("/contact.html")
# def my_contact():
#     return render_template("contact.html")

# @app.route("/components.html")
# def my_components():
#     return render_template("components.html")

def write_to_file(data):
    with open('database.txt', mode='a') as database:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        file = database.write(f'\n{email}, {subject}, {message}')

def write_to_csv(data):
    with open('database.csv', mode='a', newline='') as database2:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        csv_writer = csv.writer(database2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == "POST":
        data = request.form.to_dict()
        write_to_csv(data)
        return redirect('/thankyou.html')
    else:
        return 'something went wrong! try again..'