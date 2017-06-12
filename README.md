# hello-flask lessons
Lesson one SERVER SIDE VALIDATION
In this lesson we'll create a form where a user can enter a time in hours and minutes, and then we'll validate the input and tell the user whether that is a valid time.

The steps we'll follow to accomplish this are:

Create an HTML form with placeholders that will be filled with values using str.format and create a route for it
Write the code to process the form and provide feedback to the user:
Get the data from the request
Provide error message to the user if input is invalid or provide success message if the input is valid:
Use a Try/Except block to test the input for whether it consists of integers
Provide unique error messages based on how the input was invalid (not an integer vs. out of range)
Create a message to display if input is valid (if the error messages are empty)
Leave valid values in place in the input fields, but remove invalid values

Lesson 2 USING REDIRECTS 
Notes
Instead of merely providing a success message, web apps typically redirect users to a different page after they successfully submit information (e.g., login). In this video, we will add this functionality to our app to see how it works.

The main difference from our previous code will be to replace our success message with return redirect(url-path) where the url-path is a handler that we create to display the HTML for a response to valid inputs. We can then proceed to give specific info back to the user using query paramaters.

Lesson HTML Escaping 
Notes
HTML escaping is essential for developing safe web apps as it helps prevent Cross Site Scripting (XSS), which is a term used for malicious JavaScript injection. To learn more about why XSS is dangerous, read Part One of this article: Excess XSS: A comprehensive tutorial on cross-site scripting.

Jinja2 HTML Templates
In this video we learn how to make our code more maintainable and encapsulated by removing the long strings of HTML from our main.py and putting them into templates. We will do this using a Python templating engine called Jinja2. Here are the steps we'll follow:

import os and import jinja2 in main.py
Create a directory named templates and then use the imported os object to construct a string that contains the file path to this directory. Note that this path will be an absolute path in the filesystem on which the program is running.
template_dir = os.path.join(os.path.dirname(__file__),
    'templates')
Initialize the Jinja templating environment, using the template_dir:
jinja_env = jinja2.Environment(
    loader = jinja2.FileSystemLoader(template_dir))
Extract the HTML string in the variable form and put it in a newly created hello_form.html file in the templates directory.
In the index function, create a template variable that holds the template returned from Jinja's get_template function and then return the string that template.render() returns:
def index():
    template = jinja_env.get_template('hello_form.html')
    return template.render()
Extract the HTML string that hello returns from main.py and put it in a newly created hello_greeting.html file in the templates directory. Be sure to add the proper doctype and head/body tags.
Repeat step 5 for the hello function, but this time pass an argument to template.render that matches a placeholder called name in the template itself:
def hello():
    first_name = request.form['first_name']
    template = jinja_env.get_template('hello_greeting.html')
    return template.render(name=first_name)
Protect your code from malicious users by adding HTML escaping via Jinja's autoescape=True option:
jinja_env = jinja2.Environment(
    loader = jinja2.FileSystemLoader(template_dir), autoescape=True)
