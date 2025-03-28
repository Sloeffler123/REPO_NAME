import unittest

from htmlnode import HTMLNode, LeafNode


class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        props = {'href': 'https://www.google.com', 'target': '_blank'}
        node = HTMLNode(props=props)
        expected = "href='https://www.google.com' target='_blank'"
        self.assertEqual(node.props_to_html(), expected)

    def test_empty_props(self):
        node = HTMLNode()
        self.assertEqual(node.props_to_html(), '')

    def test_repr(self):
        node = HTMLNode('p', 'Hello, world!', None, {'class': 'text'})
        # Check that repr contains all the relevant information
        repr_str = repr(node)
        self.assertIn('p', repr_str)
        self.assertIn('Hello, world!', repr_str)
        self.assertIn('class', repr_str)
    
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_a(self):
        node = LeafNode(tag='a', value='Click me!', props={'href': 'https://www.google.com'})
        self.assertEqual(node.to_html(), "<a href='https://www.google.com'>Click me!</a>")

    def test_leaf_to_html_no_tag(self):
        node = LeafNode(None, "Hello, world!")
        self.assertEqual(node.to_html(), "Hello, world!")

if __name__ == '__main__':
    unittest.main()







