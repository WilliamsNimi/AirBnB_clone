#!/usr/bin/python3
""" Test file review """
import unittest
from models.review import Review


class TestUser(unittest.TestCase):
    """ Test for Review Class """

    def setUp(self):
        """ The setUp function """
        self.review = Review()

    def test_place_id_attribute(self):
        """This function tests the that the Review class has the place_id attribute"""
        self.assertTrue(hasattr(self.review, "place_id"))
        self.assertIsInstance(self.review.place_id, str, "place_id should be of type str")
        self.assertEqual(self.review.place_id, "")

    def test_user_id_attribute(self):
        """This function tests the that the Review class has the user_id attribute"""
        self.assertTrue(hasattr(self.review, "user_id"))
        self.assertIsInstance(self.review.user_id, str, "user_id should be of type str")
        self.assertEqual(self.review.user_id, "")

    def test_text_attribute(self):
        """This function tests the that the Review class has the text attribute"""
        self.assertTrue(hasattr(self.review, "text"))
        self.assertIsInstance(self.review.text, str, "text should be of type str")
        self.assertEqual(self.review.text, "")

    def tearDown(self):
        """This is the tearDown function to destroy the instance of review created"""
        del self.review


if __name__ == "__main__":
    unittest.main()
