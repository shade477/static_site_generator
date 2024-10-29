import unittest
from leafnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_child_test(self) -> None:
        node = LeafNode('p', 'Paragraph of text')
        self.assertEqual(node.to_html(), '<p>Paragraph of text</p>')
        
    def test_child_prop(self) -> None:
        node = LeafNode('a', 'Button', {'href':'https://www.google.com'})
        self.assertEqual(node.to_html(), '<a href="https://www.google.com">Button</a>')

    def test_value_error(self) -> None:
        with self.assertRaises(ValueError) as context: 
            LeafNode('a', value=None)
                     
        self.assertTrue('No value present' in str(context.exception))

    def test_no_value(self) -> None:
        node = LeafNode(value="No tag check")
        self.assertEqual(node.to_html(), 'No tag check')
