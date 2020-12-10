import unittest
from src.coloranalysis import colorfunctions as cf

class TestCalculator(unittest.TestCase):

        

        def test_suggested_font_color(self):
                user_url = "https://assets.imgix.net/unsplash/bridge.jpg"
                self.assertEqual(cf.suggested_font_color(user_url), "#8c8c8c", "Suggested Font Color suggestion for bridge is accurate!")

        def test_hex(self):
                user_url = "https://assets.imgix.net/unsplash/motorbike.jpg"
                self.assertEqual(len(cf.color_values(user_url)), 6, "Color Value is providing correct number!")

        def test_color_modifier_parameter(self):
                user_url = "https://assets.imgix.net/unsplash/bridge.jpg"
                self.assertIsInstance(cf.suggested_font_color(user_url, "teal"), str, "Color modifying parameter accepted.")
        

if __name__ == '__main__':
        unittest.main()