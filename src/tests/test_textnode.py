import unittest

from src.leafnode import LeafNode
from src.textnode import TextNode, TextType

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.TEXT)
        node2 = TextNode("This is a text node", TextType.TEXT)
        self.assertEqual(node, node2)

    def test_eq_false(self):
        node = TextNode("This is a text node", TextType.TEXT)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_eq_false2(self):
        node = TextNode("This is a text node", TextType.TEXT)
        node2 = TextNode("This is a text node2", TextType.TEXT)
        self.assertNotEqual(node, node2)

    def test_eq_url(self):
        node = TextNode("This is a text node", TextType.ITALIC, "https://www.boot.dev")
        node2 = TextNode("This is a text node", TextType.ITALIC, "https://www.boot.dev")
        self.assertEqual(node, node2)

    def test_repr(self):
        node = TextNode("This is a text node", TextType.TEXT, "https://www.boot.dev")
        self.assertEqual(
            "TextNode(This is a text node, TextType.TEXT, https://www.boot.dev)", repr(node)
        )

    def test_textnode_tags(self):
        node = TextNode('Normal Text', TextType.TEXT)
        # tn = TextNode
        node2 = LeafNode(None, 'Normal Text')
        # self.assertEqual(tn.text_node_to_html_node(node), node2)
        self.assertEqual(node.text_node_to_html_node(), node2)

    def text_textnode_tags2(self):
        node = TextNode('Italic Text', TextType.ITALIC)
        # tn = TextNode
        node2 = LeafNode('i', 'Italic Text')
        # self.assertEqual(tn.text_node_to_html_node(node), node2)
        self.assertEqual(node.text_node_to_html_node(), node2)

    def text_textnode_tags3(self):
        node = TextNode('Image Text', TextType.IMAGE, 'www.imgur.com')
        # tn = TextNode
        node2 = LeafNode('img', '', {'src': 'www.imgur.com', 'alt': 'Image Text'})
        # self.assertEqual(tn.text_node_to_html_node(node), node2)
        self.assertEqual(node.text_node_to_html_node(), node2)

if __name__ == "__main__":
    unittest.main()

