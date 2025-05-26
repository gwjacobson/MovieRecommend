class HashMap:

    def __init__(self, array_size):
        self.array_size = array_size
        self.array = [None for item in range(array_size)]

    def hash(self, key):
        hash_code = int(key) #user will enter appropriate int for movie genre
        return hash_code
    
    def assign(self, key, value):
        index = self.hash(key)
        self.array[index] = value

    def retrieve(self, key):
        index = self.hash(key)
        return self.array[index]
    
