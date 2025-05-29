class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.prop = props

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        result_string = ''
        for key, value in props.items():
            result_string += f'{key}="{value}" '
        return result_string.rstrip()

    def __repr__(self):
        f"HTMLNode(\ntag={self.tag}\nvalue={self.value}\nchildren={self.children}\nprops={self.props})"


class LeafNode(HTMLNode):
    def __init__(self, tag=None, value=None):
       super().__init__(tag=tag, value=value, children=None, props=None)
       self.tag = tag
       self.value = value

    def __init_subclass__(cls, *args, **kwargs):
        raise TypeError(f"Class '{cls.__name__}' can't be subclassed")

    def to_html(self):
        if self.value is None:
            raise ValueError
        if self.tag is None:
            return self.value
        return f"<{self.tag}>{self.value}</{self.tag}>"

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag=tag, value=None, children=children, props=props)
        self.tag = tag
        self.children = children
        self.props = props

    def to_html(self):
        if self.tag is None:
            raise ValueError("ParentNode is missing tag property")
        if self.children is None:
            raise ValueError("ParentNode is missing children property")
        result = f"<{self.tag}>"
        for child in self.children:
            result += child.to_html()
        result += f"</{self.tag}>"
        return result
        