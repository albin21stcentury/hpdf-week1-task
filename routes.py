import requests
from flask import Flask,render_template,make_response,send_file,request

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World - Albin'

@app.route('/authors')
def get_data():
    r1 = requests.get('https://jsonplaceholder.typicode.com/users')
    r2 = requests.get('https://jsonplaceholder.typicode.com/posts')
    jobject1=r1.json()
    jobject2=r2.json()
    return render_template('authors.html',authors=jobject1,posts=jobject2)

@app.route('/setcookie')
def setcookie():

   resp=make_response("Cookies are set")
   if 'name' not in request.cookies:
       resp.set_cookie('name','Albin')
   if 'age' not in request.cookies:
       resp.set_cookie('age','21')
   else:
       resp=make_response('Cookies are already set.')
   return resp

@app.route('/getcookies')
def getcookie():
   name = request.cookies.get('name')
   age = request.cookies.get('age')
   return '<h1>Name is '+name+' <br>Age is '+age+'</h1>'

@app.route('/robots.txt')
def deny():
    return send_file('robots.txt')

@app.route('/html')
def render_html():
    return render_template('simple.html')

@app.route('/image')
def render_image():
    return render_template('img.html')

@app.route('/input')
def input():
   return render_template('input.html')

@app.route('/display', methods = ['POST', 'GET'])
def display():
   if request.method == 'POST':
       input = request.form['value']
       print(input)
   return 'Input printed on terminal'
if __name__ == "__main__":
    app.run()
