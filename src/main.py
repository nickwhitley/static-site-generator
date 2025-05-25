from textnode import TextNode, TextType

def main():
    node = TextNode("This is some anchor text", TextType.LINK_TEXT, "https://wwww.bootdev.com")
    print(node)

if __name__ == "__main__":
    main()
