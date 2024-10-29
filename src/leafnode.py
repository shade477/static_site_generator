from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self, tag=None, value:str=None, props: dict = None) -> None:
        super().__init__(tag=tag, value=value, props=props)

    def to_html(self):
        if not self.value:
            raise ValueError("No value present")
        if not self.tag:
            return self.value
        return f'<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>'
