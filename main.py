from flask import Flask, render_template, request, make_response, redirect, url_for


app = Flask(
  __name__,
  template_folder='templates',
  static_folder='static'
)

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/process')
def process():
  return "processing here"

if __name__ == '__main__':
  app.run(
	host='0.0.0.0',
	debug=True,
	port=8080
  )
