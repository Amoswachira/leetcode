class MyStack:

    def __init__(self):
        self.queue = deque()
        

    def push(self, x: int):
        self.queue.append(x)
        for _ in range(len(self.queue) - 1):
            self.queue.append(self.queue.popleft())
        

    def pop(self):
        return self.queue.popleft()
        

    def top(self):
        return self.queue[0]

    def empty(self):
        return not len(self.queue)
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()