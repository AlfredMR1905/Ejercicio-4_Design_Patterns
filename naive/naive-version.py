import requests  # Importa la librería requests para hacer solicitudes HTTP

class BromeliaPictInventory:
    def __init__(self):
        # Claves de API para Pixabay y Unsplash
        self.pixabay_key = 'claveRandomPixabay'
        self.unsplash_key = 'claveRandomUnsplash'

    # Método para obtener fotos de Pixabay
    def get_pixabay_photos(self, query):
        # Realiza una solicitud HTTP GET a la API de Pixabay
        response = requests.get(f'https://pixabay.com/api/?key={self.pixabay_key}&q={query}')
        # Convierte la respuesta JSON a un diccionario de Python y devuelve la lista de fotos ('hits')
        return response.json()['hits']

    # Método para obtener fotos de Unsplash
    def get_unsplash_photos(self, query):
        # Configura los headers
        headers = {"Authorization": f"Client-ID {self.unsplash_key}"}
        # Realiza una solicitud HTTP GET a la API de Unsplash
        response = requests.get(f'https://api.unsplash.com/search/photos?query={query}', headers=headers)
        # Convierte la respuesta JSON a un diccionario de Python y devuelve la lista de fotos ('results')
        return response.json()['results']

    # Método para obtener las 10 mejores fotos de Pixabay y Unsplash
    def get_top_photos(self, query):
        pixabay_photos = self.get_pixabay_photos(query)
        unsplash_photos = self.get_unsplash_photos(query)
        return (pixabay_photos + unsplash_photos)[:10]