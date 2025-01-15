from src.textnode import TextType
from src.textnode import TextNode
from src.inline_markdown import text_to_textnodes

def main():
    nodes = text_to_textnodes("This is **text** with an *italic* word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)")
    for node in nodes:
        print(node)

if __name__ == '__main__':
    main()
