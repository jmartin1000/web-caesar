from flask import Flask, request

app = Flask(__name__)
app.config['DEBUG'] = True

form = """
<!DOCTYPE html>
<html>
    <head>
        <style>
            form {
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }
            textarea {
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }
        </style>
    </head>
    <body>
        <form action="/hello" method="post">
            <label>Rotate by:
                <input type="number" value=0 name="rot"/>
            </label>
            <textarea name="secret"></textarea>
            <input type="submit" value="Submit Query"/>
        </form>
    </body>
</html>
"""

@app.route("/")
def index():
    return form

@app.route("/hello", methods=['POST'])
def hello():
    #first_name = request.args.get('first_name')
    first_name = request.form['first_name']
    return '<h1>Hello, ' + first_name + '</h1>'

    
app.run()