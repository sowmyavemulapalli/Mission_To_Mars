from flask import Flask, render_template, redirect, url_for
from flask_pymongo import PyMongo
import scraping
import ssl

app = Flask(__name__)

app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
mongo = PyMongo(app)

@app.route("/")
def index():
   ssl._create_default_https_context = ssl._create_unverified_context
   mars = mongo.db.mars.find_one()
   return render_template("index.html", mars=mars)

@app.route("/scrape")
def scrape():
   print("scrape method-url triggered")
   mars = mongo.db.mars
   mars_data = scraping.scrape_all()
   mars.update({}, mars_data, upsert=True)
   mas = mongo.db.mars.find_one()
   return render_template("/index.html", mars=mas)
   
if __name__ == "__main__":
   app.run()


 