import unittest
from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_to_html(self):
        # Case 0: Single href prop
        node = HTMLNode(None, None, None, {"href": "https://www.boot.dev"})
        self.assertEqual(node.props_to_html(), "href=`https://www.boot.dev`")

        # Case 1: Single src prop
        node = HTMLNode(None, None, None, {"src": "https://www.boot.dev/image.png"})
        self.assertEqual(node.props_to_html(), "src=`https://www.boot.dev/image.png`")

        # Case 2: Multiple props
        node = HTMLNode(None, None, None, {"href": "https://www.boot.dev", "src": "https://www.boot.dev/image.png"})
        self.assertEqual(node.props_to_html(), "href=`https://www.boot.dev` src=`https://www.boot.dev/image.png`")

        # Case 3: No props
        node = HTMLNode(None, None, None, None)
        self.assertEqual(node.props_to_html(), "")

if __name__ == "__main__":
    unittest.main()