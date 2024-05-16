
class ArtworkNotFoundException(Exception):
    def __init__(self,artworkId):
        super().__init__(f"Artwork with ID {artworkId} not found.")