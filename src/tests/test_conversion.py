import unittest
from src.ParentNode import ParentNode
from src.LeafNode import LeafNode
from src.converter import markdown_to_html_node

class TestConversion(unittest.TestCase):

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