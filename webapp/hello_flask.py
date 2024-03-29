from flask import Flask, render_template, request
from vsearch import search_for_letters
from DBcm import UseDatabase

app = Flask(__name__)
app.config['dbconfig'] = {'host': '127.0.0.1',
                'user' : 'vsearch',
                'password' : 'KevinLee0!',
                'database' : 'vsearchDB',}

#log_request 는, vsearch.log 라는 파일의 내부에 req 와 res 를 단순 입력한다.
def log_request(req:'flask_request',res : str) ->None:

    dbconfig = {'host': '127.0.0.1',
                'user' : 'vsearch',
                'password' : 'KevinLee0!',
                'database' : 'vsearchDB',}
    with UseDatabase(app.config['dbconfig']) as cursor:
        _SQL = """insert into log
                        (phrase, letters, ip, browser_string, results)
                        values
                        (%s, %s, %s, %s, %s)"""
        cursor.execute(_SQL, (req.form['phrase'],
                              req.form['letters'],
                              req.remote_addr,
                              req.user_agent.browser,
                              res,))

@app.route('/search4', methods = ['POST'])
def do_search() ->'html':
    phrase = request.form['phrase']
    letters = request.form['letters']
    results = str(search_for_letters(phrase,letters))
    title = 'Here are your results'

    log_request(request,results)

    return render_template('results.html',
        the_phrase = phrase,
        the_letters = letters,
        the_title = title,
        the_results = results,
        )

@app.route('/viewlog')
def view_the_log() -> 'html':
    with UseDatabase(app.config['dbconfig']) as cursor:
        _SQL = """select phrase, letters, ip, browser_string, results from log"""

        cursor.execute(_SQL)
        contents = cursor.fetchall()

    titles = ('Phrase', 'Letters', 'Remote_addr','User_agent', 'Results')

    return render_template('viewlog.html',
                           the_title = 'View log',
                           the_row_titles = titles,
                           the_data = contents)

@app.route('/')
@app.route('/entry')
def entry_page() -> 'html':
    return render_template('entry.html',the_title='Welcome to search_for_letters on the web!')

if __name__ == '__main__':
    app.run(debug=True)
