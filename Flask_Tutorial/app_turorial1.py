from flask import Flask,request

app = Flask(__name__)

@app.route('/')
def index():
    return "<h1>Hello world</h1>"

@app.route('/hello')
def hello():
    # return "Hello World\n" , 201 (mean CREATED)
    # return "Hello World\n" , 202 (mean Accepted)
    # return "Hello World\n" , 404 (mean Not found)
    # return "Hello World\n" , 500 (mean Internal Server Error)
    # return "Hello World\n" , 501 (mean Not Implemented)
    # return "Hello World\n" , 936 (mean Unknow)
    return "Hello World\n" 

@app.route('/greet/<name>')
def greet(name):
    return f"Hello {name}"

@app.route('/add/<int:number1>/<int:number2>')
def add(number1, number2):
    return f'{number1} + {number2} = {number1 + number2}'

@app.route('/handle_url_params')
def handle_params():
    if 'greeting' in request.args.keys() and 'name' in request.args.keys():
        greeting = request.args['greet']
        name = request.args['greeting']
        return f'{greeting}, {name}'
    else:
        return 'Some parameters are missing'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5555, debug=True)