'''
Created on 2016-4-18
@author: Administrator
'''
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'hello world'
if __name__ == '__main__':
    app.run(debug = True)