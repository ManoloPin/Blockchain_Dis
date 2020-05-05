from hashlib import sha256
import json
import time

class Block:
    def __init__ (self, index, transactions, timestamp, previous_hash):
        self.index          = index         #numero de cada bloque 
        self.trasactions    = transactions  #transacciones recolectadas
        self.timestamp      = timestamp     #tiempo del bloque
        self.previous_hash  = previous_hash #hash del bloque anterior

    def calcular_hash(self): # calcular el hash
        """
        devuelve el hash del bloque al convertirlo primero en JSON o al cerrar el bloque 
        """
        block_string = json.dumps(self.__dict__, sort_keys = True)
        return sha256(block_string.encode()).hexdigest()

"""
----------------------------------------------------------"
"""

class Blockchain:

    def __init__(self):
        """
        constructor de la clase blokchain
        """
        dificultad = 2 # dificultad del algoritmo

        self.chain = []
        self.crear_generisi_block()

    def crear_genesis_block(self):

        genesis_block = Block(0,[],time.time(),"0")
        genesis_block.hash = genesis_block.calcular_hash()
        self.chain.append(genesis_block) # agregar el bloque genesis a la cadena

    @property
    def Ultimo_block(self):
        return self.chain[-1]

    

    