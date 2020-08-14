from app import create_app

application = create_app(config_name='base_config')

if __name__ == '__main__':
    application.run(debug=True, host='0.0.0.0', port=5000, use_reloader=True)
