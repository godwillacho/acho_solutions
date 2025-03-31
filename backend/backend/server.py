from flask import Flask,request , jsonify
import products_dao
from sql_connection import get_sqlconnection

app = Flask(__name__)

connection = get_sqlconnection()

@app.route('/getproducts/', methods=['GET'])

def getproducts():
    products = products_dao.display_all_products(connection)
    response = jsonify(products)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response 

if __name__ == '__main__':
    print('starting python flask Server for Grocery store Management system ')
    app.run(port=5000)