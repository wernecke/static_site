import unittest
from generate_page import *

class TestGeneratePage(unittest.TestCase):
    def test_extract_title(self):
        md = """# Here's the Page

Test body copy for ya
"""
        title = extract_title(md)
        self.assertEqual(
            title,
            "Here's the Page")

    
