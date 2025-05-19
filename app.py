from flask import Flask, render_template
import requests

app = Flask(__name__)

# Route for the home page
@app.route("/")
def index():
    response = requests.get("https://raw.githubusercontent.com/Hipo/university-domains-list/refs/heads/master/world_universities_and_domains.json")
    data = response.json()

    universities = []

if __name__ == '__main__':
    app.run(debug=True)