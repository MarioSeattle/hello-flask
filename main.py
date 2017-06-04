from flask import Flask

app = Flask(__name__)
app.config['DEBUG'] = True


form = """ 
<!doctype html>
<html>

<body>

<form>
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
    

app.run()