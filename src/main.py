from textnode import TextNode, TextType
import os
import shutil
from copystatic import copy_files_recursive
from generate_content import generate_page_recursive

dir_path_static = "./static"
dir_path_public = "./public"
dir_path_content = "./content"
template_path = "./template.html"

def main():
    print("Deleting public directory...")
    if os.path.exists(dir_path_public):
        shutil.rmtree(dir_path_public)

    print("Copying static files to public directory...")
    copy_files_recursive(dir_path_static, dir_path_public)

    print("Generating page...")
    generate_page_recursive(
        os.path.join(dir_path_content),
        template_path,
        os.path.join(dir_path_public),
    )

if __name__ == "__main__":
    main()
