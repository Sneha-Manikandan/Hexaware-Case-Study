class GalleryNotFoundException(Exception):
    def  __init__(self,galleryId):
        super().__init__(f"No such gallery with GalleryID {galleryId} found.")