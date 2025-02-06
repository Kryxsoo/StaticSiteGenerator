class HTMLNode:
  def __init__(self, tag=None, value=None, children=None, props=None):
    self.tag = tag
    self.value = value
    self.children = children
    self.props = props
  
  def to_html(self):
    raise NotImplementedError
  
  def props_to_html(self):
      if not self.props:
        return ""
      attributes = []
      for key, value in self.props.items():
        attributes.append(f'{key}="{value}"')
      return " " + " ".join(attributes)
  
  def __repr__(self):
    return f'HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})'
  
class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
      super().__init__(tag, value, [], props)
    
    def to_html(self):
        if self.value is None:
            raise ValueError("Value cannot be none")       
        if self.tag is None:
            return self.value
      
        return f'<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>'
    

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)
        if tag is None:
            raise ValueError("Tag cannot be none")
        if children is None:
            raise ValueError("Children cannot be none")

    def to_html(self):
        children_html = "".join(child.to_html() for child in self.children)
        return f'<{self.tag}{self.props_to_html()}>{children_html}</{self.tag}>'

  
