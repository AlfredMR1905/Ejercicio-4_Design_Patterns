from adapter.pixabay_adapter import PixabayAdapter
from adapter.unsplash_adapter import UnsplashAdapter
from bridge.rank_algorithm import RankAlgorithm, SimpleRankAlgorithm, AdvancedRankAlgorithm

class BromeliaPictInventory:
    def __init__(self, pixabay_api_key, unsplash_access_key, rank_algorithm: RankAlgorithm):
        self.pixabay_adapter = PixabayAdapter(pixabay_api_key)
        self.unsplash_adapter = UnsplashAdapter(unsplash_access_key)
        self.rank_algorithm = rank_algorithm

    def search_and_rank_photos(self, query):
        #Note que como se implementa un patron adapter y retorna un diccionario en ambos casos
        # con el mismo formato de datos, no es necesario hacer una transformacion de datos.
        pixabay_photos = self.pixabay_adapter.search_photos(query)
        unsplash_photos = self.unsplash_adapter.search_photos(query)
        all_photos = pixabay_photos + unsplash_photos
        return self.rank_algorithm.rank_photos(all_photos)

# Ejemlo de uso
if __name__ == "__main__":
    pixabay_api_key = 'claveRandomPixabay'
    unsplash_access_key = 'claveRandomUnsplash'
    rank_algorithm = SimpleRankAlgorithm()  #O cualquier otra implementacion de RankAlgorithm

    # Instanciar el inventario de fotos
    inventory = BromeliaPictInventory(pixabay_api_key, unsplash_access_key, rank_algorithm) 
    top_photos = inventory.search_and_rank_photos('nature') 
    print(top_photos)