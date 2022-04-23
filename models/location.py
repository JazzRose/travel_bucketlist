class Location:
    def __init__(self, name, type, info, visited = False, id = None):
        self.name = name
        self.type = type
        self.info = info
        self.visited = visited
        self.id = id