from flask import Flask
from flask import render_template, flash, redirect
from config import Config, DevelopmentConfig
from .forms import LoginForm

app = Flask(__name__)
app.config.from_object(Config)

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Enzo'}
    posts = [
        {
            'author': {'username': 'Lucas Pierre'},
            'body': 'Flask é sensacional'
        },
        {
            'author': {'username': 'Rayssa Garcia'},
            'body': 'Eu amo dar aulas de inglês'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash(f'Login requested for user {form.username.data}, remember_be={form.remember_me.data}')
        return redirect('/index')
    return render_template('login.html', title='Sign In', form=form)

@app.route('/user/<user>')
def user(user):
    return f'<h1 style="color: blue;"> {user} </h1>'

@app.route('/user/<int:id>')
def user_id(id):
    return f'<h1 style="color: red;"> {id} </h1>'


