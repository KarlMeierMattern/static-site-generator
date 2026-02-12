import unittest
from leafnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_to_html(self):
        # Case 0: No tag, no value
        node = LeafNode(None, None)
        self.assertRaises(ValueError, node.to_html)

        # Case 1: No tag, with value
        node = LeafNode(None, "This is a leaf node")
        self.assertEqual(node.to_html(), "This is a leaf node")

        node = LeafNode("p", None)
        self.assertRaises(ValueError, node.to_html)

        # Case 1: No tag, with value
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(node.to_html(), "<a href=`https://www.google.com`>Click me!</a>")

if __name__ == "__main__":
    unittest.main()