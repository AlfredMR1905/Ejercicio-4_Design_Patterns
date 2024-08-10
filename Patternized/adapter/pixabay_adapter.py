import requests
import photo_adapter as PhotoAdapter

class PixabayAdapter(PhotoAdapter):
    def __init__(self, api_key):
        self.api_key = api_key

    def search_photos(self, query):
        response = requests.get(
            'https://pixabay.com/api/',
            params={'q': query, 'key': self.api_key}
        )
        data = response.json()
        return [{'id': photo['id'], 'likes': photo['likes'], 'views': photo['views']} for photo in data['hits']]
