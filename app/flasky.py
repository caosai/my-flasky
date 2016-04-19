'''
Created on 2016-4-18
@author: Administrator
'''
from flask import Flask
from flask import redirect
from flask import render_template
from flask.ext.bootstrap import Bootstrap
from flask.ext.moment import Moment
from datetime import datetime
from flask.ext.wtf import Form
from wtforms import  StringField, SubmitField
from wtforms.validators import Required
from wsgiref.validate import validator


app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'
bootstrap = Bootstrap(app)
moment = Moment(app)

@app.route('/',methods = ['GET','POST'])
def index():
    name = None
    form = NameForm()
    if form.validate_on_submit():
        name = form.name.data
        form.name.data = ''
    return render_template("index.html" , name=name,form=form,current_time=datetime.utcnow())

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



class NameForm(Form):
    name = StringField('What is your name?',validators = [Required()])
    submit = SubmitField('Submit')


if __name__ == '__main__':
    app.run(debug = True)