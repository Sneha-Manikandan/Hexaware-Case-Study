import unittest

from DAO.artwork_Service import ArtworkService
from Entity.Artwork import Artwork


class TestArtworkyServiceModule(unittest.TestCase):
    def setUp(self):
        self.artwork_service = ArtworkService()
        # Adding some initial data for testing
        # self.test_gallery = Gallery(7,'The Vintage Museum','Museum dedicated for vintage arts', 'Paris,France', 'Wison', '12:00:00', 7)
        self.test_artwork_id = self.artwork_service.addArtwork(9,'The Vintage Museum','Museum dedicated for vintage arts', 'Paris,France', 'Wison', '12:00:00', 5)
        self.assertIsNotNone(self.test_artwork_id)

    def test_add_artwork(self):
        self.artwork_service = ArtworkService()
        artworkId=8
        description='A painting by Pablo Picasso.'
        title='Les Demoiselles Avignon'
        creationDate='1907-07-01'
        medium='Oil on canvas'
        imageURL='https://example.com/lesdemoiselles.jpg'
        artistID=3
        created_artwork_id = self.artwork_service.addArtwork(artworkId,description,title,creationDate,medium,imageURL,artistID)
        self.assertIsNotNone(created_artwork_id)

    def test_read_artwork(self):
        self.artwork_service=ArtworkService()
        artworks = self.artwork_service.readArtwork()
        self.assertIsNotNone(artworks)
        self.assertGreater(len(artworks), 0)

    def test_update_artwork(self):
        self.artwork_service = ArtworkService()
        artworkId=8
        description='A painting by Pablo Picasso.'
        title='Les Demoiselles Avignon'
        creationDate='1907-07-01'
        medium='Oil on canvas'
        imageURL='https://example.com/lesdemoiselles.jpg'
        artistId = 3
        update_status=self.artwork_service.addArtwork(artworkId,description,title,creationDate,medium,imageURL,artistId)
        self.assertTrue(update_status)


        # Check after updating the movie
        self.artwork_service.cursor.execute(
            "SELECT * FROM artwork WHERE artworkId=?", (artworkId,) 
        )
        updated_artwork = self.gallery_service.cursor.fetchone()


        self.assertEqual(updated_artwork[0], artworkId)
        self.assertEqual(updated_artwork[1], description)
        self.assertEqual(updated_artwork[2], title)
        self.assertEqual(updated_artwork[3], creationDate)
        self.assertEqual(updated_artwork[4], medium)
        self.assertEqual(updated_artwork[5], imageURL)
        self.assertEqual(updated_artwork[6], artistId)

    def test_delete_artwork(self):
        self.artwork_service=ArtworkService()
        self.artworkId=9
        self.artwork_service.removeArtwork(self.artworkId)

        self.artwork_service.cursor.execute(
            "SELECT * FROM artwork WHERE artworkId = ?", (self.artworkId)
        )
        artwork = self.artwork_service.cursor.fetchone()

        self.assertIsNone(artwork)


if __name__ == "__main__":
    unittest.main()