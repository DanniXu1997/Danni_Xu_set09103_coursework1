from flask import Flask
from flask import request
app = Flask(__name__)

@app.route('/', method=['GET', 'POST'])
def homepage():
  return "Welcome to Danni Music"

@app.route('/signin', methods=['GET'])
def signin_form():
  return '''<form action="/signin" method="post">
            <p><input name="username"></p>
            <p><input name="passwprd" type="password"></p>
            </form>'''

@app.route('/signin', methods=['POST', 'GET'])
def signin():
  if request.method == 'POST':
    print request.form
    name = request.form['name']
   return "hello  %s" % name
  else:
   return 'Bad username or password.'

if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)


