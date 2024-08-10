from abc import ABC, abstractmethod

class PhotoAdapter(ABC):
    
    @abstractmethod
    def search_photos(self, query):
        pass