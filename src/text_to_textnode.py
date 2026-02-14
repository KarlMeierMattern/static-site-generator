# Time to put all the "splitting" functions together into a function that can convert a raw string of markdown-flavored text into a list of TextNode objects.

from textnode import TextNode, TextType
from split_nodes import split_nodes_image, split_nodes_link
from split_nodes_delimiter import split_nodes_delimiter

def text_to_textnodes(text):
    nodes = [TextNode(text, TextType.TEXT)]
    nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
    nodes = split_nodes_delimiter(nodes, "_", TextType.ITALIC)
    nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)
    return nodes