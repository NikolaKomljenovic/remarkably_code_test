class BaseConfig(object):
    # postgres
    POSTGRES = {
        'user': 'postgres',
        'pw': 'password',
        'db': 'remarkably_db',
        'host': 'localhost',
        'port': '5431',
    }

    SQLALCHEMY_DATABASE_URI = 'postgresql://%(user)s:%(pw)s@%(host)s:%(port)s/%(db)s' % POSTGRES

    SQLALCHEMY_TRACK_MODIFICATIONS = False


app_config = {
    "base_config": "config.BaseConfig"
}
