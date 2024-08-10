import requests  # Importa la librería requests para hacer solicitudes HTTP

class BromeliaPictInventory:
    def __init__(self):
        # Claves de API para Pixabay y Unsplash
        self.pixabay_key = 'your-pixabay-key'
        self.unsplash_key = 'your-unsplash-key'

    def get_pixabay_photos(self, query):
        """
        Busca fotos en la API de Pixabay usando una consulta específica.
        
        Parámetros:
        query (str): El término de búsqueda para las fotos.

        Retorna:
        list: Una lista de fotos obtenidas de Pixabay.
        """
        # Realiza una solicitud HTTP GET a la API de Pixabay con la clave y la consulta
        response = requests.get(f'https://pixabay.com/api/?key={self.pixabay_key}&q={query}')
        # Convierte la respuesta JSON a un diccionario de Python y devuelve la lista de fotos ('hits')
        return response.json()['hits']

    def get_unsplash_photos(self, query):
        """
        Busca fotos en la API de Unsplash usando una consulta específica.
        
        Parámetros:
        query (str): El término de búsqueda para las fotos.

        Retorna:
        list: Una lista de fotos obtenidas de Unsplash.
        """
        # Configura los headers de la solicitud con la clave de acceso de Unsplash
        headers = {"Authorization": f"Client-ID {self.unsplash_key}"}
        # Realiza una solicitud HTTP GET a la API de Unsplash con los headers y la consulta
        response = requests.get(f'https://api.unsplash.com/search/photos?query={query}', headers=headers)
        # Convierte la respuesta JSON a un diccionario de Python y devuelve la lista de fotos ('results')
        return response.json()['results']

    def get_top_photos(self, query):
        """
        Obtiene las 10 mejores fotos combinando resultados de Pixabay y Unsplash.
        
        Parámetros:
        query (str): El término de búsqueda para las fotos.

        Retorna:
        list: Las primeras 10 fotos combinadas de ambas APIs.
        """
        # Llama a los métodos para obtener fotos de ambas APIs
        pixabay_photos = self.get_pixabay_photos(query)
        unsplash_photos = self.get_unsplash_photos(query)
        # Combina las listas de fotos de ambas APIs y devuelve las primeras 10
        return (pixabay_photos + unsplash_photos)[:10]