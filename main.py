from flask import render_template, flash, redirect, url_for, make_response, request
from flask import Flask
app = Flask(__name__)

@app.route('/setsession', methods = ['GET', 'POST'])
def setsession():
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('index'))
    return '''
         <form action="" method="POST">
         <p><input type="text" name="username"></p>
         <p><input type="submit" value="Login"></p>
         </form>
    '''
@app.route('/unsetsession')
def unsetsession():
    session.pop('username', None)
    return redirect(url_for('index'))
    
app.secret_key = 'SOME SECRET'
@app.route('getcookie')
def getcookie():
    flask_cookie = request.cookies.get('flask_cookie')
    return '<h1>Cookie: ' + flask_cookie + '</h1>'


@app.route('/')
@app.route('/index')
def index():
    if 'username' in session:
        return '<h1>Session %s</h1>' % session['username']
    return '<h1>No session!</h1>'
    
    
    
    user = {'username' : 'Максим'}
    
    posts = [
            {
                     'author': {'username': 'Михаил'},
                     'body'  : 'Hello!'
            },
            {
                     'author': {'username': 'Иван'},
                     'body'  : 'Как дела?'
            },
            {
                     'author': {'username': 'Юрий'},
                     'body'  : 'Рад вас видеть!'
            }
    ]
    
if __name__ == "__main__":
    app.run()
