"""
Create a main() function in main.py and call it.
The function should create a new TextNode object with some dummy values.
Print the object, and make sure it looks like you'd expect. For example, my code printed:
"""

from textnode import TextNode, TextType

def main():
    text_node = TextNode("This is some anchor text", TextType.LINK, "https://www.boot.dev")
    print(text_node)

if __name__ == "__main__":
    main()