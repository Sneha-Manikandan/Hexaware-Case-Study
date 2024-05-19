class ArtistNotFoundException(Exception):
    def __init__(self,artistId):
        super().__init__(f"Artist with ID {artistId} not found.")