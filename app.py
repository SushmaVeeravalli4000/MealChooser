from flask import Flask, render_template, request, url_for, redirect, flash
from flask_sqlalchemy import SQLAlchemy
import randomizer

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
@app.route('/home')
def home():
    return render_template('home.html', food=randomizer.food(), foodlist=randomizer.fastFoodDict)


@app.route('/about')
def about():
    return render_template("about.html",title= "about")

@app.route('/mealchooser', methods=['POST', 'GET'])

def mealchooser():
    return render_template('mealchooser.html', food=randomizer.food(), foodlist=randomizer.fastFoodDict, title='mealchooser')


if __name__ == "__main__":
    app.run(debug=True)
    

    