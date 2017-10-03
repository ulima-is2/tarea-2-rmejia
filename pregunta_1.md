###Principio de responsabilidad unica: (S)
- Las clases deben tener solo una responsabilidad, y en este caso las clases
cine (CinePlaneta y CineStark) tienen más de una: listar_peliculas, listar_funciones
y guardar_entrada, donde el último es el que tiene una funcionalidad absolutamente
distinta a las dos anteriores. Listar y Guardar son responsabilidades diferentes.

###Principio de Abierto/Cerrado (O)
-  Las clases de los cines no contienen herencia de una clase Padre, y tienen métodos
que realizan las mismas funciones pero no tienen conexión alguna. Esto también hace que
el código no sea extendible.

###Principio de Sustitución de Liskov (L)
- Este principio define que si los subtipos de un tipo pueden reemplazar a los objetos
del tipo no deben alterar ninguna propiedad del programa. En este caso no vemos ningún
tipo de herencia generada.