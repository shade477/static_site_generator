import unittest
from leafnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_child_test(self):
        node = LeafNode('p', 'Paragraph of text')
        self.assertEqual(node.to_html(), '<p>Paragraph of text</p>')
        
    def test_child_prop(self):
        node = LeafNode('a', 'Button', {'href':'https://www.google.com'})
        self.assertEqual(node.to_html(), '<a href="https://www.google.com">Button</a>')

    # def test_value_error(self):
    #
    #     with self.assertRaises(ValueError) as context: 
    #         node = LeafNode('a')
    #
    #     self.assertTrue('No value present' in str(context.exception))

    def test_no_value(self):
        node = LeafNode(value="No value check")
        self.assertEqual(node.to_html(), 'No value check')
