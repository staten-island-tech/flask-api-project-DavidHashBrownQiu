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
        id = review['product']
        product = review['product']
        manufacturer = review['manufacturer']
        videoCode = review['videoCode']
        imageUrl = f"https://img.youtube.com/vi/{videoCode}/0.jpg"  # note to self: this for loop helps w/ searching through revi4ews
        #to put info into the list for each product of the databawswe
        foods.append({
            'id': id.lower(),
            'name': product.capitalize(),
            'company': manufacturer,
            'image': imageUrl
        })

    return render_template("index.html", foods=foods)    

@app.route("/review/<id>")
def reviews(id):
    response = requests.get("https://raw.githubusercontent.com/andyklimczak/TheReportOfTheWeek-API/refs/heads/master/data/reports.json")
    data = response.json()
    reviews = data['reports']

    review = next((r for r in reviews if r['product'].lower() == id), None)

    if not review:
        return render_template("error.html", message="Review not found.")

    product = review['product']
    manufacturer = review['manufacturer']
    rating = review.get('rating', 'No rating available')
    videoCode = review['videoCode']
    imageUrl = f"https://img.youtube.com/vi/{videoCode}/0.jpg"

    return render_template("reviews.html",
                           product=product,
                           manufacturer=manufacturer,
                           rating=rating,
                           image=imageUrl,
                           videoCode=videoCode)

if __name__ == '__main__':
    app.run(debug=True)