from flask import Flask, render_template
from flask_restful import Api
from src.PresentationLayer.Controlers import IncedentControler
from src.PresentationLayer.IncedentControlerGet import IncedentControlerGet


app = Flask(__name__, template_folder='../resources/templates/', static_folder='../resources/static')
api = Api(app)


@app.route('/')
def homePageRender():
    return render_template('index.html')


@app.route('/addincedentdash')
def addIncedentRender():
    return render_template('incedentAdd.html')


@app.route('/incedentlist')
def incedentListRender():
    return render_template('incedentList.html')


api.add_resource(IncedentControler, '/postincedent')
api.add_resource(IncedentControlerGet, '/getlist')
api.init_app(app)


if __name__ == '__main__':
    app.run()
