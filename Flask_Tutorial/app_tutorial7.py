from blueprintapp.app import create_app

flask_app = create_app()

if __name__ == '__name__':
    flask_app.run(host='0.0.0.0', debug=True)