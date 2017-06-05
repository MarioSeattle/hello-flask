from flask import Flask, request

app = Flask(__name__)
app.config['DEBUG'] = True


form = """ 
<!doctype html>
<html>

<body>

<form action="/hello" method="post">
    <label for="first-name">First Name:</label>
    <input id="first-name" type="test" name="first_name"/>
    <input type="submit"/>
</form>

</body>

</hmtl>

"""


@app.route("/")
def index():
    return form

#handler to catch the inputand send the data to server /hello route
@app.route("/hello", methods=['POST'])
def hello():
#the html will display first_name + greeting message
#http://127.0.0.1:5000/hello?first_name=Mario
    first_name = request.form['first_name'] 
    return '<h1>Hello, ' + first_name + '</h1>'
        
app.run()