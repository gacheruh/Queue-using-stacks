class Stack:
    def __init__(self):
        self.stack = []
    
    def is_empty(self):
        return len(self.stack) == 0
    
    def size(self):
        return len(self.stack)
    
    def push(self, num):
        self.stack.append(num)

    def pop(self):
        if self.is_empty():
            print("Stack is empty")
        else:
            return self.stack.pop()


class QueueUsingStacks:
    def __init__(self):
        self.stack_in = Stack()  # First stack for enqueueing
        self.stack_out = Stack()  # Second stack for dequeueing

    def is_empty(self):
        return self.stack_in.is_empty() and self.stack_out.is_empty()
    
    def size(self):
        return self.stack_in.size() + self.stack_out.size()

    def enqueue(self, num):
        self.stack_in.push(num)

    def dequeue(self):
        if self.is_empty():
            return "Queue is empty"
        
        # If stack_out is empty, transfer all elements from stack_in to stack_out
        if self.stack_out.is_empty():
            while not self.stack_in.is_empty():
                self.stack_out.push(self.stack_in.pop())

        return self.stack_out.pop()  # Pop from stack_out


# Testing the QueueUsingStacks class
q = QueueUsingStacks()
print(q.is_empty())  # Should return True
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
print(f'Size of queue is {q.size()}')
print(q.dequeue())  # Should return 1
print(q.dequeue())  # Should return 2
print(q.dequeue())  # Should return 3
print(q.dequeue())  # Should return 4
print(q.dequeue())  # Should indicate that the queue is empty




