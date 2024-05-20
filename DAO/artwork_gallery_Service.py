from Util.DBConn import DBConnection
from abc import ABC,abstractmethod

class IArtworkGallery(ABC):
    @abstractmethod
    def getArtworkGallery(self):
        pass

    @abstractmethod
    def getArtworkGallerybyId(self,artworkId):
        pass
    
    @abstractmethod
    def addArtworkToGallery(self,new_artworkGallery):
        pass

    @abstractmethod
    def removeArtworkFromGallery(self,artworkId,gallerykId):
        pass

class ArtworkGalleryService(IArtworkGallery, DBConnection):
    def getArtworkGallery(self):
        try:
            self.cursor.execute("""SELECT ag.artworkID, g.galleryID, g.name, g.description, g.location, g.curator, g.openingHours, g.artistID
                                   FROM Artwork_Gallery ag
                                   INNER JOIN Gallery g ON ag.galleryID = g.galleryID""")
            artwork_galleries = self.cursor.fetchall()
            for artwork_gallery in artwork_galleries:
                print(artwork_gallery)
        except Exception as e:
            print(e)

    def getArtworkGallerybyId(self, artworkId):
        try:
            self.cursor.execute("""SELECT ag.artworkID, g.galleryID, g.name, g.description, g.location, g.curator, g.openingHours, g.artistID
                                   FROM Artwork_Gallery ag
                                   INNER JOIN Gallery g ON ag.galleryID = g.galleryID
                                   WHERE ag.artworkID = ?""", (artworkId,))
            artwork_gallery = self.cursor.fetchall()
            for gallery in artwork_gallery:
                print(gallery)
        except Exception as e:
            print(e)

    def addArtworkToGallery(self,new_artworkGallery):
        try:
            self.cursor.execute("INSERT INTO Artwork_Gallery (artworkID, galleryID) VALUES (?, ?)",
                                (new_artworkGallery.artworkId, new_artworkGallery.galleryId))
            self.conn.commit()
        except Exception as e:
            print(e)

    def removeArtworkFromGallery(self, artworkId, galleryId):
        try:
            self.cursor.execute("DELETE FROM Artwork_Gallery WHERE artworkID = ? AND galleryID = ?",
                                (artworkId, galleryId))
            self.conn.commit()
        except Exception as e:
            print(e)