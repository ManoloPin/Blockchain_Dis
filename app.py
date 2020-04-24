from flask import Flask, jsonify, Request

app = Flask(__name__)

from  products import products # importacion 

@app.route('/ping')
def ping(): # coneccion de envio
    return ({"message": "pong1"}) # enviar json 

@app.route('/products', methods = ['GET']) # NO ES NECESARIO PONER METODO GET YA QUE LO  HACE POR DEFECTO 
def getProducts():
    return jsonify({"products": products, "menssage": "products list"})

@app.route('/products/<string:product_name>')
def getproduct(product_name):
    productsFound = [product for product in products if product ['name'] == product_name]
    if (len(productsFound) > 0):
        return jsonify({"product": productsFound[0]})
    return jsonify({"message": " Product not found"})

#ruta para crear datos 
@app.route('/products', methods = ['POST'])
def addProduct():# recivir los datos que envia el cliente 
    new_product = { # almacenar producto recivido
        "name" : Request.json['name'],
        "price": Request.json['price'],
        "quantity": Request.json['quantity']
    }
    products.append(new_product)
    return 'received'

if __name__ == '__main__':
    app.run(debug=True, port = 5000)