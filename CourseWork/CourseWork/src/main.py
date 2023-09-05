from flask import Flask, render_template, session
from flask_restful import Api
from src.controlers.controlers import RegistrationControler, LoginControler


app = Flask(__name__, template_folder='../resources/templates', static_folder='../resources/static')
api = Api(app)


@app.route('/')
def return_index():
    return render_template('index.html')


@app.route('/login')
def return_login_page():
    return render_template('loginPage.html')


@app.route('/profile')
def return_login():
    return render_template('profile.html')


@app.route('/register')
def return_register():
    return render_template('registerPage.html')


@app.route('/car-list')
def return_carList():
    return render_template('carList.html')


@app.route('/add-car')
def add_car():
    return render_template('addCarToList.html')


@app.route('/service-station-list')
def return_service_station_list():
    return render_template('serviceStationList.html')


@app.route('/service-station-profile')
def return_service_station_profile():
    return render_template('serviceStationProfile.html')


app.secret_key = '647ccde280ecfd0d18295abb'
api.add_resource(RegistrationControler, '/registrationUser')
api.add_resource(LoginControler, '/postLogin')
if __name__ == "__main__":
    app.run()
