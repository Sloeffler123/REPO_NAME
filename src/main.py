from textnode import TextNode
import shutil
import os 
from markdown_blocks import markdown_to_html_node, extract_title
from pathlib import Path
import sys

dir_path_static = "./static"
dir_path_public = "./docs"
dir_path_content = "./content"
template_path = "./template.html"
default_basepath = "/"

def main():
    basepath = default_basepath
    if len(sys.argv) > 1:
        basepath = sys.argv[1]

    copy_static(source=dir_path_static, destination=dir_path_public)
    
    generate_pages_recursive(
        dir_path_content=dir_path_content,         
        template_path=template_path,       
        dest_dir_path=dir_path_public,
        basepath=basepath           
    )
def copy_static(source, destination):
    if source == './static' and os.path.exists('./docs'):
        shutil.rmtree(destination)
        os.mkdir(destination)
    elif not os.path.exists(destination):
        os.mkdir(destination)    
    entries_in_source_directory = os.listdir(source)
    for entry in entries_in_source_directory:
        entries_in_source_directory = os.path.join(source, entry)
        destination_directory = os.path.join(destination, entry)
        print(f"Source: {source}, Destination: {destination}")
        print(f"Working on entry: {entry}")
        if os.path.isfile(entries_in_source_directory):
            shutil.copy(entries_in_source_directory, destination_directory)
        else:
            if not os.path.exists(destination_directory):
                os.mkdir(destination_directory)
            copy_static(entries_in_source_directory, destination_directory)

def generate_page(from_path, template_path, dest_path, basepath):
    print(f'Generating page from {from_path} to {dest_path} using {template_path}')
    with open(from_path, 'r') as file: # markdown file
        content = file.read()
    with open(template_path, 'r') as template_file: # template html file
        template = template_file.read()
    template_text_to_html = markdown_to_html_node(content) # from path file
    html = template_text_to_html.to_html()
    title = extract_title(content)
    template = template.replace("{{ Title }}", title)
    template = template.replace("{{ Content }}", html)
    template = template.replace('href="/', 'href="' + basepath)
    template = template.replace('src="/', 'src="' + basepath)#changing the template html file
    dir_name = os.path.dirname(dest_path)
    if not os.path.exists(dir_name):
        os.makedirs(dir_name)
    with open(dest_path, 'w') as html_file:
        html_file.write(template)

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, basepath):
    for filename in os.listdir(dir_path_content):
        from_path = os.path.join(dir_path_content, filename)
        dest_path = os.path.join(dest_dir_path, filename)
        if os.path.isfile(from_path):
            dest_path = Path(dest_path).with_suffix(".html")
            generate_page(from_path, template_path, dest_path, basepath)
        else:
            generate_pages_recursive(from_path, template_path, dest_path, basepath)
main()