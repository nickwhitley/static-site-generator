import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode


class TestHTMLNode(unittest.TestCase):
    def test_eq_html_node(self):
        node = HTMLNode(tag="p",value="paragraph")
        node2 = HTMLNode(tag="p",value="paragraph")
        self.assertEqual(node.value, node2.value)

    def test_not_eq_text_html_node(self):
        node = HTMLNode(tag="p",value="paragraph does not equal")
        node2 = HTMLNode(tag="p",value="paragraph")
        self.assertNotEqual(node.value, node2.value)

    def test_eq_leaf_node(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

if __name__ == "__main__":
    unittest.main()