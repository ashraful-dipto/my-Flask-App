from flask import Flask, render_template, url_for, request, redirect

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
   return render_template('home.html')

@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)


if __name__ == '__main__':
   app.run(debug=True)