class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError("to_html not impletemented yet")
    
    def props_to_html(self):
        if self.props is None:
            return ""
        return_string = ""
        for key in self.props:
            return_string += f" {key}='{self.props[key]}'"
        return return_string
    
    def __repr__(self):
        return(f"HTMLNode(tag: {self.tag}, value: {self.value}, children: {self.children}, props: {self.props})")

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value is None:
            raise ValueError("all leafs must have a value")
        if self.tag is None:
            return self.value
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
    
    def __repr__(self):
        return f"LeafNode(tag: {self.tag}, value: {self.value}, props: {self.props})"
    
class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag is None:
            raise ValueError("tags are required for ParentNode")
        if self.children is None:
            raise ValueError("children are required for ParentNode")
        html = f"<{self.tag}>"

        for child in self.children:
            html += child.to_html()
        
        html += f"</{self.tag}>"
        return html


    def __repr__(self):
        return f"ParentNode(tag: {self.tag}, children: {self.children}, props: {self.props})"
        