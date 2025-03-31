



# def markdown_to_blocks(markdown):
#     blocks = []
#     # Split by double newlines
#     raw_blocks = markdown.split('\n\n')
    
#     for block in raw_blocks:
#         if block.strip():  # Skip empty blocks
#             # Process each line in the block
#             lines = block.strip().split('\n')
#             cleaned_lines = [line.strip() for line in lines]
#             # Rejoin the lines with single newlines
#             cleaned_block = '\n'.join(cleaned_lines)
#             blocks.append(cleaned_block)
    
#     return blocks


def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    filtered_blocks = []
    for block in blocks:
        if block == "":
            continue
        block = block.strip()
        filtered_blocks.append(block)
    return filtered_blocks















