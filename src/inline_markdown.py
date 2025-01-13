from src.textnode import TextNode, TextType

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    """
    Splits the nodes using a delimter and tags them with the specified text_type
    WARNING: In case of using Italic text type use BOLD first to remove '**' delimters that will interfere with the results
    @params:
    - old_nodes: List[TextNodes] -> A list of nodes that need to be split
    - delimiter: String -> A delimiter with which to break the TextNodes
    - text_type: Enum(TextType) -> An enum used to tag the resulting matching TextNodes

    @return: List[TextNodes] -> List of TextNodes split with the delimiter and tagged with the text_type

    """ 
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        split_nodes = []
        sections = old_node.text.split(delimiter)
        if len(sections) % 2 == 0:
            raise ValueError("Invalid markdown, formatted section not closed")
        for i in range(len(sections)):
            if sections[i] == "":
                continue
            if i % 2 == 0:
                split_nodes.append(TextNode(sections[i], TextType.TEXT))
            else:
                split_nodes.append(TextNode(sections[i], text_type))
            
        new_nodes.extend(split_nodes)
    return new_nodes

def extract_markdown_images(text):

    """
    Extract Alternate Text and links to markdown images and pack them in a tuple and return in a list

    @params:
    - text: String -> Text from which links to be extracted
    
    return: List[tuple(alt_text: str, link:str)]
    """

    start = text.find('!')
    if start == -1:
        return [()]

    