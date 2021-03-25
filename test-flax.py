from flask import Flask
app = Flask(__name__)
"""
this one prints Hello world
"""
@app.route('/')
def hello():
    return "Hello Ravi!"

if __name__ == '__main__':
    app.run()

'''
Another comment
'''
