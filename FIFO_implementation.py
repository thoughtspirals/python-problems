class Queue:
    def __init__(self):
        self.queue = []
        
    def Enqueue(self, item):
            self.queue.append(item)
            
    def Dequeue(self):
                if len(self.queue)<1:
                    return None
                return self.queue.pop(0)
            
    def Display(self):
                print(self.queue)
                
q = Queue()
q.Enqueue(1)
q.Enqueue(2)
q.Enqueue(3)
q.Enqueue(4)
q.Display()
q.Dequeue()
q.Display()
