from flask import Flask, render_template
import requests

app = Flask(__name__)

# Route for the home page
@app.route("/")
def index():
    response = requests.get("https://raw.githubusercontent.com/andyklimczak/TheReportOfTheWeek-API/refs/heads/master/data/reports.json")
    data = response.json()
    reviews = data['reports']

    foods = [] #used to use the info needed

    for review in reviews:
        product = review['product']
        manufacturer = review['manufacturer']
        videoCode = review['videoCode']
        imageUrl = f"https://img.youtube.com/vi/{videoCode}/0.jpg"  # note to self: this for loop helps w/ searching through revi4ews
        #to put info into the list for each product of the databawswe
        foods.append({
            'name': product.capitalize(),
            'company': manufacturer,
            'image': imageUrl
        })

    return render_template("index.html", foods=foods)

@app.route("/review/")

if __name__ == '__main__':
    app.run(debug=True)