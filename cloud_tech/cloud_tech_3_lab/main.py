from flask import Flask, render_template

app = Flask(__name__)


@app.route('/index')
def return_main():
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
