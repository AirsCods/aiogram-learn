import sqlite3
from typing import Union


def logger(statement):
    print(f'''
    -------------------------------------------------------------------
    Executing:
    {statement}

    -------------------------------------------------------------------
    ''')


class DataBase:
    def __init__(self, path_to_dp='data/main.db'):
        self.path_to_db = path_to_dp

    @property
    def connection(self):
        return sqlite3.connect(self.path_to_db)

    def execute(self, sql: str, parameters: tuple = None,
                fetchone=False, fetchall=False, commit=False) -> Union[None | tuple]:

        if not parameters:
            parameters = tuple()
        data = None

        connection = self.connection
        connection.set_trace_callback(logger)
        cursor = connection.cursor()
        cursor.execute(sql, parameters)

        if commit:
            connection.commit()
        if fetchone:
            data = cursor.fetchone()
        if fetchall:
            data = cursor.fetchall()

        connection.close()
        return data

    def create_table_users(self):
        sql = '''
        CREATE TABLE Users (
        id int NOT NULL,
        name varchar(255) NOT NULL,
        email varchar(255),
        PRIMARY KEY (id)
        );
        '''
        self.execute(sql=sql, commit=True)

    def add_user(self, id: int, name: str, email: str = None):
        sql = 'INSERT INTO Users(id, name, email) VALUES(?, ?, ?);'
        parameters = (id, name, email)
        self.execute(sql=sql, parameters=parameters, commit=True)

    def select_all_users(self):
        sql = 'SELECT * FROM Users;'
        return self.execute(sql=sql, fetchall=True)

    @staticmethod
    def format_args(sql, parameters: dict):
        sql += ' AND '.join([f'{item} = ?' for item in parameters.keys()])
        sql += ';'
        return sql, tuple(parameters.values())

    def select_user(self, **kwargs):
        sql = 'SELECT * FROM Users WHERE '
        sql, parameters = self.format_args(sql, kwargs)

        return self.execute(sql=sql, parameters=parameters, fetchone=True)

    def count_users(self):
        return self.execute(sql='SELECT COUNT(*) FROM USERS;', fetchone=True)

    def update_email(self, email, id):
        sql = 'UPDATE Users SET email=? WHERE id=?;'
        return self.execute(sql=sql, parameters=(email, id), commit=True)

    def delete_users(self):
        self.execute(sql='DELETE FROM Users WHERE TRUE;')
