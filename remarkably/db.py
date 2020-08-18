from datetime import datetime

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


# for DB seed purposes
def get_move_out_seed():
    roles_seed = [(2, datetime(2020, 8, 15, 13, 00, 00)),
                  (3, datetime(2020, 8, 16, 13, 00, 00)),
                  (5, datetime(2020, 8, 17, 13, 00, 00)),
                  (23, datetime(2020, 8, 18, 13, 00, 00))
                  ]
    return roles_seed


def insert_seed_data(connection):
    # MOVE OUT
    sql = "INSERT INTO public.moveout (value, created_date) VALUES (%s, %s)"
    for values in get_move_out_seed():
        connection.execute(sql, values)
