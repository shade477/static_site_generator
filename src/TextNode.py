from enum import Enum
from src.LeafNode import LeafNode
from src.TextType import TextType

class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self,node):
        return (self.text == node.text and
            self.text_type == node.text_type and
                self.url == node.url)

    def __repr__(self) -> str:
        return f'TextNode("{self.text}", {self.text_type}, {self.url})'


    def text_node_to_html_node(self):
        match self.text_type:
            case TextType.TEXT:
                return LeafNode(None, self.text)
            case TextType.BOLD:
                return LeafNode('b', self.text)
            case TextType.ITALIC:
                return LeafNode('i', self.text)
            case TextType.CODE:
                return LeafNode('code', self.text)
            case TextType.LINK:
                return LeafNode('a', self.text, {'href': self.url})
            case TextType.IMAGE:
                return LeafNode('img', '', {'src': self.url, 'alt': self.text})
            case _:
                raise Exception('Invalid Text_Type')
