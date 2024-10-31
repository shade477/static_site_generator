from src.textnode import TextType
from src.textnode import TextNode

def main():
    print(TextNode('This is a text node', TextType.BOLD, 'https://www.boot.dev'))

if __name__ == '__main__':
    main()
