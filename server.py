from flask import Flask, render_template, url_for, request, redirect
import csv
app = Flask(__name__)


# to make it more dynamic, we accept the page name in the url and passed it to the fun. to open
@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)

def write_to_file(data):
    with open("web_server\database.txt", mode="a") as db:
        email = data["email"]
        message = data["message"]
        subject = data["subject"]
        file = db.write(f"\n{email},{subject},{message}")


def write_to_csv(data):
    with open('web_server\database.csv', newline='', mode='a') as db2:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        csv_writer = csv.writer(db2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        # 1st arg is the database we wanna store data in.
        # delimiter is the separator
        # quotechar if we wanna any quotes around the items
        # quoting MINIMAL means don't quote unless have a special character

        csv_writer.writerow([email,subject,message])


@app.route('/submit_form', methods=['GET', 'POST'])#post means sending data to server. get mean getting data from server
def submit_form():
    if request.method == "POST":
        try:
            #data = request.form["message"] if we wanna access a specific part of the form
            name1 = request.form.get("subject")
            data = request.form.to_dict()
            write_to_csv(data)
            #return redirect("/thankyou.html")
            return render_template("/thankyou.html", name1=name1)
        except:
            return "did not save to database"
    else:
        return "something went wrong!!"





# @app.route('/index.html')
# def index():
#     return render_template('index.html')
#
# @app.route('/about.html')
# def about():
#     return render_template('about.html')
#
# @app.route('/contact.html')
# def contact():
#     return render_template('contact.html')
#
# @app.route('/components.html')
# def components():
#     return render_template('components.html')
#
# @app.route('/works.html')
# def works():
#     return render_template('works.html')

