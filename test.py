import Queue
q1=Queue.Queue()
q2=Queue.Queue()
q1.enqueue(1)
q1.enqueue(2)
q1.enqueue(3)
q1.enqueue(4)
q1.enqueue(5)
q1.enqueue(6)
print(q1.__repr__())
print(q2.__repr__())
for i in range(q1.size()):
    current=q1.peek()
    # if(current==3):
    #     q1.dequeue()
    q2.enqueue(q1.dequeue())
print(q1.__repr__)
print(q2.__repr__)