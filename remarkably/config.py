class BaseConfig(object):
    DEBUG = True
    DEVELOPMENT = True

    # postgres
    POSTGRES = {
        'user': 'postgres',
        'pw': 'password',
        'db': 'remarkably_db',
        'host': 'remarkably_db',
        'port': '5432',
    }

    SQLALCHEMY_DATABASE_URI = 'postgresql://%(user)s:%(pw)s@%(host)s:%(port)s/%(db)s' % POSTGRES

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    SECRET_KEY = 'x-rmb-eventscv-token'


app_config = {
    "base_config": "config.BaseConfig"
}
