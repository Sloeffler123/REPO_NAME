from textnode import TextNode, TextType


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    
    text_type_lst = []
    
    result = ''
    text_type_result = ''
    nodes = old_nodes[0].text.split()
    for node in nodes:
        if delimiter in node:
            text_type_result += ' ' + node 
            if result != '':
                text_type_lst.append(TextNode(text=result, text_type=TextType.TEXT))
                result = ''
        else:
            result += node + ' '

    
    
    text_type_lst.append(TextNode(text=text_type_result.strip(delimiter), text_type=text_type))
    text_type_lst.append(TextNode(text=result, text_type=TextType.TEXT))
    return text_type_lst
    # text_type_lst.append(TextNode(text=))
            













