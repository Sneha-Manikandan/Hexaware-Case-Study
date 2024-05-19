import unittest

from DAO.gallery_Service import GalleryService
from Entity.Gallery import Gallery


class TestGalleryServiceModule(unittest.TestCase):
    def setUp(self):
        self.gallery_service = GalleryService()

    def test_add_gallery(self):
        name = 'The Vintage museum'
        description = 'Museum dedicated for vintage arts'
        location = 'Paris, France'
        curator = 'Wilson'
        openingHours = '12:00:00'
        artistId = 4
        created_gallery_id = self.gallery_service.addGallery(name, description, location, curator, openingHours, artistId)
        self.assertIsNotNone(created_gallery_id)

    def test_read_gallery(self):
        galleries = self.gallery_service.readGallery()
        self.assertIsNotNone(galleries)
        self.assertGreater(len(galleries), 0)

    def test_update_gallery(self):
        galleryId = 3
        name = 'Matisse Museum'
        description = 'Museum dedicated to the works of Henri Matisse.'
        location = 'Nice, France'
        curator = 'Henri Matisse'
        openingHours = '11:00:00'
        artistId = 3
        update_status=self.gallery_service.updateGallery(galleryId,name, description, location, curator, openingHours, artistId)
        self.assertTrue(update_status)


        self.gallery_service.cursor.execute(
            "SELECT * FROM gallery WHERE galleryId=?", (galleryId,) 
        )
        updated_gallery = self.gallery_service.cursor.fetchone()


        self.assertEqual(updated_gallery[1], name)
        self.assertEqual(updated_gallery[2], description)
        self.assertEqual(updated_gallery[3], location)
        self.assertEqual(updated_gallery[4], curator)
        self.assertEqual(updated_gallery[5][:8], openingHours)
        self.assertEqual(updated_gallery[6], artistId)

    def test_delete_gallery(self):
        self.galleryId=7
        self.gallery_service.removeGallery(self.galleryId)

        self.gallery_service.cursor.execute(
            "SELECT * FROM gallery WHERE galleryId = ?", (self.galleryId)
        )
        gallery = self.gallery_service.cursor.fetchone()

        self.assertIsNone(gallery)


if __name__ == "__main__":
    unittest.main()