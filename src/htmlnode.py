class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props:dict=None) -> None:
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
        
    def to_html(self):
        raise NotImplementedError()

    def props_to_html(self):
        properties = ''
        if self.props:
            for prop in self.props:
                properties += f' {prop}="{self.props[prop]}"'
        return properties
    
    def __repr__(self):
        return f'HTMLNode({self.tag}, {self.value}, children: {self.children}, {self.props})'


