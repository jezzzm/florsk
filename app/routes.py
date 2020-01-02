from app import app
from flask import render_template

@app.route('/')
@app.route('/index')
def index():
  user = {'username': 'Jez'}
  title= 'Home'
  posts = [
    {
      'author': {'username': 'Jez'},
      'body': 'test jez article'
    },
    {
      'author': {'username': 'Jez'},
      'body': 'yet another Jez test'
    }
  ]
  return render_template('index.html', title=title, user=user, posts=posts)
  