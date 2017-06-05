#formatting methods for str in python
#working with long strings that consist in chunks of HTML that will be rendiering the returning from
#flask handlers
#Showing the ways to insert ingo using the string method
#place holder that will insert the value 0
#We can use name place holder too <title>tittle</title> and call it instead of {1}
# Using indexed placeholders

markup = """
<!doctype html>
<html>
    <head>
        <title>{0}</title>
    </head>
    <body>
        <h1>{0}</h1>
    </body>
</html>
"""

markup = markup.format('My Page Title', 'My Page Heading')
print(markup)

# Using named placeholders

markup = """
<!doctype html>
<html>
    <head>
        <title>{title}</title>
    </head>
    <body>
        <h1>{heading}</h1>
    </body>
</html>
"""

markup = markup.format(title='My Page Title', heading='My Page Heading')
print(markup)