from src.ParentNode import ParentNode
from src.LeafNode import LeafNode
from BlockType import BlockType
import blocks_markdown as bm

def markdown_to_html_node(markdown):
    blocks = bm.markdown_to_blocks(markdown)
    res = []
    for block in blocks:
        type = bm.block_to_block_type(block)
        match(type):
            case BlockType.PARAGRAPH:
                child = LeafNode(BlockType.PARAGRAPH.value , block)

            case BlockType.HEADING1:
                child = LeafNode(BlockType.HEADING1.value, block[2:])

            case BlockType.HEADING2:
                child = LeafNode(BlockType.HEADING2.value, block[3:])

            case BlockType.HEADING3:
                child = LeafNode(BlockType.HEADING3.value, block[4:])

            case BlockType.HEADING4:
                child = LeafNode(BlockType.HEADING4.value, block[5:])
                
            case BlockType.HEADING5:
                child = LeafNode(BlockType.HEADING5.value, block[6:])

            case BlockType.HEADING6:
                child = LeafNode(BlockType.HEADING6.value, block[7:])

            case BlockType.CODE:
                child = LeafNode(BlockType.CODE.value, block[3:])

            case BlockType.QUOTE:
                child = LeafNode(BlockType.QUOTE.value, block[2:])

            case BlockType.UNORDERED:
                lines = block.split('\n')
                list = []
                for line in lines:
                    node = LeafNode('li', line[2:])
                    list.append(node)
                child = ParentNode('ul', list)

            case BlockType.ORDERED:
                lines = block.split('\n')
                list = []
                for line in lines:
                    node = LeafNode('li', line[3:])
                    list.append(node)
                child = ParentNode('ol', list)

        res.append(child)
    
    return ParentNode('div', res)