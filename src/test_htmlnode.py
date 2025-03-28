import unittest

from htmlnode import HTMLNode


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


if __name__ == '__main__':
    unittest.main()







