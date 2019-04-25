from flask import Flask, request, render_template, flash, redirect
from db import db
from db_setup import *
from forms import *
from models import *
from tables import *
# from SI507project_tools import get_itunes_media, populate_data_into_db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///allstateparks_info.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = "super secret key"
db.init_app(app)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/all')
def all():
    all_parks = Park.query.all()
    all_parks_str= list(map(lambda x: str(x), all_parks))
    return render_template('all.html', results = all_parks)

@app.route('/allstateinfo')
def allstateinfo():
    all_states = State.query.all()
    all_states_str= list(map(lambda x: str(x), all_states))
    return render_template('allstates.html', lists = all_states)


@app.route('/search', methods=['GET'])
def search():
    search = ParkSearchForm(request.form)
    return render_template('searchform.html', form=search)

@app.route('/table', methods=['GET'])
def table():
    table = ParkSearchForm(request.form)
    if request.method == 'GET':
        return table_results(table)

def table_results(search):
    results = []
    search_string = search.data['search']
    if search_string:
        if search.data['select'] == 'Name':
            qry = session.query(Park).filter(
                Park.Name.contains(search_string))
            results = [item[0] for item in qry.all()]
        elif search.data['select'] == 'Descr':
            qry = session.query(Park).filter(
                Park.Descr.contains(search_string))
            results = qry.all()
        elif search.data['select'] == 'Location':
            qry = session.query(Park).filter(
                Park.Location.contains(search_string))
            results = qry.all()
    else:
        qry = session.query(Park)
        results = qry.all()

    if not results:
        flash('No results found!')
        return redirect('/')
    else:
        # display results
        table = Results(results)
        table.border = True
    return render_template('results.html', table=table)

#
#
# @app.route('/searchresult')
# def after_search():
#     if request.method == 'GET':
#         keyword = request.args.get('keyword')
#         no = request.args.get('no')
#         keyword = keyword if keyword else 'Born this way'
#         no = no if no else 10  # use 10 as default value
#         media_data = get_itunes_media(keyword, no)
#         populate_data_into_db(media_data['results'])  # call those two funcs from tools.py
#         return render_template('searchresult.html',
#             keyword = keyword,
#             results = media_data['results'])
#     return '<h1>Please use the form to visit this link</h1>'  # just in case user use another request method

if __name__ == '__main__':
    app.run(port=5000, debug=True)
