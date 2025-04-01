from enum import Enum

class BlockType(Enum):
    PARAGRAPH = 'paragraph'
    HEADING = 'heading'
    CODE = 'code'
    QUOTE = 'quote'
    UNORDERED_LIST = 'unordered list'
    ORDERED_LIST = 'ordered list'


def block_to_block_type(markdown_block):
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
    blocks = markdown.split("\n\n")
    filtered_blocks = []
    for block in blocks:
        if block == "":
            continue
        block = block.strip()
        filtered_blocks.append(block)
    return filtered_blocks















