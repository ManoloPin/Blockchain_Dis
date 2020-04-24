from flask import Flask, jsonify

app = Flask(__name__)

from  products import products

@app.route('/ping')
def ping(): # coneccion de envio
    return ({"message": "pong1"}) # enviar json 

@app.route('/products', methods = ['GET']) # NO ES NECESARIO PONER METODO GET YA QUE LO  HACE POR DEFECTO 
def getProducts():
    return jsonify({"products": products, "menssage": "products list"})

@app.route('/products/<string:product_name>')
def getproduct(product_name):
    productsFound = [product for product in products if product ['name'] == product_name]
    return jsonify({"product": productsFound})



if __name__ == '__main__':
    app.run(debug=True, port = 5000)