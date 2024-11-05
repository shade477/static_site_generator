from src.textnode import TextNode, TextType

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    print('--------------------------')
    print('Split Module')
    print(f'Inputs:\n{old_nodes}\n{delimiter}\n{text_type}')
    print('--------------------------------')
    for old_node in old_nodes:
        print('--------------------')
        print(f'old node: {old_node}')
        print('-----------------------------')
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        split_nodes = []
        sections = old_node.text.split(delimiter)
        print('----------------------------------')
        print(f'SECTIONS:')
        print(f'{sections}')
        print('-----------------------------------')
        if len(sections) % 2 == 0:
            raise ValueError("Invalid markdown, formatted section not closed")
        for i in range(len(sections)):
            if sections[i] == "":
                continue
            print('-------------------------------------')
            print(f'Current loop: {i}')
            if i % 2 == 0:
                
                print(f'Current Text Section: {i}')
                print(f'Contents of Text section {i}: {sections[i]}')
                split_nodes.append(TextNode(sections[i], TextType.TEXT))
            else:
                
                print(f'Current {text_type} section: {i}')
                print(f'Contents of {text_type} section {i}: {sections[i]}')
                split_nodes.append(TextNode(sections[i], text_type))
            print('---------------------------------------')
            
        new_nodes.extend(split_nodes)
    return new_nodes