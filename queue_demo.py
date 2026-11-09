class Queue:
    """Circular queue using a fixed-size array (FIFO)."""

    def __init__(self, capacity=5):
        self.capacity = capacity
        self.arr = [None] * capacity
        self.front = 0      # index of the first element
        self.count = 0      # number of elements stored

    def is_empty(self):
        return self.count == 0

    def is_full(self):
        return self.count == self.capacity

    def size(self):
        return self.count

    def enqueue(self, x):
        """Add x at the rear."""
        if self.is_full():
            print(f"enqueue({x}) -> Overflow, queue is full")
            return
        rear = (self.front + self.count) % self.capacity
        self.arr[rear] = x
        self.count += 1
        print(f"enqueue({x}) -> ok")

    def dequeue(self):
        """Remove and return the front element."""
        if self.is_empty():
            print("dequeue() -> Underflow, queue is empty")
            return None
        x = self.arr[self.front]
        self.arr[self.front] = None
        self.front = (self.front + 1) % self.capacity
        self.count -= 1
        print(f"dequeue() -> {x}")
        return x

    def peek_front(self):
        if self.is_empty():
            print("front() -> queue is empty")
            return None
        print(f"front() -> {self.arr[self.front]}")
        return self.arr[self.front]

    def peek_rear(self):
        if self.is_empty():
            print("rear() -> queue is empty")
            return None
        rear = (self.front + self.count - 1) % self.capacity
        print(f"rear() -> {self.arr[rear]}")
        return self.arr[rear]

    def search(self, x):
        """Return position from the front (0 = front), or -1."""
        for i in range(self.count):
            if self.arr[(self.front + i) % self.capacity] == x:
                print(f"search({x}) -> found, {i} place(s) from front")
                return i
        print(f"search({x}) -> not found")
        return -1

    def display(self):
        items = [self.arr[(self.front + i) % self.capacity]
                 for i in range(self.count)]
        print("display() -> front [", ", ".join(map(str, items)), "] rear")

    def clear(self):
        self.arr = [None] * self.capacity
        self.front = 0
        self.count = 0
        print("clear() -> queue emptied")


if __name__ == "__main__":
    q = Queue(5)
    print("isEmpty() ->", q.is_empty())
    for v in (10, 20, 30, 40, 50):
        q.enqueue(v)
    print("isFull() ->", q.is_full())
    q.enqueue(60)                 # Overflow
    q.peek_front()
    q.peek_rear()
    print("size() ->", q.size())
    q.dequeue()                   # 10
    q.dequeue()                   # 20
    q.enqueue(60)                 # wraps around the array
    q.enqueue(70)
    q.display()
    q.search(40)
    q.search(99)
    q.clear()
    q.display()
    q.dequeue()                   # Underflow
