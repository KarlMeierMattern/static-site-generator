import unittest
from textnode import TextNode, TextType
from leafnode import LeafNode
from parentnode import ParentNode
from htmlnode import HTMLNode
from textnode_to_htmlnode import text_node_to_html_node
from split_nodes_delimiter import split_nodes_delimiter
from extract import extract_markdown_images, extract_markdown_links
from split_nodes import split_nodes_image, split_nodes_link
from text_to_textnode import text_to_textnodes

class TestHTMLNode(unittest.TestCase):

    def test_text_node(self):
        # Case 0: Text type and URL are the same
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

        # Case 1: Text type is different
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.TEXT)
        self.assertNotEqual(node, node2)

        # Case 2: URL is different
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD, "https://www.boot.dev")
        self.assertNotEqual(node, node2)

        # Case 3: URL is None (explicit vs default) — should be equal
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD, None)
        self.assertEqual(node, node2)

        # Case 4: Text type is different and URL is different
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.TEXT, "https://www.boot.dev")
        self.assertNotEqual(node, node2)

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

    def test_leafnode_to_html(self):
        # Case 0: No tag, no value -> should raise ValueError
        node = LeafNode(None, None)
        self.assertRaises(ValueError, node.to_html)

        # Case 1: No tag, value
        node = LeafNode(None, "This is a leaf node")
        self.assertEqual(node.to_html(), "This is a leaf node")

        # Case 2: Tag, no value
        node = LeafNode("p", None)
        self.assertRaises(ValueError, node.to_html)

        # Case 3: Tag, value, props
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(node.to_html(), "<a href=`https://www.google.com`>Click me!</a>")

    def test_to_html_with_children(self):
        # Case 0: No tag, no children -> should raise ValueError
        parent_node = ParentNode(None, None)
        self.assertRaises(ValueError, parent_node.to_html)

        # Case 1: Tag, no children -> should raise ValueError
        parent_node = ParentNode("div", None)
        self.assertRaises(ValueError, parent_node.to_html)

        # Case 2: Tag, children
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")
    
    def test_to_html_with_grandchildren(self):
        # Case 0: No tag, no grandchildren -> should raise ValueError
        parent_node = ParentNode(None, None)
        self.assertRaises(ValueError, parent_node.to_html)

        # Case 1: Tag, no grandchildren -> should raise ValueError
        parent_node = ParentNode("div", None)
        self.assertRaises(ValueError, parent_node.to_html)

        # Case 2: Tag, grandchildren
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(),"<div><span><b>grandchild</b></span></div>",)

        # Case 3: Tag, grandchildren, nested
        nested_child_node_1 = LeafNode("li", "item 1")
        nested_child_node_2 = LeafNode("li", "item 2")
        nested_parent_node = ParentNode("ol", [nested_child_node_1, nested_child_node_2])
        child_node = ParentNode("ul", [nested_parent_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(),"<div><ul><ol><li>item 1</li><li>item 2</li></ol></ul></div>")

    def test_split_nodes_image(self):
        # Case 0: No images -> return empty list
        nodes = [TextNode("This is a text node", TextType.TEXT)]
        self.assertEqual(split_nodes_image(nodes), [TextNode("This is a text node", TextType.TEXT)])

        # Case 1: Images found
        nodes = [TextNode("This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)", TextType.TEXT)]
        self.assertEqual(split_nodes_image(nodes), [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("rick roll", TextType.IMAGE, "https://i.imgur.com/aKaOqIh.gif"),
            TextNode(" and ", TextType.TEXT),
            TextNode("obi wan", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
        ])

    def test_split_nodes_link(self):
        # Case 0: No links -> return empty list
        nodes = [TextNode("This is a text node", TextType.TEXT)]
        self.assertEqual(split_nodes_link(nodes), [TextNode("This is a text node", TextType.TEXT)])

        # Case 1: Links found
        nodes = [TextNode("This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)", TextType.TEXT)]
        self.assertEqual(split_nodes_link(nodes), [
            TextNode("This is text with a link ", TextType.TEXT),
            TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
            TextNode(" and ", TextType.TEXT),
            TextNode("to youtube", TextType.LINK, "https://www.youtube.com/@bootdotdev"),
        ])

    def test_split_nodes_delimiter(self):
        # Case 0: Unclosed delimiter -> raise
        nodes = [TextNode("This is | a text node", TextType.TEXT)]
        self.assertRaises(ValueError, split_nodes_delimiter, nodes, "|", TextType.BOLD)

        # Case 1: No delimiter -> return node as-is
        nodes = [TextNode("This is a text node", TextType.TEXT)]
        self.assertEqual(split_nodes_delimiter(nodes, "|", TextType.BOLD), [TextNode("This is a text node", TextType.TEXT)])

        # Case 2: Delimiter found
        old_nodes = [TextNode("Plain start. ", TextType.TEXT), TextNode("**bold phrase**", TextType.TEXT), TextNode(" end.", TextType.TEXT)]
        self.assertEqual(split_nodes_delimiter(old_nodes, "**", TextType.BOLD), [TextNode("Plain start. ", TextType.TEXT), TextNode("bold phrase", TextType.BOLD), TextNode(" end.", TextType.TEXT)])

         # Case 3: Delimiter found
        old_nodes = [TextNode("Plain start **bold phrase** end", TextType.TEXT)]
        self.assertEqual(split_nodes_delimiter(old_nodes, "**", TextType.BOLD), [TextNode("Plain start ", TextType.TEXT), TextNode("bold phrase", TextType.BOLD), TextNode(" end", TextType.TEXT)])
    

    def test_extract_markdown_images(self):
        # Case 0: No images -> return empty list
        text = "This is a text node"
        self.assertEqual(extract_markdown_images(text), [])

        # Case 1: Images found
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        self.assertEqual(extract_markdown_images(text), [("rick roll", "https://i.imgur.com/aKaOqIh.gif"), ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")])

    def test_extract_markdown_links(self):
        # Case 0: No links -> return empty list
        text = "This is a text node"
        self.assertEqual(extract_markdown_links(text), [])

        # Case 1: Links found
        text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        self.assertEqual(extract_markdown_links(text), [("to boot dev", "https://www.boot.dev"), ("to youtube", "https://www.youtube.com/@bootdotdev")])

    def test_text_to_textnodes(self):
        # Case 0: No text -> return empty list
        text = ""
        self.assertEqual(text_to_textnodes(text), [])

        # Case 1: Text found
        text = "This is text with a **bold phrase** and a [link](https://www.boot.dev)"
        self.assertEqual(text_to_textnodes(text), [TextNode("This is text with a ", TextType.TEXT), TextNode("bold phrase", TextType.BOLD), TextNode(" and a ", TextType.TEXT), TextNode("link", TextType.LINK, "https://www.boot.dev")])

if __name__ == "__main__":
    unittest.main()