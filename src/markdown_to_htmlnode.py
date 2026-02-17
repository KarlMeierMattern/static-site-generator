from split_blocks import markdown_to_blocks
from block_type import block_to_block_type, BlockType
from parentnode import ParentNode
from textnode import TextNode, TextType
from textnode_to_htmlnode import text_node_to_html_node
from text_to_textnode import text_to_textnodes

def text_to_children(text: str) -> list:
    """Convert inline markdown string to list of HTMLNode (LeafNode) children."""
    text_nodes = text_to_textnodes(text)
    return [text_node_to_html_node(tn) for tn in text_nodes]

def markdown_to_html_node(markdown: str) -> ParentNode:
    split_blocks = markdown_to_blocks(markdown)
    parent_node = ParentNode("div", [])
    for block in split_blocks:
        block_type = block_to_block_type(block)
        if block_type == BlockType.HEADING:
            n = 0
            while n < len(block) and block[n] == "#":
                n += 1
            inner = block[n:].lstrip()
            children = text_to_children(inner)
            parent_node.children.append(ParentNode(f"h{n}", children))
        elif block_type == BlockType.CODE:
            content = block.strip("`").strip()
            code_leaf = text_node_to_html_node(TextNode(content, TextType.CODE))
            parent_node.children.append(ParentNode("pre", [code_leaf]))
        elif block_type == BlockType.QUOTE:
            lines = [line.lstrip("> ").lstrip(">") for line in block.split("\n")]
            inner = " ".join(lines)
            children = text_to_children(inner)
            parent_node.children.append(ParentNode("blockquote", children))
        elif block_type == BlockType.UNORDERED_LIST:
            items = [line[2:].strip() for line in block.split("\n")]
            li_nodes = [ParentNode("li", text_to_children(item)) for item in items]
            parent_node.children.append(ParentNode("ul", li_nodes))
        elif block_type == BlockType.ORDERED_LIST:
            items = []
            for line in block.split("\n"):
                idx = line.find(". ")
                items.append(line[idx + 2 :].strip() if idx >= 0 else line)
            li_nodes = [ParentNode("li", text_to_children(item)) for item in items]
            parent_node.children.append(ParentNode("ol", li_nodes))
        else:
            children = text_to_children(block)
            parent_node.children.append(ParentNode("p", children))
    return parent_node