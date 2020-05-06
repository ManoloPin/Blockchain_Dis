import hashlib
import json
from time import time
from flask import Flask,jsonify, Request
"""
prueba ignorar
"""
app = Flask(__name__)

class Bloquecadena(object):
  def __init__(self):
   
   self.actual_Transacciones = []
   self.cadena = []

   # Crea el bloque génesis
   self.nuevo_bloque(anterior_hash=1, prueba=100)

  def nuevo_bloque(self, prueba, anterior_hash=None): # Crea un nuevo bloque y lo añade a la cadena de paso
   
     # Crear un nuevo Bloque en el Cadena de Bloques
   bloque = {
     'indice': len(self.cadena) + 1,
     'timestamp': time(),
     'Transacciones': self.actual_Transacciones,
     'prueba': prueba,   # La prueba dada por el algoritmo de Prueba de Trabajo
     'anterior_hash': anterior_hash or self.hash(self.cadena[-1]), # Hash del Bloque anterior
   }

   # Anular la lista actual de transacciones
   self.actual_Transacciones = []

   self.cadena.append(bloque)
   return bloque

  def new_transaction(self, remitente, destinatario, cantidad): # Añade una nueva transacción a la lista de transacciones de paso
   
   self.actual_Transacciones.append({
    'remitente': remitente,  # Dirección del remitente
    'destinatario': destinatario, # Dirección del destinatario
    'cantidad': cantidad, # Cantidad
   })

   return self.ultimo_bloque['indice'] + 1  # El índice del Bloque que llevará a cabo esta transacción

  @property
  def ultimo_bloque(self): # Devuelve el último bloque de la cadena
   return self.cadena[-1]

  @staticmethod
  def hash(bloque): # Hashes de un bloque
   
   # Debemos asegurarnos de que el Diccionario esté Ordenado, o tendremos hashes inconsistentes
   bloque_string = json.dumps(bloque, sort_keys=True).encode()
   return hashlib.sha256(bloque_string).hexdigest()

if __name__ == '__main__':
    app.run(debug=True, port = 5000)