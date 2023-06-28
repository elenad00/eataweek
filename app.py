from flask import Flask, render_template, redirect, url_for, request
from static.scripts.grocerystore import * 
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
  if meal not in ['breakfast','lunch','dinner','snack']:
    return redirect(url_for('error'))
  return render_template('addmeal.html', day = 'today', meal=meal)

@app.route('/<day>/<meal>/additem', methods=['GET','POST'])
def additem(day, meal):
  if request.method == 'GET':
    if meal not in ['breakfast','lunch','dinner','snack']:
      return redirect(url_for('error'))
    return render_template('additem.html', day = day, meal=meal, results=False)

  else:
    search_criteria = request.form.get('item')
    results = doSearch(search_criteria)
    return render_template('additem.html', day = day, meal=meal, results = results)


@app.route('/login')
def login():
  return render_template('login.html')

@app.route('/error')
def error():
  return render_template('blank.html')

if __name__ == '__main__':
  app.run(debug=True)