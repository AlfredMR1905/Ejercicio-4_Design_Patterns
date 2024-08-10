import requests
import photo_adapter as PhotoAdapter

class UnsplashAdapter(PhotoAdapter):
    def __init__(self, access_key):
        self.access_key = access_key

    def search_photos(self, query):
        response = requests.get(
            'https://api.unsplash.com/search/photos',
            params={'query': query, 'client_id': self.access_key}
        )
        data = response.json()
        return [{'id': photo['id'], 'likes': photo['likes'], 'views': photo['views']} for photo in data['results']]