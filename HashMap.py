from LinkedList import Node, LinkedList
from random import randint

class HashMap:

    def __init__(self, array_size):
        self.array_size = array_size
        self.array = [LinkedList() for item in range(array_size)]

    def hash(self, key):
        hash_code = int(key) #user will enter appropriate int for movie genre
        return hash_code
    
    def assign(self, key, value):
        index = self.hash(key) #int of user input
        payload = Node([key, value]) #Node of list with genre number at key, and movie title at value
        list_at_array = self.array[index]
        list_at_array.insert(payload)
        return

    def retrieve(self, key):
        index = self.hash(key)
        list_at_index = self.array[index]

        if list_at_index.get_size() == 0:
            return None

        random_index = randint(0, list_at_index.get_size() - 1)
        print(random_index)
        iterator = 0
        current_node = list_at_index.get_head()
        while iterator <= random_index:
            iterator += 1
            current_node = current_node.get_next_node()

        return current_node.get_value()[1]
    
