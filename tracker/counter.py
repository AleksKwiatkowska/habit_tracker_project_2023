class Counter:
    
    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description
        self.count = 0
    
    def increment(self):
        self.count += 1
        
    def reset(self):
        self.count = 0
        
    def __str__(self):
        return f"{self.name}: {self.count}"
        
# counter = Counter("test name", "test description")
# counter.increment()
# print(counter)