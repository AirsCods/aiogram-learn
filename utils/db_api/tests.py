from utils.db_api.sqlite import DataBase

db = DataBase()


def test():
    db.create_table_users()
    db.add_user(1, 'First', 'email')
    db.add_user(2, 'Vasya', 'vg@gmail.com')
    db.add_user(3, 'Fedor')
    # db.add_user(4, 1, 1)
    db.add_user(5, 'John', 'john@mail.com')

    users = db.select_all_users()
    print('Пользователи:')
    print(*users)

    user = db.select_user(name='Vasya', id=2)
    print(f'Получил пользователя: {user}')

test()
