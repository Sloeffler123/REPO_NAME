import re


def extract_markdown_images(text):
    
    alt_text = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)


    return alt_text

def extract_markdown_links(text):
    alt_text = re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    

    return alt_text




