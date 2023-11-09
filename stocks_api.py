# Sarah Ma
# Lab 7 - Web Applications

from flask import Flask
from flask import request
import requests 

app = Flask(__name__)
app.debug = True

def getStock(symbol):
    baseURL = 'https://www.alphavantage.co/query?function=GLOBAL_QUOTE&datatype=csv'
    keyPart = '&apikey=' + "APIKEY"
    symbolPart = '&symbol=' + symbol
    stockResponse = requests.get(baseURL+keyPart+symbolPart)
    return stockResponse.text  #Return only text part of response

@app.route('/')
def html():
    html = ''
    html += '<html>\n'
    html += '<body>\n'

    html += '<form method="POST" action="user_input">\n'
    html += 'Stock symbol: <input type="text" name="stock_symbol" /><br>\n'


    # Opening Price
    html += '<input type="checkbox" id="openingprice" name="openingprice" value="Opening Price">\n'
    html += '<label for="openingprice"> Opening Price</label><br>\n'

    # High 
    html += '<input type="checkbox" id="high" name="high" value="High">\n'
    html += '<label for="high"> High</label><br>\n'

    # Low
    html += '<input type="checkbox" id="low" name="low" value="Low">\n'
    html += '<label for="low"> Low</label><br>\n'

    # Current Price
    html += '<input type="checkbox" id="currentprice" name="currentprice" value="Current Price">\n'
    html += '<label for="currentprice"> Current Price</label><br>\n'


    # Submit Button
    html += '<input type="submit" value="Submit">\n'

    html += '</body>\n'
    html += '</html>\n'
    html += '</form>'

    return html

@app.route('/user_input', methods=['POST'])
def get_stock_data():
    # Get the stock symbol the user entered
    stock_symbol = request.form['stock_symbol']
    # Use the stock symbol to get the stock data
    stock_data = getStock(stock_symbol)

    # Since the first line of the stock data isn't the actual data this skips the first line
    stock_lines = stock_data.split('\n')
    # Splits the second line by commas
    stock_info = stock_lines[1].split(',')

    # Check if stock data is found
    if "Error Message" in stock_data:
        error = f"Stock symbol '{stock_symbol}' does not exist."
        return error

    html = ''
    html += '<html>\n'
    html += '<body>\n'
    html += f'Stock value for {stock_symbol} is as follows: <br>\n'

    # Checks if the user checked certain boxes and if they did display those certain things
    if request.form.get('openingprice'):
        html += f'Opening Price: {stock_info[1]}<br>\n'
    if request.form.get('high'):
        html += f'High: {stock_info[2]}<br>\n'
    if request.form.get('low'):
        html += f'Low: {stock_info[3]}<br>\n'
    if request.form.get('currentprice'):
        html += f'Current Price: {stock_info[4]}<br>\n'

    # Back Button
    html += '<a href="/">Back</a>\n'

    html += '</body>\n'
    html += '</html>\n'
    return html

if __name__ == '__main__':
    app.run()
