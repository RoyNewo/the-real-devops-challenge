**Challenge #1**
He querido comprobar que el resultado era correcto por lo que para hacer el primer challenge básicamente he hecho varios de los otros por el camino que desarrollare en más medida cuando llegue.
Aunque tengo algo de experiencia con python es verdad que no he trabajado apenas ni con flask ni con Mongodb, por lo que me ha llevado más un buen par de horas arrancar la aplicación y cargar los datos para ver los resultados. Aunque han sido horas bien invertidas porque me ha allanado el trabajo para los siguientes Challenges.

Para solucionar el challenge 1 he el archivo mongoflask.py he hecho los siguientes cambios
he añadido la libreria Response de flask para tener la respuesta http 204
luego he cambiado funcion find_restaurants al siguiente codigo:

    def  find_restaurants(mongo, _id=None):    
	    query  = {}    
	    if  _id:    
		    query["_id"] = ObjectId(_id)    
		    if  mongo.db.restaurant.find_one(query) is  None:    
			    return Response(status=204)    
		    else:    
			    return  mongo.db.restaurant.find_one(query)    
	    else:    
		    return  list(mongo.db.restaurant.find(query))

Con esto diferencio entre la query donde saca todos los restaurantes y uno específico para dar resultados distintos.

Tambien he tenido que hacer un cambio dentro de app.py ya que la response 204 no era json serializable asi que ahora es asi:

    @app.route("/api/v1/restaurant/<id>")    
    def  restaurant(id):    
	    restaurants  =  find_restaurants(mongo, id)    
	    try:    
		    return jsonify(restaurants)    
	    except  TypeError:    
		    return  restaurants


**Challenge #3**
En el repositorio he dejado un Dockerfile con la creación de la imagen de docker
Puntos que tengo en cuenta: 

 1. En siguiente challenges voy a hacer un docker-compose que va a estar
    en una ruta superior al Dockerfile.
El dockerfile en si es muy simple uso la imagen python3.6 que he visto que funciona con la app, gracias a los tests de tox, he instalado con pip los requirements y lanzado la app

**Challenge #4**
Este Challenge lo resuelvo entre el challenge #1 antes de que cargue la app de flask llamo a un pequeño script que he metido en src llamado loaddataset.py en este script compruebo si la db restaurat de mongo tiene datos. Si no tiene los import si no paso.
Luego levanto la instancia de mongodb desde el docker-compose, se que lo he levantado sin ningún tipo de usuario y contraseña, y probablemente deberíamos tener un sitio más específico para el volumen de datos. Pero en este caso he priorizado a que funcionara, aunque inseguro.

**Challenge #5**
Aunque el docker-compose lo he dejado dentro de la misma carpeta donde esta todo. Tengo en cuenta va a estar en la ruta superior a la hora de ejecutarlo.
Me aprovecho que va a estar en el mismo stack de docker para poder usar el nombre de servicio mongo a la hora de llamarlo en las peticiones de la api

**Final Challenge**
Este no he podido probarlo realmente, asi que no me extrañaria que fallara por algun lado, pero el archivo manifest.yaml contine los deployment y servicios para levantar tanto la app como mongodb.
