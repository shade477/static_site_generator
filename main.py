from src.TextType import TextType
from src.TextNode import TextNode
from src.inline_markdown import markdown_to_blocks

def main():
    text = """# This is a heading

This is a paragraph of text. It has some **bold** and *italic* words inside of it.

* This is the first list item in a list block
* This is a list item
* This is another list item"""
    print(markdown_to_blocks(text))

if __name__ == '__main__':
    main()
