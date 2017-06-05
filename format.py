#formatting methods for str in python
#working with long strings that consist in chunks of HTML that will be rendiering the returning from
#flask handlers
#Showing the ways to insert ingo using the string method
#place holder that will insert the value 0
#We can use name place holder too <title>tittle</title> and call it instead of {1}

markup = """
<!doctype html>
<html>
    <head>
        <title>{0}</title>

    </head>
    <body>
        <h1>{1}</h1>

    </body>

</html>
"""
#within the format method we can give value to be inserted in the place holder str
markup = markup.format('My Page Title', 'Page Heading')
print(markup)