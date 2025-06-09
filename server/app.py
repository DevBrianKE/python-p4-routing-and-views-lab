from flask import Flask

# Create Flask application instance
app = Flask(__name__)

@app.route('/')
def index():
    """Home route that returns an h1 heading"""
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<string:parameter>')
def print_string(parameter):
    """Prints the parameter to console and returns it"""
    print(parameter)  # Prints to console (server side)
    return parameter  # Returns to browser (client side)

@app.route('/count/<int:parameter>')
def count(parameter):
    """Returns numbers from 0 to parameter-1, each on a new line"""
    numbers = '\n'.join(str(num) for num in range(parameter)) + '\n'
    return numbers

@app.route('/math/<int:num1>/<string:operation>/<int:num2>')
def math(num1, operation, num2):
    """Performs math operations based on URL parameters"""
    result = None
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == 'div':
        result = num1 / num2
    elif operation == '%':
        result = num1 % num2
    else:
        return 'Invalid operation', 400
    
    return str(result)

if __name__ == '__main__':
    app.run(port=5555, debug=True)