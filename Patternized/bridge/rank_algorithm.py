from abc import ABC, abstractmethod

# Abstraccion 
class RankAlgorithm(ABC):
    @abstractmethod
    def rank_photos(self, photos):
        pass

# Implementacion concreta #1
class SimpleRankAlgorithm(RankAlgorithm):
    def rank_photos(self, photos):
        return sorted(photos, key=lambda photo: photo.likes, reverse=True)[:10]

# Implementacion concreta #2
class AdvancedRankAlgorithm(RankAlgorithm):
    def rank_photos(self, photos):
        return sorted(photos, key=lambda photo: (photo.likes * photo.views), reverse=True)[:10]