from Util.DBConn import DBConnection
from abc import ABC,abstractmethod
from myexceptions import ArtworkNotFoundException

class IArtworkService(ABC):
    @abstractmethod
    def readArtwork(self):
        pass
    @abstractmethod
    def getArtworkById(self,artworkId):
        pass
    @abstractmethod
    def addArtwork(self,new_artwork):
        pass
    @abstractmethod
    def removeArtwork(self,artworkId):
        pass
    @abstractmethod
    def updateArtwork(self,artworkId,description,title,creationDate,medium,imageURL,artistID):
        pass
class ArtworkService(IArtworkService,DBConnection):
    def readArtwork(self):
        try:
            self.cursor.execute("select * from artwork")
            artworks=self.cursor.fetchall()
            for artwork in artworks:
                print(artwork)
            return artworks
        except Exception as e:
            print(e)
            return None
    
    def getArtworkById(self,artworkId):
        try:
            self.cursor.execute("select * from artwork where artworkId=?",(artworkId))
            artwork=self.cursor.fetchone()
            if artwork is None:
                raise ArtworkNotFoundException(artworkId)
            else:
                print(artwork)

        except ArtworkNotFoundException as e:
            print("Error!!",e)

        except Exception as e:
            print("Error!!",e)

    def addArtwork(self,new_artwork):
        try:
            self.cursor.execute("insert into Artwork(artworkID,description,title,creationDate,medium,imageURL,artistID) VALUES(?,?,?,?,?,?,?)",
                      (new_artwork.artworkID,new_artwork.description,new_artwork.title,new_artwork.creationDate,new_artwork.medium,new_artwork.imageURL,new_artwork.artistID)
                        )

            self.conn.commit() 
            return new_artwork.artworkId
        except Exception as e:
            print("Error!!",e)
            return None
        
    def removeArtwork(self,artworkId):
        try:
            self.cursor.execute("Delete FROM User_Favorite_Artwork WHERE artworkId = ?", (artworkId,))
            self.cursor.execute("Delete FROM Artwork_Gallery WHERE artworkId = ?", (artworkId,))
            self.cursor.execute("Delete from artwork where artworkId=?",(artworkId))
           
            self.conn.commit()
        except Exception as e:
            print(e)
       
    def updateArtwork(self,artworkId,description,title,creationDate,medium,imageURL,artistID):
        try:
            self.cursor.execute("update artwork SET description = ?, title = ?, creationDate = ?, medium = ?, imageURL = ?, artistID = ? WHERE artworkId = ? ",
                        (description,title,creationDate,medium,imageURL,artistID,artworkId)
                        )
            self.conn.commit()
            return True
        except Exception as e:
            print(e)
            return False
