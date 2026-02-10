from enum import Enum

"""
text (plain)
**Bold text**
_Italic text_
`Code text`
Links, in this format: [anchor text](url)
Images, in this format: ![alt text](url)
"""

class TextType(Enum):
    TEXT = "text"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"

class TextNode:
    def __init__(self, text: str, text_type: TextType, url: str = None):
        self.text = text
        self.text_type = text_type
        self.url = url

    """
    Create an __eq__ method on TextNode that compares self to another TextNode instance (other) and returns True if all of their properties are equal. Our future unit tests will rely on this method to compare objects.
    Create a __repr__ method that returns a string representation of the TextNode object. It should look like this:
    "TextNode(text='Hello, World!', text_type='text', url=None)"
    """

    def __eq__(self, other):
        return self.text == other.text and self.text_type == other.text_type and self.url == other.url

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"