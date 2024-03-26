import os
from block_markdown import markdown_to_html_node


def generate_page_recursive(dir_path_content, template_path, dest_dir_path):
    content = os.listdir(dir_path_content)
    for i in content:
        content_path = os.path.join(dir_path_content, i)
        if os.path.isfile(content_path):
            dest_path = os.path.join(dest_dir_path, "index.html")
            generate_page(content_path, template_path, dest_path)
        else:
            dest_dir_path = os.path.join(dest_dir_path, i)
            generate_page_recursive(content_path, template_path, dest_dir_path)


def generate_page(from_path, template_path, dest_path):
    print(f" * {from_path} {template_path} -> {dest_path}")
    from_file = open(from_path, "r")
    markdown_content = from_file.read()
    from_file.close()

    template_file = open(template_path, "r")
    template = template_file.read()
    template_file.close()

    node = markdown_to_html_node(markdown_content)
    html = node.to_html()

    title = extract_title(markdown_content)
    template = template.replace("{{ Title }}", title)
    template = template.replace("{{ Content }}", html)

    dest_dir_path = os.path.dirname(dest_path)
    if dest_dir_path != "":
        os.makedirs(dest_dir_path, exist_ok=True)
    to_file = open(dest_path, "w")
    to_file.write(template)


def extract_title(md):
    lines = md.split("\n")
    for line in lines:
        if line.startswith("# "):
            return line[2:]
    raise ValueError("No title found")
