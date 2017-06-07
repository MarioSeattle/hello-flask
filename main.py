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

time_form = """
    <style>
        .error {{ color: red; }}
    </style>
    <h1>Validate Time</h1>
    <form method='POST'>
        <label>Hours (24-hour format)
            <input name="hours" type="text" value='{hours}' />
        </label>
        <p class="error">{hours_error}</p>
        <label>Minutes
            <input name="minutes" type="text" value='{minutes}' />
        </label>
        <p class="error">{minutes_error}</p>
        <input type="submit" value="Validate" />
    </form>
    """
    #places holders {minutes_error}
    #empty strings will be place on def display_time_format
    #setup a route
    #def = handler
    #@app.route('/validate-time', methods=['POST']) AVAILABLE URL
@app.route('/validate-time')
def display_time_form():
    return time_form.format(hours='', hours_error='',minutes='', minutes_error='')


app.run()