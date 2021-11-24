from flask import Flask, session, request
from checker import check_logged_in


app = Flask(__name__)
app.secret_key = 'KevinLee0!'


@app.route('/')
def home() -> str:
    return 'welcome to hell'


@app.route('/page1')
@check_logged_in
def page1() -> str:
    return 'This is page1'


@app.route('/login')
def do_login() -> str:
    session['logged_in'] = True
    return 'You are now logged in'


@app.route('/logout')
def do_logout() -> str:
    session.pop('logged_in')
    return 'You are now logged out'


if __name__ == '__main__':
    app.run(debug=True)

