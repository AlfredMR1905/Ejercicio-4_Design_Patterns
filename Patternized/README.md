# Documentación

## Implementación del Patrón Adapter

En este ejercicio, hemos implementado el patrón Adapter para permitir que nuestra aplicación busque fotos en diferentes servicios web de fotos en este caso Pixabay y unsplash. A continuación, se describe cómo se ha implementado este patrón.

### Interfaz del Adaptador (Adapter Interface)

Primero, definimos una interfaz abstracta `PhotoAdapter` que declara el método `search_photos`. Este método debe ser implementado por cualquier clase que actúe como adaptador.

### Clases concretas implemetando adapter

* La clase `UnsplashAdapter` se encarga de realizar la búsqueda de fotos en el servicio Unsplash. Implementa el método `search_photos` definido en la interfaz `PhotoAdapter`.
* La clase PixabayAdapter se encarga de realizar la búsqueda de fotos en el servicio Pixabay. Implementa el método `search_photos` definido en la interfaz `PhotoAdapter`.

Note que al realizar esto este aplicación puede trabajar con diferentes servicios de fotos sin cambiar el código.


### Implementación del Patrón Bridge

En este ejercicio, hemos implementado el patrón Bridge para desacoplar la lógica de ranking de fotos de su implementación específica. Lo que facilita cambiar entre diferentes algoritmos de ranking sin modificar el código que utiliza estos algoritmos.

#### Definición de la Abstracción y la Implementación

1. **Interfaz de Implementación (Implementor Interface)**:
    - Definimos una clase abstracta `RankAlgorithm` que declara el método `rank_photos`.

2. **Implementaciones Concretas (Concrete Implementors)**:
    - Creamos clases concretas `SimpleRankAlgorithm` y `AdvancedRankAlgorithm` que implementan la interfaz `RankAlgorithm`.




