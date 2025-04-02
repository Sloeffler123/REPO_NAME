from enum import Enum
import re
from htmlnode import HTMLNode, ParentNode
from textnode import text_node_to_html_node, TextNode, TextType
from split_nodes import text_to_textnodes
class BlockType(Enum):
    PARAGRAPH = 'paragraph'
    HEADING = 'heading'
    CODE = 'code'
    QUOTE = 'quote'
    UNORDERED_LIST = 'unordered list'
    ORDERED_LIST = 'ordered list'


def block_to_block_type(markdown_block):
    global hashtags
    hashtags = markdown_block.count('#')
    split_lst = markdown_block.split('\n')
    
    if markdown_block[0:hashtags + 1] == '#' * hashtags + ' ':
        return BlockType.HEADING
    elif markdown_block[0:3] == '```' and markdown_block[-3:] == '```':
        return BlockType.CODE
    elif markdown_block[0:2] == '> ':
        for line in split_lst:
            if not line.startswith('> '):
                break
        return BlockType.QUOTE
    elif markdown_block[0:2] == '- ':
        for line in split_lst:
            if not line.startswith('- '):
                break
        return BlockType.UNORDERED_LIST
    elif markdown_block[0].isdigit():
        for line in split_lst:
            if not line[0].isdigit:
                break
        return BlockType.ORDERED_LIST
    else: return BlockType.PARAGRAPH




def markdown_to_blocks(markdown):
    blocks = []
    # Split by double newlines
    raw_blocks = markdown.split('\n\n')
    
    for block in raw_blocks:
        if block.strip():  # Skip empty blocks
            # Process each line in the block
            lines = block.strip().split('\n')
            cleaned_lines = [line.strip() for line in lines]
            # Rejoin the lines with single newlines
            cleaned_block = '\n'.join(cleaned_lines)
            blocks.append(cleaned_block)
    
    return blocks


def markdown_to_html_node(markdown):
    
    lst = []
    blocks = markdown_to_blocks(markdown)
    for block in blocks:
        block_type = block_to_block_type(block)
        if block_type == BlockType.PARAGRAPH:
            text_node = TextNode(text=block.replace('\n', ' '), text_type=TextType.TEXT)
            children = text_to_children([text_node])

            node = ParentNode(tag='p', children=children)
            lst.append(node)
        elif block_type == BlockType.HEADING:
            new_block = block.replace('#' * hashtags, '').replace('\n', ' ').strip()
            text_node = TextNode(text=new_block, text_type=TextType.TEXT)
            children = text_to_children([text_node])
            node = ParentNode(tag=f'h{hashtags}', children=children)
            lst.append(node)
        elif block_type == BlockType.CODE:
            code_content = code_content = "\n".join(block.split("\n")[1:])[:-1] if block.endswith("\n") else "\n".join(block.split("\n")[1:]).replace('```', '')
            text_node = TextNode(text=code_content, text_type=TextType.TEXT)
            code_child = text_node_to_html_node(text_node)
            code_node = ParentNode(tag='code', children=[code_child])
            pre_node = ParentNode(tag='pre', children=[code_node])
            lst.append(pre_node)
        elif block_type == BlockType.QUOTE:
            text_node = TextNode(text=block.replace('\n', ' ').replace('> ', ''), text_type=TextType.TEXT)
            children = text_to_children([text_node])
            node = ParentNode(tag='blockquote', children=children)  
            lst.append(node) 
        
        elif block_type == BlockType.ORDERED_LIST:
            lst.append(olist_to_html_node(block))
        elif block_type == BlockType.UNORDERED_LIST:
            lst.append(ulist_to_html_node(block))
            
            

    return ParentNode('div', lst)


def text_to_children(text):
    lst = []
    conversion = text_to_textnodes(text)
    
    for nodes in conversion:
        node = text_node_to_html_node(nodes)
        lst.append(node)
    return lst
    

def olist_to_html_node(block):
    items = block.split("\n")
    html_items = []
    for item in items:
        text = item[3:]
        text_node = TextNode(text, TextType.TEXT)
        children = text_to_children([text_node])
        html_items.append(ParentNode("li", children))
    return ParentNode("ol", html_items)


def ulist_to_html_node(block):
    items = block.split("\n")
    html_items = []
    for item in items:
        text = item[2:]
        text_node = TextNode(text, TextType.TEXT)
        children = text_to_children([text_node])
        html_items.append(ParentNode("li", children))
    return ParentNode("ul", html_items)


