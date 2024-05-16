from Util.DBConn import DBConnection
from abc import ABC,abstractmethod

class IArtistService(ABC):
    @abstractmethod
    def readArtist(self):
        pass
    @abstractmethod
    def addArtist(self,new_artist):
        pass
    @abstractmethod
    def removeArtist(self,artistId):
        pass
    @abstractmethod
    def updateArtist(self,artistId,name,biography,birthDate,nationality,website,contactInformation):
        pass
class ArtistService(IArtistService,DBConnection):
    def readArtist(self):
        try:
            self.cursor.execute("select * from artist")
            artists=self.cursor.fetchall()
            for artist in artists:
                print(artist)
        except Exception as e:
            print(e)

    def addArtist(self,new_artist):
        try:
            self.cursor.execute("insert INTO artist (artistId,name,biography,birthDate,nationality,website,contactInformation) VALUES(?,?,?,?,?,?,?)",
                        (new_artist.artistId,new_artist.name,new_artist.biography,new_artist.birthDate,new_artist.nationality,new_artist.website,new_artist.contactInformation)
                        )
            
            # self.conn.commit() 
        except Exception as e:
            print(e)

    def removeArtist(self,artistId):
        try:
            self.cursor.execute("DELETE FROM Artwork_Gallery WHERE artworkID IN (SELECT artworkID FROM Artwork WHERE artistID = ?)", (artistId,))
            self.cursor.execute("DELETE FROM User_Favorite_Artwork WHERE artworkID IN (SELECT artworkID FROM Artwork WHERE artistID = ?)", (artistId,))
            self.cursor.execute("delete FROM gallery WHERE artistId=?",(artistId))
            self.cursor.execute("delete FROM artwork WHERE artistId=?",(artistId))
            self.cursor.execute("delete FROM artist WHERE artistId=?",(artistId))
                        
            # self.conn.commit()
        except Exception as e:
            print(e)
       

    def updateArtist(self,artistId,name,biography,birthDate,nationality,website,contactInformation):
        try:
            self.cursor.execute("Update Artist SET name = ?, biography = ?, birthDate = ?, nationality = ?, website = ?, contactInformation = ? WHERE ArtistId=?",
                        (name,biography,birthDate,nationality,website,contactInformation,artistId)
                        )
            # self.conn.commit()
        except Exception as e:
            print(e)
            
