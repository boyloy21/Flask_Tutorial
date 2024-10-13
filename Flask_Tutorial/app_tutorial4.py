from flask import Flask, request, render_template

app = Flask(__name__, template_folder='template', static_folder='static', static_url_path='/')

@app.route('/')
def index():
    return render_template('index3.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)