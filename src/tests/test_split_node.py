import unittest
from src.inline_markdown import split_nodes_delimiter, split_nodes_image, split_nodes_link, text_to_textnodes
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
            TextNode(' but a ', TextType.TEXT),
            TextNode('Simple MAN', TextType.BOLD)
        ]
        nodes2 = split_nodes_delimiter(nodes, '**', TextType.BOLD)
        result = split_nodes_delimiter(nodes2, '*', TextType.ITALIC)
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

    def test_node_image(self):
        node = [TextNode("This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)", TextType.TEXT)]
        expected_arr = [
            TextNode('This is text with a ', TextType.TEXT),
            TextNode('rick roll', TextType.IMAGE, 'https://i.imgur.com/aKaOqIh.gif'),
            TextNode(' and ', TextType.TEXT),
            TextNode('obi wan', TextType.IMAGE, 'https://i.imgur.com/fJRm4Vk.jpeg')
        ]

        result = split_nodes_image(node)

        self.assertListEqual(result, expected_arr)

    def test_node_link(self):
        node = [
            TextNode("This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)", TextType.TEXT)
        ]
        expected_arr = [
            TextNode('This is text with a link ', TextType.TEXT),
            TextNode('to boot dev', TextType.LINK, 'https://www.boot.dev'),
            TextNode(' and ', TextType.TEXT),
            TextNode('to youtube', TextType.LINK, 'https://www.youtube.com/@bootdotdev')
        ]

        result = split_nodes_link(node)

        self.assertListEqual(result, expected_arr)

    def test_node_image_normal(self):
        node = [
            TextNode('This is normal text that does not contain any link', TextType.TEXT)
        ]
        expected_arr = [
            TextNode('This is normal text that does not contain any link', TextType.TEXT)
        ]

        result = split_nodes_image(node)
        self.assertListEqual(result, expected_arr)

    def test_node_link_normal(self):
        node = [
            TextNode('This is normal text that does not contain any link', TextType.TEXT)
        ]
        expected_arr = [
            TextNode('This is normal text that does not contain any link', TextType.TEXT)
        ]
        result = split_nodes_link(node)
        self.assertListEqual(result, expected_arr)

    def test_node_link_postfix(self):
        node = [
            TextNode("This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev) with ending text", TextType.TEXT)
        ]
        expected_arr = [
            TextNode('This is text with a link ', TextType.TEXT),
            TextNode('to boot dev', TextType.LINK, 'https://www.boot.dev'),
            TextNode(' and ', TextType.TEXT),
            TextNode('to youtube', TextType.LINK, 'https://www.youtube.com/@bootdotdev'),
            TextNode(' with ending text', TextType.TEXT)
        ]
        result = split_nodes_link(node)
        self.assertListEqual(result, expected_arr)

    def test_text_to_node_normal(self):
        text = 'This is **text** with an *italic* word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)'
        expected_arr = [
            TextNode("This is ", TextType.TEXT),
            TextNode("text", TextType.BOLD),
            TextNode(" with an ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" word and a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" and an ", TextType.TEXT),
            TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
            TextNode(" and a ", TextType.TEXT),
            TextNode("link", TextType.LINK, "https://boot.dev"),
        ]

        result = text_to_textnodes(text)
        self.assertListEqual(result, expected_arr)