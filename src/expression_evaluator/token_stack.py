class TokenStack:
    def __init__(self):
        self.stack = {}
        self.index = 0
        self.priority_index = 0

    def __len__(self):
        length = 0
        for key in self.stack:
            length += len(self.stack[key])
        return length

    def __iter__(self):
        self.index = 0
        self.priority_index = 0
        return self
        
    def __next__(self):
        current_priority = self.current_priority()
        if current_priority is None:
            raise StopIteration
        elif (self.index >= len(current_priority)) and (self.priority_index >= len(self.priority_order())):
            raise StopIteration

        elif self.index >= len(current_priority):
            self.index = 0
            self.priority_index += 1
            current_priority = self.current_priority()
            if current_priority is None:
                raise StopIteration
        
        if self.index < len(current_priority):
            token = current_priority[self.index]
            self.index += 1
            return token

    def priority_order(self):
        return sorted(self.stack.keys(), reverse=True)

    def current_priority(self):
        if self.priority_index >= len(self.priority_order()):
            return None
        priority_level = self.priority_order()[self.priority_index]
        return self.stack[priority_level]

    def add(self, token):
        if token.priority_level not in self.stack.keys():
            self.stack[token.priority_level] = []
        self.stack[token.priority_level].append(token)