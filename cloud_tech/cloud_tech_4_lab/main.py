from JsonOperator import JsonOperator
from flask import Flask, request

app = Flask(__name__)
json_operator = JsonOperator


@app.route('/get-users')
def call_all_users():
    return json_operator.get_all_users()


@app.route('/get-user-by-id')
def call_get_one_user():
    return json_operator.get_user_by_id(int(request.args.get('id')))


@app.route('/add-user', methods=['POST'])
def call_add_user():
    json_operator.insert_user_into_json(request.args.get('login'),
                                        request.args.get('password'),
                                        request.args.get('name'))
    return 'success'


@app.route('/delete-user', methods=['POST'])
def call_delete_user():
    json_operator.delete_user_by_id(int(request.args.get('id')))
    return 'success'


if __name__ == '__main__':
    app.run(debug=True)
