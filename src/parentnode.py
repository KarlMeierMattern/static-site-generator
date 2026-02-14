from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag: str | None = None, children: list["HTMLNode"] | None = None, props: dict[str, str] | None = None):
        super().__init__(tag, None, children, props)
    
    def to_html(self):
        if self.tag is None:
            raise ValueError("Parent node must have a tag")

        if self.children is None:
            raise ValueError("Parent node must have children")

        # Otherwise, return a string representing the HTML tag of the node and its children. This should be a recursive method (each recursion being called on a nested child node).
        return f"<{self.tag}{' ' if self.props else ''}{self.props_to_html()}>{''.join([child.to_html() for child in self.children])}</{self.tag}>"

    def __repr__(self):
        return f"ParentNode(tag={self.tag}, children={self.children}, props={self.props})"