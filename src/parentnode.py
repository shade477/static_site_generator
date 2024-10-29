from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag=None, children=None, props: dict = None) -> None:
        if not children:
            raise ValueError('No children Present')
        super().__init__(tag,None, children, props)

    def to_html(self):
        if not self.tag:
            raise ValueError('Invalid HTML: No tag')
        if not self.children:
            raise ValueError('Invalid HTML: No children')
        html = ''
        for child in self.children:
            html += child.to_html()

        return f'<{self.tag}{self.props_to_html()}>{html}</{self.tag}>'
    
    def __repr__(self):
        return f'ParentNode({self.tag}, {self.value}, {self.children}, {self.props})'
