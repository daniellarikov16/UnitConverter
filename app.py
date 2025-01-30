from flask import *
app = Flask(__name__)
app.secret_key = 'dany_buster16'
def convert_values(value, convert_from, convert_to):
    convert_table = {'millimeter': 1,
                     'centimeter' : 10,
                     'meter' : 1000,
                     'kilometer' : 1000000,
                     'inch' : 25.4,
                     'foot' : 304.8,
                     'yard' : 914.4,
                     'mile' : 1609344,
                     'milligram' : 1,
                     'gram' : 1000,
                     'kilogram' : 1000000,
                     'ounce': 28349.5,
                     'pound' : 453592,
                     'celsius' : 1,
                     'fahrenheit' : -17.22,
                     'kelvin' : -272.15}
    value = float(value)
    if convert_from == 'celsius':
        if convert_to == 'fahrenheit':
            return (value * 9 / 5) + 32
        elif convert_to == 'kelvin':
            return value + 273.15
        else:
            return value
    elif convert_from == 'fahrenheit':
        if convert_to == 'celsius':
            return (value - 32) * 5 / 9
        elif convert_to == 'kelvin':
            return (value - 32) * 5 / 9 + 273.15
        else:
            return value
    elif convert_from == 'kelvin':
        if convert_to == 'celsius':
            return value - 273.15
        elif convert_to == 'fahrenheit':
            return (value - 273.15) * 9 / 5 + 32
        else:
            return value
    else:
        new_value = value / convert_table[convert_to]*convert_table[convert_from]
    return new_value

@app.route('/',methods=['GET', 'POST'])
def get_main():
        return render_template('index.html')
@app.route('/convert', methods = ['POST'])
def convert_lenght():
    try:
        session['my_value'] = float(request.form['value'])
        session['my_convert_from'] = request.form['from']
        session['my_convert_to'] = request.form['to']
    except ValueError:
        return "Ошибка: некорректное значение", 400
    return redirect (url_for('result'))
@app.route('/result', methods=['GET', 'POST'])
def result():
    value = session.get('my_value', None)
    convert_from = session.get('my_convert_from', None)
    convert_to = session.get('my_convert_to', None)
    new_value = convert_values(value,convert_from, convert_to)
    return render_template('result.html', value=value, convert_from=convert_from, convert_to=convert_to, new_value=new_value)
@app.route('/weight', methods=['GET', 'POST'])
def get_weight():
    return render_template('weight.html')
@app.route('/temperature', methods=['GET', 'POST'])
def get_temperature():
    return render_template('temperature.html')

if __name__ == '__main__':
    app.run(debug=True)