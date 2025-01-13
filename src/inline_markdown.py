import re
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

    # Create Empty list to store all new nodes
    new_nodes = []

    # Run through all the nodes in old nodes
    for old_node in old_nodes:
        # If old_node.text_type is not TextType.TEXT then it is already processed and thus ignored and appended
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue

        # Create empty list to store the split nodes
        split_nodes = []
        # Splitting the old_node.text using delimiter
        sections = old_node.text.split(delimiter)
        # if the length of sections is not even then the text is not enclosed properly
        if len(sections) % 2 == 0:
            raise ValueError("Invalid markdown, formatted section not closed")
        
        # Running through all the sections
        for i in range(len(sections)):
            # If its an empty string then it is ignored
            if sections[i] == "":
                continue
            # If the index of the section is even then it is an unenclosed text else it is an enclosed by delimiters. These are added to the return
            if i % 2 == 0:
                split_nodes.append(TextNode(sections[i], TextType.TEXT))
            else:
                split_nodes.append(TextNode(sections[i], text_type))
            
        new_nodes.extend(split_nodes)
    return new_nodes

def split_markdown_images(text):
    """
    Extract Alternate Text and links to markdown images and pack them in a tuple and return in a list

    @params:
    - text: String -> Text from which links to be extracted
    
    return: List[tuple(alt_text: str, link:str)]
    """
    pattern = r"!\[([^\[\]]*)\]\(([^\(\)]*)\)"
    matches = re.findall(pattern, text)
    return matches

def split_markdown_links(text):
    """
    Extract Alternate Text and links to pack them in a tuple and return in a list

    @params:
    - text: String -> Text from which links to be extracted
    
    return: List[tuple(alt_text: str, link:str)]
    """
    pattern = r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)"
    matches = re.findall(pattern, text)
    return matches