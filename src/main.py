import os
import shutil

from copystatic import copy_files_recursive
from generate_content import generate_page


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

    print("Generating pages...")
    for root, dirs, files in os.walk(dir_path_content):
        for file in files:
            if file.endswith(".md"):
                # Full path to the source markdown file
                from_path = os.path.join(root, file)

                # Transform the path to determine where the generated file should go
                relative_path = os.path.relpath(from_path, dir_path_content)
                dest_path = os.path.join(
                    dir_path_public, os.path.splitext(relative_path)[0] + ".html"
                )

                # Call the generate_page function for each markdown file
                generate_page(from_path, template_path, dest_path)
    
main()
