from flask import Flask, Response, request, render_template
# from forms import BasicForm

app = Flask(__name__)


@app.route('/')
@app.route('/home')
def homePage():
    return render_template('layout.html', title='Home')


@app.route('/subscribe')
def subscribe():
    return render_template('subscribe.html', title='Subscribe')


# @app.route('/subscribe', methods=['GET','POST'])
# def register():
#     error = ""
#     form = BasicForm()
#
#     if request.method == 'POST':
#         first_name = form.first_name.data
#         last_name = form.last_name.data
#
#         if len(first_name) == 0 or len(last_name) == 0:
#             error = "Please enter your first name and last name. These fields cannot be empty."
#         else:
#             return 'Thank you!'
#
#     return render_template('subscribe.html', title='Subscribe')


if __name__ == "__main__":
    app.run(debug=True)

# @app.route('/hello')
# def hello_from_flask():
#     return "Hello from Flask!"
#
#
# @app.route('/get/text')
# def get_text():
#     return Response("Hello from Flask using an explicit Response object", mimetype='text/plain')
#
#
# @app.route('/post/text', methods=['POST'])
# def post_text():
#     data_sent = request.data.decode('utf-8')
#     return Response("You posted this data to the Flask app: " + data_sent, mimetype='text/plain')
#
#
# @app.route('/page/<name>')
# def say_hello_page(name):
#     return """
# <html>
# <head>
#     <title>Sample - Flask routes</title>
# </head>
# <body>
#     <h1>Name Page</h1>
#     <p>Hello {}!</p>
# </body>
# </html>
# """.format(name)




#



