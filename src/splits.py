from src.textnode import TextNode

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []

    # Iterate through the node list
    for node in old_nodes:
        text = node.text
        l = 0 
        while l < len(text):
            opening = text.find(delimiter, l)
            if opening == -1:
                # no more delimiters are found   
                new_nodes.append(TextNode(text[l:], node.text_type))
                break

            closing = text.find(delimiter, opening + len(delimiter))
            if closing == -1:
                # no closing delimiter is found
                raise Exception(f"Invalid Markdown: Missing ending '{delimiter}'")
                
            # text to add between l and opening?
            if text[l:opening]:
                new_nodes.append(TextNode(text[l:opening], node.text_type))
            # text to add between opening and closing
            new_nodes.append(TextNode(text[opening + len(delimiter):closing], text_type))
            
            l = closing + len(delimiter)

    return new_nodes            
        
    # Not Optimized
    ###################################
    #     substr = text[:index]
    #     if substr:
    #         new_nodes.append(TextNode(substr, node.text_type))
    #     while True:
    #         index = text.find(delimiter, l)
    #         if index != -1:
    #             substr = text[l:index]
    #             if substr:
    #                 new_nodes.append(TextNode(substr, node.text_type))
    #             l = index + len(delimiter)
    #             index = text.find(delimiter, l)
                
    #             if index == -1:
    #                 raise Exception(f"Invalid Markdown: Missing ending '{delimiter}'")
    #             new_nodes.append(TextNode(text[l:index], text_type))
    #             l = index + len(delimiter)
    #         else:
    #             substr = text[l:]
    #             if substr:
    #                 new_nodes.append(TextNode(substr, node.text_type))
    #             break
    # return new_nodes


        # # To mark Delimiter appearance
        # flag = 0
        # index = 0
        # count = 0
        # # Iterate throught the text index
        # for c in range(len(text)):
        #     # Look for delimiter
        #     if text[c+len(delimiter)-1] == delimiter:

        #         # If there is text before the delimiter
        #         if not count:
        #             count = 0
        #             new_nodes.append(TextNode(text[c-count:c], node.text_type))

        #         # If the delimiter appears again
        #         if flag == 1:
        #             flag = 0
        #             new_nodes.append(TextNode(text[index:c], text_type))
        #             index = c+1
        #         else:
        #             index = c + 1
        #             flag = 1
        #         continue

        #     count += 1
        
        # if flag == 1:
        #     raise Exception('Invalid Markdown: Missing delimiter')
        # if not count:
        #     new_nodes.append(TextNode(text[index:], node.text_type))
            
        
            
        