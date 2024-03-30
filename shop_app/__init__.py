from flask import Flask


app = Flask(__name__)

# RUN FLASK APP
if __name__ == "__main__":
    app.run(debug=True)