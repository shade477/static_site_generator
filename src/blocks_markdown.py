def markdown_to_blocks(text):
    """
    Takes input a string document and returns blocks
    @params
    - text: str -> String document to be split into blocks

    @return
    - List[str]
    """

    blocks = text.split('\n\n')
    res = []
    for block in blocks:
        if not block:
            continue
        block = block.strip()
        block = block.lstrip('\n')
        res.append(block)
    
    return res
