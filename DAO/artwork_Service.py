# try:
#             self.cursor.execute("insert into Artwork(artworkID,description,title,creationDate,medium,imageURL,artistID) VALUES(?,?,?,?,?,?,?)",
#                         (artwork.artworkID,artwork.description,artwork.title,artwork.creationDate,artwork.medium,artwork.imageURL,artwork.artistID)
#                         )
            
#             self.conn.commit() # Permanently store | no commit we can undo 
#         except Exception as e:
#             print(e)

from Util.DBConn import DBConnection
class ArtworkService(DBConnection):
    def readArtwork(self):
        try:
            self.cursor.execute("select * from artwork")
            artworks=self.cursor.fetchall()
            for artwork in artworks:
                print(artwork)
        except Exception as e:
            print(e)

    def addArtwork(self,new_artwork):
        try:
            self.cursor.execute("insert into Artwork(artworkID,description,title,creationDate,medium,imageURL,artistID) VALUES(?,?,?,?,?,?,?)",
                      (new_artwork.artworkID,new_artwork.description,new_artwork.title,new_artwork.creationDate,new_artwork.medium,new_artwork.imageURL,new_artwork.artistID)
                        )

            self.conn.commit() 
        except Exception as e:
            print(e)
        
       
 
    def removeArtwork(self,artworkId):
        try:
            self.cursor.execute("delete from artwork where artworkId=?",
                        (artworkId)
                        )
            
            self.conn.commit()
        except Exception as e:
            print(e)
       

    def updateArtwork(self,artworkId,description,title,creationDate,medium,imageURL,artistID):
        try:
            self.cursor.execute("update artwork SET ?,?,?,?,?,?,? WHERE artworkId=?",
                        (artworkId,description,title,creationDate,medium,imageURL,artistID)
                        )
            self.conn.commit()
        except Exception as e:
            print(e)
            
