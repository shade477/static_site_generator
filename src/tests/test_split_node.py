import unittest
from src.inline_markdown import split_nodes_delimiter
from src.textnode import TextNode, TextType

class TestSplitNodes(unittest.TestCase):
    def test_plain(self):
        node = [TextNode('This is plain text without delimiters', TextType.TEXT)]
        expected_arr = [TextNode('This is plain text without delimiters', TextType.TEXT)]

        node_arr = split_nodes_delimiter(node, '*', TextType.ITALIC)
        self.assertListEqual(expected_arr, node_arr)

    def test_plain2(self):
        node = [TextNode('This is a plain text with **bold and nice** delimiters', TextType.TEXT)]
        expected_arr = [TextNode('This is a plain text with ', TextType.TEXT),
                        TextNode('bold and nice', TextType.BOLD),
                        TextNode(' delimiters', TextType.TEXT)]

        node_arr = split_nodes_delimiter(node, '**', TextType.BOLD)
        # print(f'Plain2: {node_arr}')
        self.assertListEqual(node_arr, expected_arr)

    def test_plain3(self):
        node = [TextNode('This is a plain text with *Italic* delimiters', TextType.TEXT)]
        expected_arr = [TextNode('This is a plain text with ', TextType.TEXT),
                        TextNode('Italic', TextType.ITALIC),
                        TextNode(' delimiters', TextType.TEXT)]
        
        node_arr = split_nodes_delimiter(node, '*', TextType.ITALIC)
        # print('pass')
        self.assertListEqual(node_arr, expected_arr)

    def test_pre_plain(self):
        node = [TextNode('**Starts with BOLD** followed by normal and **then by bold**', TextType.TEXT)]
        expected_arr = [TextNode('Starts with BOLD', TextType.BOLD), 
                        TextNode(' followed by normal and ', TextType.TEXT), 
                        TextNode('then by bold', TextType.BOLD)]
        
        node_arr = split_nodes_delimiter(node, '**', TextType.BOLD)
        self.assertListEqual(node_arr, expected_arr)

    def test_multiple_nodes_italic(self):
        # Test processing of italic delimiters
        nodes = [
            TextNode('Hello I am', TextType.TEXT),
            TextNode('*Nothing* but a **Simple MAN**', TextType.TEXT)
        ]
        
        expected = [
            TextNode('Hello I am', TextType.TEXT),
            TextNode('Nothing', TextType.ITALIC),
            TextNode(' but a **Simple MAN**', TextType.TEXT)
        ]
        
        result = split_nodes_delimiter(nodes, '*', TextType.ITALIC)
        self.assertListEqual(result, expected)

    def test_multiple_nodes_bold(self):
        # Test processing of bold delimiters
        nodes = [
            TextNode('Hello I am', TextType.TEXT),
            TextNode('Nothing but a **Simple MAN**', TextType.TEXT)
        ]
        
        expected = [
            TextNode('Hello I am', TextType.TEXT),
            TextNode('Nothing but a ', TextType.TEXT),
            TextNode('Simple MAN', TextType.BOLD)
        ]
        
        result = split_nodes_delimiter(nodes, '**', TextType.BOLD)
        self.assertListEqual(result, expected)

    def test_error(self):
        node = [TextNode('Using invalid *texttype', TextType.TEXT)]
        with self.assertRaises(ValueError) as context:
            split_nodes_delimiter(node, '*', TextType.ITALIC)
        
        self.assertTrue("Invalid markdown, formatted section not closed" in str(context.exception))

    def test_adjacent_delimiter(self):
        node = [TextNode("text**bold**", TextType.TEXT)]
        expected_arr = [
            TextNode("text", TextType.TEXT),
            TextNode("bold", TextType.BOLD)
        ]
        
        result = split_nodes_delimiter(node, "**", TextType.BOLD)
        self.assertListEqual(result, expected_arr)

    def test_adjacent_delimiters(self):
        # Basic case
        node = [TextNode("text**bold**", TextType.TEXT)]
        expected_arr = [
            TextNode("text", TextType.TEXT),
            TextNode("bold", TextType.BOLD)
        ]
        result = split_nodes_delimiter(node, "**", TextType.BOLD)
        self.assertListEqual(result, expected_arr)

    def test_multiple_delimiters(self):
        # Multiple delimited sections
        node = [TextNode("a**b**c**d**", TextType.TEXT)]
        expected_arr = [
            TextNode("a", TextType.TEXT),
            TextNode("b", TextType.BOLD),
            TextNode("c", TextType.TEXT),
            TextNode("d", TextType.BOLD)
        ]
        result = split_nodes_delimiter(node, "**", TextType.BOLD)
        self.assertListEqual(result, expected_arr)