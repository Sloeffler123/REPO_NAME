from textnode import TextNode, TextType
from extract_images import extract_markdown_images, extract_markdown_links
import re
def split_nodes_delimiter(old_nodes, delimiter, text_type):
    
    
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        split_nodes = []
        sections = old_node.text.split(delimiter)
        if len(sections) % 2 == 0:
            raise ValueError("invalid markdown, formatted section not closed")
        for i in range(len(sections)):
            if sections[i] == "":
                continue
            if i % 2 == 0:
    
                split_nodes.append(TextNode(sections[i], TextType.TEXT))
            else:
               split_nodes.append(TextNode(sections[i], text_type))
        new_nodes.extend(split_nodes)
    return new_nodes


def split_nodes_image(old_nodes):
    new_nodes = []
    
    for old_node in old_nodes:
        # Skip non-text nodes
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        
        text = old_node.text
        image_data = extract_markdown_images(text)
        
        # If no images, keep the node as is
        if not image_data:
            new_nodes.append(old_node)
            continue
        
        # Keep track of where we are in the original text
        remaining_text = text
        
        # For each image we found
        for alt_text, img_url in image_data:
            # The full image markdown
            image_markdown = f"![{alt_text}]({img_url})"
            
            # Split the text at the image markdown (just once)
            parts = remaining_text.split(image_markdown, 1)
            
            # The text before the image
            before_text = parts[0]
            if before_text:
                new_nodes.append(TextNode(before_text, TextType.TEXT))
            
            # The image itself
            new_nodes.append(TextNode(alt_text, TextType.IMAGE, img_url))
            
            # The remaining text becomes what was after this image
            if len(parts) > 1:
                remaining_text = parts[1]
            else:
                remaining_text = ""
        
        # Add any remaining text after the last image
        if remaining_text:
            new_nodes.append(TextNode(remaining_text, TextType.TEXT)) 

    return new_nodes

def split_nodes_link(old_nodes):
    new_nodes = []
    
    for old_node in old_nodes:
        # Skip non-text nodes
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        
        text = old_node.text
        image_data = extract_markdown_links(text)
        
        # If no images, keep the node as is
        if not image_data:
            new_nodes.append(old_node)
            continue
        
        # Keep track of where we are in the original text
        remaining_text = text
        
        # For each image we found
        for alt_text, img_url in image_data:
            # The full image markdown
            image_markdown = f"[{alt_text}]({img_url})"
            
            # Split the text at the image markdown (just once)
            parts = remaining_text.split(image_markdown, 1)
            
            # The text before the image
            before_text = parts[0]
            if before_text:
                new_nodes.append(TextNode(before_text, TextType.TEXT))
            
            # The image itself
            new_nodes.append(TextNode(alt_text, TextType.LINK, img_url))
            
            # The remaining text becomes what was after this image
            if len(parts) > 1:
                remaining_text = parts[1]
            else:
                remaining_text = ""
        
        # Add any remaining text after the last image
        if remaining_text:
            new_nodes.append(TextNode(remaining_text, TextType.TEXT)) 

    return new_nodes











