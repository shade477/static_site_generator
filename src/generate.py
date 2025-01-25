import re
import os
import logging

from src.converter import markdown_to_html_node

logging.basicConfig(level=logging.INFO)

def extract_title(markdown):
    pattern = r'^#\s*(.+)'
    match = re.match(pattern, markdown)
    if match:
        title = match.group(1).strip()
        return title
    else:
        raise Exception("No valid title found")
        
def generate_page(from_path, template_path, dest_path):
    print(f'Generating page from {from_path} to {dest_path} using {template_path}')

    logging.info(f"Reading file: {from_path}")
    with open(from_path, 'r') as file:
        markdown = file.read()

    logging.info(f'Reading file: {template_path}') 
    with open(template_path, 'r') as file:
        template = file.read()

    parsed_html = markdown_to_html_node(markdown).to_html()
    title = extract_title(markdown)
    result = template.replace('{{ Title }}', title).replace('{{ Content }}', parsed_html)

    with open(dest_path, 'w') as file:
        file.write(result)

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    files = os.listdir(dir_path_content)
    for file in files:
        path = os.path.join(dir_path_content, file)
        if os.path.isfile(path) and re.search(r'\.md$', file):
            generate_page(path, template_path, os.path.join(dest_dir_path, file))
        
        else:
            dst_path = os.path.join(dest_dir_path, file)
            os.mkdir(dst_path)
            generate_pages_recursive(path, template_path, dst_path)
