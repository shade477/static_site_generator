from textnode import TextType
from textnode import TextNode

def main():
    print(TextNode('This is a text node', TextType.BOLD, 'https://www.boot.dev'))

if __name__ == '__main__':
    main()
