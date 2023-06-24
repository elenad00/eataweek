from flask import Flask, render_template
from static.scripts.scripts import * 
app = Flask(__name__)

@app.route('/')
def index():
  # check login
  # get current data rates and populate calories n percentages
  calories, percentages = getToday()
  return render_template('index.html', calories_left = calories, perc=percentages)

@app.route('/today')
def today():
  return render_template('today.html')

@app.route('/profile')
def profile():
  return render_template('profile.html')

@app.route('/plan')
def plan():
  return render_template('mealplan.html')

@app.route('/today/<meal>')
def meal(meal):
  return render_template('addmeal.html')

@app.route('/login')
def login():
  return render_template('login.html')

if __name__ == '__main__':
  app.run(debug=True)