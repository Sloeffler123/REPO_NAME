
class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        if self.props == None:
            return ''
        return ' '.join(f"{k}='{v}'" for k,v in self.props.items())
            
    def __repr__(self):
        
        return f'HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})'
    
class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        
        super().__init__(tag, value, None, props)
        

    def to_html(self):
        if self.value == None:
            raise ValueError
        if self.tag == None:
            return self.value
        props_html = self.props_to_html()
        if props_html:
            return f'<{self.tag} {props_html}>{self.value}</{self.tag}>'
        else:
            return f'<{self.tag}>{self.value}</{self.tag}>'

    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)
        
    def to_html(self):
        if self.tag is None:
            raise ValueError('Tag needs a value')
        if self.children is None:
            raise ValueError('Childeren needs a value')
        result = ''
        for i in self.children:
            result += i.to_html()
        return f'<{self.tag}>{result}</{self.tag}>'
        

        

