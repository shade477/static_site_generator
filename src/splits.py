from src.textnode import TextNode, TextType

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    
    for node in old_nodes:
        
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue

        text = node.text
        l = 0
        while l < len(text):
            opening = text.find(delimiter, l)
            if opening == -1:
                
                if text[l:]:
                    new_nodes.append(TextNode(text[l:], TextType.TEXT))
                break


            if opening <= len(text) - (2 * len(delimiter)) and text[opening:opening+len(delimiter)] == text[opening+len(delimiter):opening+(2*len(delimiter))]:
                l = opening + len(delimiter)
                l = text.find(delimiter, l) + len(delimiter)
                continue
            
            closing = text.find(delimiter, opening+len(delimiter))

            if closing == -1 or (closing < len(text)-len(delimiter) and text[closing+len(delimiter)] == text[closing]):
                raise Exception('Invalid Markdown: Missing ending delimiter')
            
            before = text[l:opening]
            
            after = text[opening+len(delimiter): closing]
            l = closing + len(delimiter)

            if before:
                new_nodes.append(TextNode(before, TextType.TEXT))
            
            new_nodes.append(TextNode(after, text_type))
        

    return new_nodes
            
        