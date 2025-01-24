from src.ParentNode import ParentNode
from src.LeafNode import LeafNode
from src.BlockType import BlockType
import src.blocks_markdown as bm
from src.TextNode import TextNode
from src.TextType import TextType
from src.inline_markdown import text_to_textnodes

def html_image(node) -> LeafNode:
    """
    Takes in a image TextNode and converts it to a LeafNode
    @params:
        - node: TextNode of TextType.IMAGE
    return: LeafNode
    """
    leaf = LeafNode('img', node.text, {'src': node.url})
    return leaf

def html_link(node) -> LeafNode:
    """
    Takes in a Link TextNode and converts it to a LeafNode
    @params:
        - node: TextNode of TextType.LINK
    return: LeafNode
    """
    leaf = LeafNode('a', node.text, {'href': node.url})
    return leaf

def textNode_to_children(nodes: list[TextNode]) -> list[LeafNode]:
    """
    Takes in a list of TextNodes and converts them to LeafNodes
    @params: 
        - nodes -> list[TextNode]
    @return: list[LeafNode]
    """
    conversion = {
        TextType.BOLD: 'b',
        TextType.ITALIC: 'i',
        TextType.CODE: 'code',
        TextType.TEXT: 'p',
        TextType.IMAGE: lambda image: html_image(image),
        TextType.LINK: lambda link: html_link(link)
    }
    res = []
    for node in nodes:
        if node.text_type in [TextType.IMAGE, TextType.LINK]:
            leaf = conversion[node.text_type](node)
        else:
            leaf = LeafNode(conversion[node.text_type], node.text)
        res.append(leaf)
    return res

def process_paragraph(markdown):
    """
    Takes in markdown and converts it to TextNodes and returns HTMLNode
    
    @params:
        - markdown -> str: Normal markdown text

    return: LeafNode or ParentNode
    """
    # Use inline markdown functions to classify inline nodes within the paragraph
    nodes = text_to_textnodes(markdown)
    nodes = textNode_to_children(nodes)
    # if size of nodes is 1 then it cannot be made to ParentNode
    if len(nodes) == 1:
        child = LeafNode('', nodes[0])
    else:
        child = ParentNode('div', nodes)

    return child


def markdown_to_html_node(markdown: str) -> ParentNode:
    """
    Takes input markdown and splits it to HTMLNodes
    @param:
        - markdown -> str
    @return: ParentNode
    """
    blocks = bm.markdown_to_blocks(markdown)
    res = []
    for block in blocks:
        type = bm.block_to_block_type(block)
        match(type):
            case BlockType.PARAGRAPH:
                child = process_paragraph(block).to_html()

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
                child = LeafNode(BlockType.HEADING6.value, block[7:].lstrip('#').lstrip())

            case BlockType.CODE:
                child = LeafNode(BlockType.CODE.value, block[3:-3])

            case BlockType.QUOTE:
                text = '\n'.join(line[2:] for line in block.split('\n'))
                child = LeafNode(BlockType.QUOTE.value, text)

            case BlockType.UNORDERED:
                lines = block.split('\n')
                items = []
                for line in lines:
                    node = LeafNode('li', process_paragraph(line[2:]).to_html())
                    items.append(node)
                child = ParentNode('ul', items)

            case BlockType.ORDERED:
                lines = block.split('\n')
                items = []
                for line in lines:
                    node = LeafNode('li', process_paragraph(line[3:]).to_html())
                    items.append(node)
                child = ParentNode('ol', items)

        res.append(child)
    
    return ParentNode('div', res)