# hello-flask
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
