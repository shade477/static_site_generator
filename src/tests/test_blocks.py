import unittest
from blocks_markdown import markdown_to_blocks

class TestBlocks(unittest.TestCase):
    def test_mark_to_block(self):
        text = """# This is a heading

This is a paragraph of text. It has some **bold** and *italic* words inside of it.

* This is the first list item in a list block
* This is a list item
* This is another list item"""
        expected_arr = [
            '# This is a heading',
            'This is a paragraph of text. It has some **bold** and *italic* words inside of it.',
            '* This is the first list item in a list block\n* This is a list item\n* This is another list item'
        ]
        result = markdown_to_blocks(text)
        self.assertListEqual(result, expected_arr)

    def test_mark_to_block_blank_lines(self):
        text = "block1\n\n\n\nblock2"
        expected_arr = [
            'block1',
            'block2'
        ]
        result = markdown_to_blocks(text)

        self.assertListEqual(result, expected_arr)