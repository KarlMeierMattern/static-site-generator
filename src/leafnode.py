from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self, tag: str | None = None, value: str | None = None, props: dict[str, str] | None = None):
        super().__init__(tag, value, None, props)

    def to_html(self):

        if self.value is None:
            raise ValueError("Leaf node must have a value")

        if self.tag is None:
            return self.value
        
        return f"<{self.tag}{' ' if self.props else ''}{self.props_to_html()}>{self.value}</{self.tag}>"

    def __repr__(self):
        return f"LeafNode(tag={self.tag}, value={self.value}, props={self.props})"
