import unittest
from src.blocks_markdown import markdown_to_blocks, block_to_block_type
from src.BlockType import BlockType

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

    def test_block_head(self):
        text = '## Heading 2'
        expected = BlockType.HEADING2

        result = block_to_block_type(text)

        self.assertEqual(result, expected)

    def test_block_head2(self):
        text = '####### Heading 6'
        expected = BlockType.HEADING6
        result = block_to_block_type(text)

        self.assertEqual(result, expected)

    def test_block_code(self):
        text = """```
        Code Block
        hello
        ```"""
        expected = BlockType.CODE
        result = block_to_block_type(text)
        self.assertEqual(result, expected)
        
    # def test_block_code_err(self):
    #     text = """```
    #     Code Block
    #     hello
    #     """
    #     with self.assertRaises(Exception) as ctx:
    #         block_to_block_type(text)
    #     self.assertTrue("Code block not enclosed" in str(ctx.exception))

    def test_block_quote(self):
        text = """> Hesitation is defeat
> If the heroes run away, who's left to help?"""
        expected = BlockType.QUOTE
        result = block_to_block_type(text)
        self.assertEqual(result, expected)
        
#     def test_block_quote_err(self):
#         text = """> Hesitation is defeat
# If the heroes run away, who's left to help?"""
#         with self.assertRaises(Exception) as ctx:
#             block_to_block_type(text)
#         self.assertTrue('Quote line not start with ">"' in str(ctx.exception))

    def test_block_unordered1(self):
        text = """- item 1
- item 2"""
        expected = BlockType.UNORDERED
        result = block_to_block_type(text)
        self.assertEqual(result, expected)

    def test_block_unordered2(self):
        text = """* item 1
* item 2"""
        expected = BlockType.UNORDERED
        result = block_to_block_type(text)
        self.assertEqual(result, expected)

#     def test_block_unordered_mix(self):
#         text = """- item 1
# - item 2
# * item 3"""
#         with self.assertRaises(Exception) as ctx:
#             block_to_block_type(text)
        
#         self.assertTrue('Unordered lines not good' in str(ctx.exception))

#     def test_block_unordered_bad(self):
#         text = """- item 1
# - item 2
# item 3"""
#         with self.assertRaises(Exception) as ctx:
#             block_to_block_type(text)
        
#         self.assertTrue('Unordered lines not good' in str(ctx.exception))

    def test_block_ordered(self):
        text = """1. item 1
2. item 2
3. item"""
        expected = BlockType.ORDERED
        result = block_to_block_type(text)
        self.assertEqual(result, expected)
    
#     def test_block_ordered_bad(self):
#         text = """1. item 1
# 2. item 2
# item 3"""
#         with self.assertRaises(Exception) as ctx:
#             block_to_block_type(text)
#         self.assertTrue('Line does not start with a number and a period' in str(ctx.exception))

#     def test_block_ordered_numbering(self):
#         text = """1. item 1
# 2. item 2
# 4. item 3"""
#         with self.assertRaises(Exception) as ctx:
#             block_to_block_type(text)
#         self.assertTrue("Bad numbering" in str(ctx.exception))

    def test_block_paragraph(self):
        text = """Just a normal paragraph with multiple lines
        lol lolol"""
        expected = BlockType.PARAGRAPH
        result = block_to_block_type(text)
        self.assertEqual(result, expected)