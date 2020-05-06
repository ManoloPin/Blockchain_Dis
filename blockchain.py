from hashlib import sha256
from flask import Flask, request
import json
import time

"""--------------------------------------------------------------------------"""
class Block:
    def __init__(self, index, transacciones, timestamp, previous_hash, nonce=0):
        self.index = index # Id unico del bloque
        self.transacciones = transacciones # Lista de Transacciones
        self.timestamp = timestamp # Tiempo en generacion del bloque
        self.previous_hash = previous_hash # Hash del bloque anterior de la cadena
        self.nonce = nonce # Prueba que se ha realizado un cambio para obtener el hashs

    def compute_hash(self): # Funcion que devuelve el hash del contenido del bloque.
        block_string = json.dumps(self.__dict__, sort_keys=True)
        return sha256(block_string.encode()).hexdigest()
"""---------------------------------------------------------------------------"""
class Blockchain:

    difficulty = 2 # Dificultad del algoritmo hash

    def __init__(self):
        self.unconfirmed_transactions = []
        self.chain = []

    def create_genesis_block(self): #Esta funcion es para generar el bloque de genesis y lo agrega a la cadena

        genesis_block = Block(0, [], 0, "0") # El bloque tiene el indice 0, previo al hash como 0 y un hash valido
        genesis_block.hash = genesis_block.compute_hash()
        self.chain.append(genesis_block)

    @property
    def last_block(self): # Ultimo bloque
        return self.chain[-1] # retornar a la cadena

    def add_block(self, block, Prueba): # La funcion que agrega el bloque a la cadena despues de la verificacion

        previous_hash = self.last_block.hash # Comprueba si la prueba es valida

        # Verifica que el hash anterior del bloque y del hash del ultimo bloque
        if previous_hash != block.previous_hash:  
            return False

        if not Blockchain.is_valid_Prueba(block, Prueba):  
            return False

        block.hash = Prueba
        self.chain.append(block)
        return True

    @staticmethod # Funcion que intenta diferentes valores de nonce para tener un hash
    def Prueba_de_trabajo(block): 
        block.nonce = 0

        computed_hash = block.compute_hash() # Calcula el hash y la del bloque
        while not computed_hash.startswith('0' * Blockchain.difficulty):
            block.nonce += 1
            computed_hash = block.compute_hash()

        return computed_hash

    def add_new_transaction(self,sender, recipient, amount):

        self.unconfirmed_transactions.append({
            'sender': sender,
            'recipient': recipient, 
            'amount': amount,
            }
            )
        

    @classmethod # Comprueba si el bloque del hash es valido donde valida los criterios de la dificultad
    def is_valid_Prueba(cls, block, block_hash): 

        return (block_hash.startswith('0' * Blockchain.difficulty) and block_hash == block.compute_hash())

    @classmethod  # Elimina el campo hash para volver a calcular el hash
    def check_chain_validity(cls, chain):
        resultado = True
        previous_hash = "0"

        for block in chain:
            block_hash = block.hash 
            delattr(block, "hash")

            if not cls.is_valid_Prueba(block, block_hash) or \
                    previous_hash != block.previous_hash:
                resultado = False
                break

            block.hash, previous_hash = block_hash, block_hash

        return resultado

    def mine(self): # Esta funcion sirve como interfaz para agregar la transaccion a la cadena de bloques y minarlos
        
        if not self.unconfirmed_transactions:
            return False

        last_block = self.last_block

        new_block = Block(index=last_block.index + 1, # Compara el nuevo bloque con el anterior
                          transacciones=self.unconfirmed_transactions, # Muestra la transaccion
                          timestamp=time.time(), # Muestra el tiempo
                          previous_hash=last_block.hash) # Compara el hash del nuevo bloque con el anterior

        Prueba = self.Prueba_de_trabajo(new_block)
        self.add_block(new_block, Prueba)

        self.unconfirmed_transactions = []

        return True