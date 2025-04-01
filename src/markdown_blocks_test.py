import unittest
from markdown_blocks import markdown_to_blocks, block_to_block_type, BlockType


class TestMarkdownToHTML(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_markdown_to_blocks_newlines(self):
        md = """
This is **bolded** paragraph




This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    # def test_markdown_block_type_heading(self):
    #     text = '### This is a level 3 heading'
    #     block = block_to_block_type(text)
    #     self.assertEqual(block, BlockType.HEADING)
        
    # def test_markdown_block_type_code(self):
    #     text = '``` This is a code text. ```'
    #     block = block_to_block_type(text)
    #     self.assertEqual(block, BlockType.CODE)
    
    # def test_markdown_block_type_ordered_list(self):
    #     text = '1. This is a 1.\n2. this is a 2.\n3. this is a 3.'
    #     block = block_to_block_type(text)
    #     self.assertEqual(block, BlockType.ORDERED_LIST)
    
    # def test_markdown_block_type_paragraph(self):
    #     text = 'This is a para.'
    #     block = block_to_block_type(text)
    #     self.assertEqual(block, BlockType.PARAGRAPH)

    # def test_markdown_block_type_unordered_list(self):
    #     text = 'This is a para.'
    #     block = block_to_block_type(text)
    #     self.assertEqual(block, BlockType.PARAGRAPH) 
    def test_block_to_block_types(self):
        block = "# heading"
        self.assertEqual(block_to_block_type(block), BlockType.HEADING)
        block = "```\ncode\n```"
        self.assertEqual(block_to_block_type(block), BlockType.CODE)
        block = "> quote\n> more quote"
        self.assertEqual(block_to_block_type(block), BlockType.QUOTE)
        block = "- list\n- items"
        self.assertEqual(block_to_block_type(block), BlockType.UNORDERED_LIST)
        block = "1. list\n2. items"
        self.assertEqual(block_to_block_type(block), BlockType.ORDERED_LIST)
        block = "paragraph"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)
if __name__ == "__main__":
    unittest.main()