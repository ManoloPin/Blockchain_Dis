from flask import Flask, jsonify, request
from blockchain import Block, Blockchain
import requests
import json
import time
"""--------------------------------------------------------------------------"""
    
app = Flask(__name__)

Blockchain = Blockchain()
Blockchain.create_genesis_block()

#direccion de miembros participantes

peers = set()

"""
agregar transaccion a la cadena de bloques
"""
@app.route('/new_transactions', methods = ['POST'])
def nueva_transaccion():

    values = request.get_json()
    required = ['sender', 'recipient', 'amount']

    if not all(k in values for k in required ):
    
        return "datos de transaccion invalidos ", 404
    
    index = Blockchain.add_new_transaction(values['sender'],values['recipient'],values['amount']) 

    response ={'menssage': f"La transacción se agregará al Bloque"}
    return jsonify(response), 201

"""
devuelve la copia del nodo de la cadena, consulta todas las publicacions a mostras
"""
@app.route('/chain', methods = ['GET'])
def get_chain():
    chain_data = []
    for block in Blockchain.chain:
        chain_data.append(block.__dict__)

    return json.dumps(
        {
        "length": len(chain_data),
        "chain": chain_data,
        "peers": list(peers)
        })

"""
solicitar trnasacciones no confirmadas para minar
"""
@app.route('/mine', methods = ['GET'])
def mine_transacciones():
    resultado = Blockchain.mine()# rectificar parametros de blockchain

    if not resultado:
        return "No hay transacciones para minar"
    else:
        #asegurar la cadena mas larga
        chain_length = len(Blockchain.chain) 
        consenso() # rectificar
        
        if chain_length == len(Blockchain.chain):
            #anunciar el bloque extraído recientemente a la red
            anunciar_new_block(Blockchain.last_block.index) # rectificar

        return "Block #{} esta minado.".format(Blockchain.last_block.index)

"""
agregar nuevos pares o (peers) a la red blockchain
"""
@app.route('/registrar_nodo', methods = ['POST'])
def registrar_nuevos_pares():
    direccion_nodo = request.get_json()["direccion_nodo"]
    if not direccion_nodo:
        return "dato invalido", 400

    """
    agregar el nodo a la lista de pares y devolver la cadena de bloques al nodo recien creado  para sincronizar
    """
    peers.add(direccion_nodo)
    return get_chain()
#________________________________________________________________-
@app.route('/registrar_con', methods=['POST'])
def registrar_con_nodo_existente():
    """
    funcion para registrar el nodo actual con el nodo especficado en el 
    solicitar y sincronizar la cadena de bloques.
    """
    direccion_nodo = request.get_json()["direccion_nodo"]
    if not direccion_nodo:
        return "dato invalido", 400

    data = {"direccion_nodo": request.host_url}
    headers = {'Content-Type': "application/json"} # rectificar funcion


    """
    hacer una solicitud  para registrar con el nodo remoto y obtenet información
    """
    respuesta = requests.post(direccion_nodo + "/registrar_nodo",
                             data=json.dumps(data), headers=headers) # rectificar

    if respuesta.status_code == 200:
        global Blockchain
        global peers #pares

        # actualizar la cadena y los pares
        chain_papelera = respuesta.json()['chain']
        blockchain = crear_chain_desde_papelera(chain_papelera)
        peers.update(respuesta.json()['peers'])#rectificar
        return "Registro exitoso", 200
    else:
        #si algo sale mal agregar a la respuesta del API
        return respuesta.content, respuesta.status_code


def crear_chain_desde_papelera(chain_papelera):
    generar_blockchain = Blockchain()
    generar_blockchain.create_genesis_block()
    for idx, block_data in enumerate(chain_papelera):
        if idx == 0:
            continue  # omitir el bloque genesis
        block = Block(block_data["index"],
                      block_data["transactions"],
                      block_data["timestamp"],
                      block_data["previous_hash"],
                      block_data["nonce"])
        prueba = block_data['hash']
        adicional = generar_blockchain.add_block(block, prueba)
        if not adicional:
            raise Exception("la papelera de la cade esta manipulada !")
    return generar_blockchain


"""
agregar un bloque extraido a la cadena del nodo. el bloaque primero se 
verifica por el nodo y luego si se agraga a la cadena 
"""
@app.route('/añadir_block', methods=['POST'])
def verificar_agregar_block():
    block_data = request.get_json()
    block = Block(block_data["index"],
                  block_data["transactions"],
                  block_data["timestamp"],
                  block_data["previous_hash"],
                  block_data["nonce"])

    prueba = block_data['hash']
    adicional = Blockchain.add_block(block,prueba)

    if not adicional:
        return "El bloque fue descartado por el nodo", 400

    return "Bloque agregado a la cadena", 201

"""consultar transacciones no confirmadas"""
@app.route('/pendiente_tx')
def get_pendiente_tx():
    return json.dumps(Blockchain.unconfirmed_transactions) 
    """rectificar """#gsjhdsjdsdjsdhjsjh----------------------------------


def consenso():
    """
    si se encuentra una cadena mas larga la cadena se remplaza por la mas larga
    """
    global Blockchain

    longest_chain = None
    current_len = len(Blockchain.chain)

    for nodo in peers:
        response = requests.get('{}chain'.format(nodo))
        length = response.json()['length']
        chain = response.json()['chain']
        if length > current_len and Blockchain.check_chain_validity(chain):
            current_len = length
            longest_chain = chain

    if longest_chain:
        blockchain = longest_chain
        return True

    return False


def anunciar_new_block(block):
    """
    funcion para anunciar a la red que se ha extraido un bloque. otros bloques pueden 
    verificar la prueba de trabajo y agragarla a su cadena respectiva
    """
    for peer in peers:
        url = "{}añadir_block".format(peer)
        headers = {'Content-Type': "application/json"}
        requests.post(url,
                      data=json.dumps(block.__dict__, sort_keys=True),
                      headers=headers)

"""-------------------------------------------------"""
if __name__ == '__main__':
    app.run(debug=True, port = 5000)