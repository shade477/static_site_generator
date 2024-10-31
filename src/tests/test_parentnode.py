import unittest

from leafnode import LeafNode
from parentnode import ParentNode
from leafnode import LeafNode

class TestParentNode(unittest.TestCase):
    def test_to_html(self):
        node = ParentNode("p",
                          [
                            LeafNode('b', 'Bold Text'),
                            LeafNode(value='Normal Text'),
                            LeafNode('a', 'Link', {'href': 'https://www.google.com'})
                          ], {'dummy': 'value'})
        # print(node)
        self.assertEqual(node.to_html(), '<p dummy="value"><b>Bold Text</b>Normal Text<a href="https://www.google.com">Link</a></p>')
    
    def test_to_html2(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )

        self.assertEqual('<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>', node.to_html())



    def test_repr(self):
        node = ParentNode('div', [LeafNode('i', 'Italic Text')]) 
        self.assertEqual(node, 'ParentNode("div", [LeafNode("i", "Italic Text")])')

    def test_no_children(self):
        with self.assertRaises(ValueError) as context:
            ParentNode('p')

        self.assertTrue('Invalid HTML: No children' in str(context.exception))

    def test_no_tag(self):
        with self.assertRaises(ValueError) as context:
            ParentNode(children={ 'href':'google.com' })

        self.assertTrue('Invalid HTML: No tag')


