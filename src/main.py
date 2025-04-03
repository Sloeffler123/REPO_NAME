from textnode import TextNode
import shutil
import os 

def main():
    
    copy_static(source='static', destination='public')

def copy_static(source, destination):
    if source == 'static' and os.path.exists('public'):
        shutil.rmtree(destination)
        os.mkdir(destination)
    elif not os.path.exists(destination):
        os.mkdir(destination)    
    entries_in_source_directory = os.listdir(source)
    
    print(entries_in_source_directory)
    
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
    
main()