
"""
This is a general overview of how web servers' request-response cycle works,
with Flask examples.

When a user enters a URL into their web browser, it goes through the Internet
as an HTTP request (basically just the URL).

When that request arrives at your server, your server will construct an HTTP
response containing the HTML that your web server is programmed to send when
a user requests that particular URL.

Flask helps you do this by allowing you to write functions that accept HTTP
requests aimed at particular URLs.

Flask will take the request, extract any important information it might have
in it, and make that information available inside the function.

The `return` statement of your function will be interpreted as HTML by the
user's browser. (Many tutorials also take advantage of Flask's extensions
to make it so you don't have to write all the HTML yourself.)

Here's an example:

    @app.route('/home')
    def home:
        return "<h1>Hello world!</h1>"

When the browser receives that HTTP response, the user then enters
information by typing data into an HTML form's input box, selecting a checkbox,
clicking on an option in a list, etc.

When a form is submitted (ie, the user does something in their browser that is
    considered a "submit" action for that form, like clicking a submit button),
the browser will put the filled-out form into an HTTP request and aim it at
the URL constructed by combining the URL snippet in the HTML form's definition
with your website's base name. This might look something like:

    <form href="/search">
plus
    https://yoursitename.pythonanywhere.com
equals
    https://yoursitename.pythonanywhere.com/search

It then sends the HTTP request back through the Internet to your web server
running Flask. Flask will take the request, extract the information from the
form, and make that available to the function that is configured to handle
that URL with a form in it.

The following example should be run with
    python3 flask_test_app.py
and accessed at
    http://localhost:5000/submit_demo
"""

from flask import Flask, request

app = Flask(__name__)


@app.route('/submit_demo', methods=['GET', 'POST'])
def submit():

    html_form = '''
        <form enctype="multipart/form-data" href="/submit_demo" method="POST">

            <input name="test_id">
                Type things in that box
            </input>

            <br>

            <button type="submit">
                Then click this button
            </button>

        </form>
    '''

    if request.method == 'GET':
        # Return only the basic HTML form.
        return html_form

    else:
        # Return the HTML form, but with the submitted data above it.
        submitted_data = request.form['test_id']
        return '''<h1>{}</h1> <br><br> {}'''.format(submitted_data, html_form)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
