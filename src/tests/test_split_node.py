import unittest
from src.splits import split_nodes_delimiter
from src.textnode import TextNode, TextType

class TestSplitNodes(unittest.TestCase):
    def test_plain(self):
        node = [TextNode('This is plain text without delimiters', TextType.TEXT)]
        expected_arr = [TextNode('This is plain text without delimiters', TextType.TEXT)]

        node_arr = split_nodes_delimiter(node, '*', TextType.ITALIC)
        self.assertEqual(expected_arr, node_arr)

    def test_plain2(self):
        node = [TextNode('This is a plain text with **bold and nice** delimiters', TextType.TEXT)]
        expected_arr = [TextNode('This is a plain text with ', TextType.TEXT),
                        TextNode('bold and nice', TextType.BOLD),
                        TextNode(' delimiters', TextType.TEXT)]

        node_arr = split_nodes_delimiter(node, '**', TextType.BOLD)
        self.assertEqual(node_arr, expected_arr)

    def test_pre_plain(self):
        node = [TextNode('**Starts with BOLD** followed by normal and **then by bold**', TextType.TEXT)]
        expected_arr = [TextNode('Starts with BOLD', TextType.BOLD), 
                        TextNode(' followed by normal and ', TextType.TEXT), 
                        TextNode('then by bold', TextType.BOLD)]
        
        node_arr = split_nodes_delimiter(node, '**', TextType.BOLD)
        self.assertEqual(node_arr, expected_arr)

    def test_multiple(self):
        node = [TextNode('Hello I am', TextType.TEXT),
                TextNode('*Nothing* but a **Simple MAN**', TextType.TEXT)]
        expected_arr = [TextNode('Hello I am', TextType.TEXT),
                        TextNode('Nothing', TextType.ITALIC),
                        TextNode(' but a **Simple MAN**', TextType.TEXT)]
        
        node_arr = split_nodes_delimiter(node, '*', TextType.ITALIC)
        self.assertEqual(node_arr, expected_arr)

    def test_error(self):
        node = [TextNode('Using invalid *texttype', TextType.TEXT)]
        with self.assertRaises(Exception) as context:
            split_nodes_delimiter(node, '*', TextType.ITALIC)
        
        self.assertTrue("Invalid Markdown: Missing ending '*'" in str(context.exception))