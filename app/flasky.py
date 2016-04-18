'''
Created on 2016-4-18
@author: Administrator
'''
from flask import Flask
from flask import redirect
from flask import render_template
from flask.ext.bootstrap import Bootstrap

app = Flask(__name__)

@app.route('/')
def index():
    return 'hello world'

@app.route('/redirect')
def redir():
    return redirect("http://baidu.com")

@app.route('/user/<name>')
def user(name):
    return render_template("user.html", name = name)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500


if __name__ == '__main__':
    app.run(debug = True)