from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return 'Welcome to Fitness Track'

@app.route('/workout')
def about():
    return render_template(workoutlog.html)

@app.route('/waterintake')
def about():
    return render_template(waterintake.html)

@app.route('/suggestions')
def about():
    return render_template(suggestions.html)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')