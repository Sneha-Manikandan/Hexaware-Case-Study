from Util.DBConn import DBConnection
from abc import ABC,abstractmethod

class IUserFavoriterArtwork(ABC):
    @abstractmethod
    def getUserFavoriteArtwork(self):
        pass

    @abstractmethod
    def getUserFavoriteArtworksbyId(self,userId):
        pass
    
    @abstractmethod
    def addArtworkToFavorite(self,new_favoriteArtwork):
        pass

    @abstractmethod
    def removeArtworkFromFavorite(self,userId,artworkId):
        pass

class UserFavoriteArtworkService(IUserFavoriterArtwork,DBConnection):
    def getUserFavoriteArtwork(self):
        try:
            self.cursor.execute("""select u.userid,a.artworkID, a.title,a.description,  a.creationDate, a.medium, a.imageURL from User_Favorite_Artwork u
                            inner join artwork a on u.artworkID=a.artworkID
                            group by u.userid,a.artworkID, a.description, a.title, a.creationDate, a.medium, a.imageURL""")
            favorite_artworks=self.cursor.fetchall()
            for artwork in favorite_artworks:
                print(artwork)
        except Exception as e:
            print(e)

    def getUserFavoriteArtworksbyId(self,userId):
        try:
            self.cursor.execute("""select u.userid,a.artworkID, a.title,a.description,  a.creationDate, a.medium, a.imageURL from User_Favorite_Artwork u
                            inner join artwork a on u.artworkID=a.artworkID
                            group by u.userid,a.artworkID, a.description, a.title, a.creationDate, a.medium, a.imageURL
                            having u.userId=?""",(userId))
            favorite_artwork=self.cursor.fetchall()
            for artwork in favorite_artwork:
                print(artwork)
        except Exception as e:
            print(e)

    def addArtworkToFavorite(self,new_favoriteArtwork):
        try:
            self.cursor.execute("insert into User_Favorite_Artwork(userId,artworkId) values(?,?)",
                                (new_favoriteArtwork.userId,new_favoriteArtwork.artworkId))
            self.conn.commit()
        except Exception as e:
            print(e)

    def removeArtworkFromFavorite(self,userId,artworkId):
        try:
            self.cursor.execute("delete from User_Favorite_Artwork where userId=? AND artworkId=?",
                                (userId,artworkId))
            self.conn.commit()
        except Exception as e:
            print(e)
    
    
