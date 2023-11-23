import json


class JsonOperator:

    @staticmethod
    def read_json() -> dict:
        with open('users.json', 'r') as file:
            json_data = json.load(file)
            return json_data

    @staticmethod
    def write_json(json_data: dict) -> None:
        with open('users.json', 'w') as json_file:
            json.dump(json_data, json_file, indent=2)

    @staticmethod
    def get_list_users_length() -> int:
        json_data = JsonOperator.read_json()
        return len(json_data['users'])

    @staticmethod
    def insert_user_into_json(login: str, password: str, name: str) -> None:
        json_data = JsonOperator.read_json()
        json_data['users'].append({'id': JsonOperator.get_list_users_length(),
                                   'login': login, 'password': password, 'name': name})
        JsonOperator.write_json(json_data)

    @staticmethod
    def get_all_users():
        json_data = JsonOperator.read_json()
        return json_data['users']

    @staticmethod
    def get_user_by_id(id: int) -> dict:
        json_data = JsonOperator.read_json()
        for user in json_data['users']:
            if user['id'] == id:
                return user

    @staticmethod
    def delete_user_by_id(id: int) -> None:
        json_data = JsonOperator.read_json()
        users_list = json_data['users'].copy()
        for user in users_list:
            if user['id'] == id:
                user_list_position = users_list.index(user)
                users_list.pop(user_list_position)
                json_data['users'] = users_list
                JsonOperator.write_json(json_data)
