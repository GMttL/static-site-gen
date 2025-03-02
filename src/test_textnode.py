import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
    
    def test_repr(self):
        node = TextNode("Test node", TextType.ITALIC)
        self.assertEqual(repr(node), "TextNode(Test node, italic, None)")

    def test_repr2(self):
        node = TextNode("Test node", TextType.ITALIC)
        self.assertNotEqual(repr(node), "TextNode(Test node, italic)")


if __name__ == "__main__":
    unittest.main()