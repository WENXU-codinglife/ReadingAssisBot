import os

def generate_directory_structure(path):
    structure = []
    for item in os.listdir(path):
        item_path = os.path.join(path, item)
        if os.path.isdir(item_path):
            nested_structure = generate_directory_structure(item_path)
            structure.append([item, nested_structure])
        else:
            structure.append(item)
    return structure
