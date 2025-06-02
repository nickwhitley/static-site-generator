from textnode import TextNode, TextType
import os
import shutil


def move_static_content_to_public():
    public_path = 'public/'
    static_path = 'static/'
    try:
        shutil.rmtree(public_path)
    except Exception as e:
        print(f"An error occured: {e}")
        return

    shutil.copytree(static_path, public_path)



def main():
    move_static_content_to_public()

if __name__ == "__main__":
    main()
