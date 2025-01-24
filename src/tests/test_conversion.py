import unittest
from src.ParentNode import ParentNode
from src.LeafNode import LeafNode
from src.converter import markdown_to_html_node

class TestConversion(unittest.TestCase):

    def test_markdown_paragraph(self):
        text = """Hello this is a normal paragraph with **Bold** text"""
        expected = ParentNode('div', [
            ParentNode('p', [
                LeafNode('p', 'Hello this is a normal paragraph with '),
                LeafNode('b', 'Bold'),
                LeafNode('p', ' text')
            ])
        ])
        result = markdown_to_html_node(text)
        self.assertEqual(result, expected)
    
    def test_markdown_head(self):
        text = """# h1 Heading

## h2 Heading"""
        expected = ParentNode('div', [
            LeafNode('h1', 'h1 Heading'),
            LeafNode('h2', 'h2 Heading')
        ])
        result = markdown_to_html_node(text)
        self.assertEqual(result, expected)

    def test_markdown_quote(self):
        text = """> quote 1 text
> quote 2 text"""
        expected = ParentNode('div', [
            LeafNode('quote', """quote 1 text
quote 2 text"""
                     )
        ])
        result = markdown_to_html_node(text)
        self.assertEqual(result, expected)

    def test_markdown_code(self):
        text = """```
def Hello():
    print("Hello")
```"""
        expected = ParentNode('div', [
            LeafNode('code', """
def Hello():
    print("Hello")
""")
        ])
        result = markdown_to_html_node(text)
        self.assertEqual(result, expected)

    def test_markdown_unordered(self):
        text = """- item 1
- item 2"""
        expected = ParentNode('div', [
            ParentNode('ul', [
                LeafNode('li', 'item 1'),
                LeafNode('li', 'item 2')
            ])
        ])
        result = markdown_to_html_node(text)
        self.assertEqual(result, expected)

    def test_markdown_unordered_nested(self):
        text = """- item 1
- item 2 with **Bold Text**"""
        expected = ParentNode('div', [
            ParentNode('ul', [
                LeafNode('li', 'item 1'),
                ParentNode('li', [
                    LeafNode('', 'item 2 with '),
                    LeafNode('b', 'Bold Text')
                ])
            ])
        ])
        result = markdown_to_html_node(text)
        self.assertEqual(result, expected)

    def test_markdown_ordered(self):
        text = """1. item 1
2. item 2"""
        expected = ParentNode('div', [
            ParentNode('ol', [
                LeafNode('li', 'item 1'),
                LeafNode('li', 'item 2')
            ])
        ])
        result = markdown_to_html_node(text)
        self.assertEqual(result, expected)

    def test_markdown_ordered_nested(self):
        text = """1. item 1
2. item 2 with *markdown text*"""
        expected = ParentNode('div', [
            ParentNode('ol', [
                LeafNode('li', 'item 1'),
                ParentNode('li', [
                    LeafNode('', 'item 2 with '),
                    LeafNode('i', 'markdown text')
                ])
            ])
        ])
        result = markdown_to_html_node(text)
        self.assertEqual(result, expected)

    def test_normal_markdown(self):
        text = """
# This is h1 heading

## This is h2 heading

### This is h3 heading

#### This is h4 heading

##### This is h5 heading

###### This is h6 heading

####### This heading should be marked as a h6

Hello this a basic markdown paragraph with multiple lines
this text is used for testing purpose only and should not be used for any other purpose
following will have other type of markdown texts

```
def hello():
    print("Hello")
```

> Hesitation is defeat
> If the heroes run away then who is there to help?

- unordered item1
- unordered item2
- unordered item3

1. ordered item1
2. ordered item2
3. ordered item3

This paragraph will contain multiple inline markdown texts. The function `test_normal_markdown` should be able
to **identify** these inline markdown and *tag* them with the appropritate tags. If anything does not work [google](www.google.com). Internet connection is not
necessary to view this dummy ![image link](https://imgur.link.testimage)
"""
        expected = ParentNode(
            'div',
            [
                LeafNode('h1', 'This is h1 heading'),
                LeafNode('h2', 'This is h2 heading'), 
                LeafNode('h3', 'This is h3 heading'),
                LeafNode('h4', 'This is h4 heading'),
                LeafNode('h5', 'This is h5 heading'),
                LeafNode('h6', 'This is h6 heading'),
                LeafNode('h6', 'This heading should be marked as a h6'),
                LeafNode('p', """Hello this a basic markdown paragraph with multiple lines
this text is used for testing purpose only and should not be used for any other purpose
following will have other type of markdown texts"""),
                LeafNode('code',"""
def hello():
    print("Hello")
"""),
                LeafNode('quote', """Hesitation is defeat
If the heroes run away then who is there to help?"""),
                ParentNode('ul', [
                    LeafNode('li', 'unordered item1'),
                    LeafNode('li', 'unordered item2'),
                    LeafNode('li', 'unordered item3')
                    ]),
                ParentNode('ol', [
                    LeafNode('li', 'ordered item1'),
                    LeafNode('li', 'ordered item2'),
                    LeafNode('li', 'ordered item3')
                    ]),
                ParentNode('div', [
                        LeafNode('p', 'This paragraph will contain multiple inline markdown texts. The function '), 
                        LeafNode('code', 'test_normal_markdown'), 
                        LeafNode('p', """ should be able
to """), 
                        LeafNode('b', 'identify'), 
                        LeafNode('p',  ' these inline markdown and '), LeafNode('i', 'tag'), 
                        LeafNode('p',  ' them with the appropritate tags. If anything does not work '), 
                        LeafNode('a', 'google', {
                                'href': 'www.google.com'}), 
                        LeafNode('p', """. Internet connection is not
necessary to view this dummy """), 
                        LeafNode('img', 'image link', {'src': 'https://imgur.link.testimage'})
                         ])
            ])
        result = markdown_to_html_node(text)
        self.assertEqual(result, expected)