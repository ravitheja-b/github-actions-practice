from flask import Flask
app = Flask(__name__)
"""
this one prints Hello world
"""
@app.route('/')
def hello():
    return "Hello World!"

if __name__ == '__main__':
    app.run()
