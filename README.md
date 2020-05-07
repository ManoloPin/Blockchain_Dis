# Blockchain
Es un trabajo realizado para Sistemas Distribuidos donde demostramos el funcionamiento de Blockchain con lenguaje de programacion Python 
y se utilizo como editor de codigo visual Studio Code, donde tambien con Insomnia se realizaron las pruebas de los datos.

# ¿Qué es "blockchain"?🚀
Blockchain es una forma de almacenar datos digitales.Es un registro unico, consensuado y distrubuido en varios nodos de red. Los datos pueden ser literalmente cualquier cosa. Para Bitcoin, son las transacciones 
(registros de transferencias de Bitcoin de una cuenta a otra), pero incluso pueden ser archivos; No importa. Los datos se almacenan en forma 
de bloques, que están vinculados (o encadenados) juntos mediante hashes criptográficos, de ahí el nombre "blockchain."

Toda la magia reside en la forma en que estos datos se almacenan y se agregan a la cadena de bloques. Una cadena de bloques es esencialmente 
una lista vinculada que contiene datos ordenados.

# Pre-requisitos 📋
Para utilizar el programa se debe tener instaldo en el sistema python3, flask,request.
# Instalación 🔧
- Tener instalado algun editor de codigo para python3

- Tambien se debe instalar flask en python3 revisar el siguiente link:

	https://flask.palletsprojects.com/en/1.1.x/installation/
    
- Luego Clonar el proyecto

	git clone https://github.com/ManoloPin/Blockchain_Dis.git

# Ejecutando las pruebas ⚙️

- Se debe ejecutar el archivo 	

	python app.py 

para que se puedan ejecutar de igual forma el archivo blockchain.py

Luego al ejecutar la aplicacion debe tener funcionamiento en http://127.0.0.1:5000, pero despues se debe copiar en Insomnea dicho link 
y se incluye /new_transactions para que se podamos incluir el siguiente codigo Json para realizar las pruebas pertinentes.


    {
    "sender": "hsfdsfsdfsdfdsfe", 
    "recipient": "ksldfrthgnjrieo", 
    "amount: "500"
    }
    

# Vista previa ⌨️

- Esta es una vista previa de como esta funcinando las pruebas de Insomnia para verificar si esta ingresando la transferencia.

http://127.0.0.1:5000/new_transactions

![stack Overflow](https://github.com/ManoloPin/Blockchain_Dis/blob/master/img/Imagen1.jpeg)

- Con este codigo se esta verificando la cadena de los bloques.

http://127.0.0.1:5000/chain

![stack Overflow](https://github.com/ManoloPin/Blockchain_Dis/blob/master/img/Imagen2.jpeg)

- Este es otra prueba realizada donde hay dos transacciones en el bloque con la funcion minar, ya que se entiende que para utilizar la funcion para cerrar el bloque ya que sin minar no se puede agregar el bloque.

http://127.0.0.1:5000/chain

![stack Overflow](https://github.com/ManoloPin/Blockchain_Dis/blob/master/img/Imagen3.jpeg)

- Aqui esta la pueba realizada despues de minar las transacciones donde se cierra el bloque y se abre uno nuevo, donde luego se muestra como se agrega correctamente la cadena.

http://127.0.0.1:5000/añadir_block

![stack Overflow](https://github.com/ManoloPin/Blockchain_Dis/blob/master/img/Imagen4.jpeg)

# Construido con 🛠️

- Visual Studio Code - Editor de codigo
- Insomnia - Realizar pruebas de datos
- Python3 - Lenguaje de Programacion
- Flask - El framework web usado
- xampp - Servidor Web



# Autores ✒️

- Jose Manuel Pinilla Casas
- John Alejandro Solorza Guerrero

# Expresiones de Gratitud 🎁
Agradecemos al profesor por Carlos Armando Lopez Solano por su colaboracion y enseñanza que se ha realizado de forma virutal por temas de la pandemia Covid-19, ya que ha tenido dedicacion y paciencia para enseñarnos por este medio.
