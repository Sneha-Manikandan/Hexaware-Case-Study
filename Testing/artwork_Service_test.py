import unittest

from DAO.artwork_Service import ArtworkService
from Entity.Artwork import Artwork


class TestArtworkyServiceModule(unittest.TestCase):
    # def setUp(self):
    #     self.artwork_service = ArtworkService()
    #     # Adding some initial data for testing
    #     # self.test_gallery = Gallery(7,'The Vintage Museum','Museum dedicated for vintage arts', 'Paris,France', 'Wison', '12:00:00', 7)
    #     new_artwork=9,'A painting by Pablo Picasso.','Les Demoiselles Avignon', '1907-07-01', 'Oil on canvas', 'https://example.com/lesdemoiselles.jpg', 3
    #     test_artwork_id = self.artwork_service.addArtwork(new_artwork)
    #     self.assertIsNotNone(test_artwork_id)

    def test_add_artwork(self):
        self.artwork_service = ArtworkService()
        artworkID=8
        description='A painting by Pablo Picasso.'
        title='Les Demoiselles Avignon'
        creationDate='1907-07-01'
        medium='Oil on canvas'
        imageURL='https://example.com/lesdemoiselles.jpg'
        artistID=3
        new_artwork=Artwork(artworkID,description,title,creationDate,medium,imageURL,artistID)
        created_artwork_id = self.artwork_service.addArtwork(new_artwork)
        self.assertIsNotNone(created_artwork_id)

    def test_read_artwork(self):
        self.artwork_service=ArtworkService()
        artworks = self.artwork_service.readArtwork()
        self.assertIsNotNone(artworks)
        self.assertGreater(len(artworks), 0)

    def test_update_artwork(self):
        self.artwork_service = ArtworkService()
        artworkID=8
        description='A painting by Pablo Picasso.'
        title='Les Demoiselles Avignon'
        creationDate='1907-07-01'
        medium='Oil on canvas'
        imageURL='https://example.com/lesdemoiselles.jpg'
        artistId = 3
        update_status=self.artwork_service.updateArtwork(artworkID,description,title,creationDate,medium,imageURL,artistId)
        self.assertTrue(update_status)


        # Check after updating the movie
        self.artwork_service.cursor.execute(
            "SELECT * FROM artwork WHERE artworkId=?", (artworkID,) 
        )
        updated_artwork = self.artwork_service.cursor.fetchone()


        self.assertEqual(updated_artwork[0], artworkID)
        self.assertEqual(updated_artwork[1], description)
        self.assertEqual(updated_artwork[2], title)
        self.assertEqual(updated_artwork[3], creationDate)
        self.assertEqual(updated_artwork[4], medium)
        self.assertEqual(updated_artwork[5], imageURL)
        self.assertEqual(updated_artwork[6], artistId)

    def test_delete_artwork(self):
        self.artwork_service=ArtworkService()
        self.artworkID=9
        self.artwork_service.removeArtwork(self.artworkID)

        self.artwork_service.cursor.execute(
            "SELECT * FROM artwork WHERE artworkId = ?", (self.artworkID)
        )
        artwork = self.artwork_service.cursor.fetchone()

        self.assertIsNone(artwork)


if __name__ == "__main__":
    unittest.main()