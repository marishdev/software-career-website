from flask import Flask, render_template

app = Flask(__name__)

JOBS = [
  {
    'id': 1,
    'title': 'Data Analyst',
    'location': 'Bengaluru, India',
    'salary': 'Rs. 10,00,000'
  },
  {
    'id': 2,
    'title': 'ui/ux developer',
    'location': 'chennai, India',
    'salary': 'Rs. 12,00,000'
  },
  {
    'id': 3,
    'title': 'front-end developer',
    'location': 'remote',
    'salary': 'Rs. 8,00,000'
  },
{
  'id': 4,
  'title': 'back-end developer',
  'location': 'remote',
  'salary': 'Rs. 14,00,000'
}

]




@app.route("/home")
def namecall():
    return render_template('home.html', jobs=JOBS)

if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=True)


