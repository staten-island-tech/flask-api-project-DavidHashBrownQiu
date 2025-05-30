from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route("/")
def index():
    response = requests.get("https://raw.githubusercontent.com/andyklimczak/TheReportOfTheWeek-API/refs/heads/master/data/reports.json")
    data = response.json()
    reviews = data['reports']

    foods = []
    manufacturers = set()

    for review in reviews:
        id = review['product']
        product = review['product']
        manufacturer = review.get('manufacturer', '').strip()
        videoCode = review['videoCode']
        imageUrl = f"https://img.youtube.com/vi/{videoCode}/0.jpg"

        foods.append({
            'id': id.lower(),
            'name': product.capitalize(),
            'company': manufacturer,
            'image': imageUrl
        })

        if manufacturer:  # make sure it's not empty
            manufacturers.add(manufacturer)

    return render_template("index.html", foods=foods, manufacturers=sorted(manufacturers))   

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

@app.route("/manufacturer/<name>")
def filter_by_manufacturer(name):
    response = requests.get("https://raw.githubusercontent.com/andyklimczak/TheReportOfTheWeek-API/refs/heads/master/data/reports.json")
    data = response.json()
    reviews = data['reports']

    filtered_foods = []
    for review in reviews:
        if review['manufacturer'].lower() == name.lower():
            filtered_foods.append({
                'id': review['product'].lower(),
                'name': review['product'].capitalize(),
                'company': review['manufacturer'],
                'image': f"https://img.youtube.com/vi/{review['videoCode']}/0.jpg"
            })

    if not filtered_foods:
        return render_template("error.html", message=f"No reviews found for {name}.")

    return render_template("index.html", foods=filtered_foods)


if __name__ == '__main__':
    app.run(debug=True)