from flask import Flask, render_template, url_for, redirect, request
import sqlalchemy as db

def searchdd(serchText):

    select_query = db.select(games).where(names.columns.name == serchText)
    select_result = connection.execute((select_query))
    searchGemas =select_result.fetchall()
    if len(searchGemas) ==0:
        select_query = db.select(games).where(names.columns.number == serchText)
        select_result = connection.execute((select_query))
        searchGemas = select_result.fetchall()
    return searchGemas


app = Flask(__name__)


try:
    engine = db.create_engine('mysql+pymysql://root:ason121245@localhost:3306/my_database')
    connection = engine.connect()
    print("Connect DB")
except Exception as ex:
    print("ERROR Connect DB")
    print(ex)

metadata = db.MetaData()
names = db.Table('names', metadata,
                 db.Column('name', db.Text),
                 db.Column('number', db.Integer))

metadata.create_all(engine)

insertion_query = games.insert().values([
    {"name":"Федя", "number":89810949841},
    {"name":"Илья", "number":8917313811},
    {"name":"Андрей", "number":89173183133},
    {"name":"Саня", "number":81931783112},
    {"name":"Олег", "number":8917371831},
    {"name":"Данил", "number":8917371313},
    {"name":"Борис", "number":8913871381},
    {"name":"Юля", "number":8913718931},
    {"name":"Даша", "number":8913719388},
    {"name":"Настя уник", "number":8913819310},
    {"name":"Настя челябинск", "number":89138193818},
    {"name":"Мама", "number":89137813819},
    {"name":"Папа", "number":8371838192},
])
#connection.execute(insertion_query)

selall = db.select(games)
selres = connection.execute(selall)
allnames = selres.fetchall()

@app.route('/', methods =["GET", "POST"])
def index():
    if request.method == "POST":
        if request.form.get('clear') =='Clear':
            d = searchdd("s")
            return render_template('index.html', allnames=d, len=len(d))
        elif request.form.get('all') =='All List':
            render_template('index.html' , allnames = allnames, len = len(allnames))
        elif request.form.get('searchBtn') == 'Search':
            a = request.form.get("search")
            d = searchdd(a)
            return render_template('index.html' , allnames = d, len = len(d))
    return render_template('index.html' , allGames = allnames, len = len(allnames))

if __name__ == '__main__':
    app.run(debug=True, port=5001 )



