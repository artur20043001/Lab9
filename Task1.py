from flask import Flask, render_template, url_for, redirect, request
import sqlalchemy as db




def searchdd(serchText):

    select_query = db.select(cities).where(cities.columns.town == serchText)
    select_result = connection.execute((select_query))
    searchCity =select_result.fetchall()
    if len(searchCity) ==0:
        select_query = db.select(cities).where(cities.columns.visit_date == serchText)
        select_result = connection.execute((select_query))
        searchBook = select_result.fetchall()
    return searchCity


app = Flask(__name__)


try:
    engine = db.create_engine('mysql+pymysql://root:ason121245@localhost:3306/my_database')
    connection = engine.connect()
    print("Connect DB")
except Exception as ex:
    print("ERROR Connect DB")
    print(ex)

metadata = db.MetaData()
phonebook = db.Table('phonebook', metadata,
                 db.Column('number_id', db.Integer, primary_key=True),
                 db.Column('name', db.Text),
                 db.Column('number', db.Text))

metadata.create_all(engine)

insertion_query = phonebook.insert().values([
    {"name":"Артур Искандаров", "number":"+79991234567"},
    {"name":"Артемий Ковалев", "number":"+79996667788"},
    {"name":"Кирилл Петров", "number":"+79994567890"},
    {"name":"Андрей Морозов", "number":"+79996543210"},
    {"name":"Ольга Иванова", "number":"+79998877666"},
    {"name":"Илья Николаев", "number":"+79992100999"},
    {"name":"Юлия Григорьева", "number":"+79994445566"},
    {"name":"Денис Крылов", "number":"+79991112233"},
    {"name":"Екатерина Лебедева", "number":"+79997778899"},
    {"name":"Данил Кузнецов", "number":"+79993334455"},



])
#connection.execute(insertion_query)

selall = db.select(phonebook)
selres = connection.execute(selall)
allNumber = selres.fetchall()

@app.route('/', methods =["GET", "POST"])
def index():
    if request.method == "POST":
        if request.form.get('clear') =='Clear':
            d = searchdd("s")
            return render_template('index.html', allNumber=d, len=len(d))
        elif request.form.get('all') =='All List':
            render_template('index.html' , allNumber = allNumber, len = len(allNumber))
        elif request.form.get('searchBtn') == 'Search':
            a = request.form.get("search")
            d = searchdd(a)
            return render_template('index.html' , allNumber = d, len = len(d))
    return render_template('index.html' , allNumber = allNumber, len = len(allNumber))

if __name__ == '__main__':
    app.run(debug=True, port=5001 )