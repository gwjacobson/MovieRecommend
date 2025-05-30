class Node:
    def __init__(self, value):
        self.value = value
        self.next_node = None
    
    def get_value(self):
        return self.value
  
    def get_next_node(self):
        return self.next_node
  
    def set_next_node(self, next_node):
        self.next_node = next_node

class LinkedList:
    def __init__(self):
        self.head_node = Node(None)
        self.size = 0

    def get_size(self):
        return self.size
    
    def get_head(self):
        return self.head_node
  
    def insert(self, new_node):
        current_node = self.head_node

        if not current_node:
            self.head_node = new_node
            self.size += 1

        while(current_node):
            next_node = current_node.get_next_node()
            if not next_node:
                current_node.set_next_node(new_node)
                self.size += 1
            current_node = next_node