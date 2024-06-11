import os

current_path = os.getcwd()


def import_md_file(file_path):
    ab_file_path = os.path.join(current_path, "markdown", file_path)
    with open(ab_file_path, 'r', encoding='utf-8') as file:
        md_text = file.read()
        return md_text
