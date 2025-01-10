from src.textnode import TextType
from src.textnode import TextNode
from src.inline_markdown import split_nodes_delimiter

def main():
    nodes = [
            TextNode('Hello I am', TextType.TEXT),
            TextNode('*Nothing* but a **Simple MAN**', TextType.TEXT)
        ]
    
    
    result = split_nodes_delimiter(nodes, '*', TextType.ITALIC)
    # print("Results with Bold")
    print("Results without Bold")
    print('---------------------------------------')
    for res in result:
        print(res)
    print('---------------------------------------')

    nodes2 = split_nodes_delimiter(nodes, "**", TextType.BOLD)
    result2 = split_nodes_delimiter(nodes2, "*", TextType.ITALIC)
    print("Results with Bold")
    print('---------------------------------------')
    for res2 in result2:
        print(res2)
    print('---------------------------------------')
    

if __name__ == '__main__':
    main()
