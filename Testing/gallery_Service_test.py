import unittest

from DAO.gallery_Service import GalleryService
from Entity.Gallery import Gallery


class TestGalleryServiceModule(unittest.TestCase):
    def setUp(self):
        self.gallery_service = GalleryService()
        # Adding some initial data for testing
        self.test_gallery_id = self.gallery_service.addGallery(9,'The Vintage Museum','Museum dedicated for vintage arts', 'Paris,France', 'Wison', '12:00:00', 5)
        self.assertIsNotNone(self.test_gallery_id)

    def test_add_gallery(self):
        self.gallery_service = GalleryService()
        galleryId = 8
        name = 'The Vintage museum'
        description = 'Museum dedicated for vintage arts'
        location = 'Paris, France'
        curator = 'Wilson'
        openingHours = '12:00:00'
        artistId = 4
        created_gallery_id = self.gallery_service.addGallery(galleryId,name, description, location, curator, openingHours, artistId)
        self.assertIsNotNone(created_gallery_id)

    def test_read_gallery(self):
        self.gallery_service=GalleryService()
        galleries = self.gallery_service.readGallery()
        self.assertIsNotNone(galleries)
        self.assertGreater(len(galleries), 0)

    def test_update_gallery(self):
        self.gallery_service=GalleryService()
        galleryId = 8
        name = 'The Vintage museum'
        description = 'Museum dedicated for vintage arts'
        location = 'Paris, France'
        curator = 'Wilson'
        openingHours = '12:00:00'
        artistId = 4
        update_status=self.gallery_service.updateGallery(galleryId,name, description, location, curator, openingHours, artistId)
        self.assertTrue(update_status)


        # Check after updating the movie
        self.gallery_service.cursor.execute(
            "SELECT * FROM gallery WHERE galleryId=?", (galleryId,) 
        )
        updated_gallery = self.gallery_service.cursor.fetchone()


        self.assertEqual(updated_gallery[0], galleryId)
        self.assertEqual(updated_gallery[1], name)
        self.assertEqual(updated_gallery[2], description)
        self.assertEqual(updated_gallery[3], location)
        self.assertEqual(updated_gallery[4], curator)
        self.assertEqual(updated_gallery[5][:8], openingHours)
        self.assertEqual(updated_gallery[6], artistId)

    def test_delete_gallery(self):
        self.gallery_service=GalleryService()
        self.galleryId=9
        self.gallery_service.removeGallery(self.galleryId)

        self.gallery_service.cursor.execute(
            "SELECT * FROM gallery WHERE galleryId = ?", (self.galleryId)
        )
        gallery = self.gallery_service.cursor.fetchone()

        self.assertIsNone(gallery)


if __name__ == "__main__":
    unittest.main()