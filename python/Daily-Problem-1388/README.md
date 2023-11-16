# Question 1388

Good morning! Here's your coding interview problem for today.

This problem was asked by Apple.

Implement a queue using two stacks. Recall that a queue is a FIFO (first-in, first-out) data structure with the following methods: enqueue, which inserts an element into the queue, and dequeue, which removes it.

## Implementation

```
Command: Push(1,2,3)

LHS | 3 2 1
RHS | 

Command: Pop() -> Expect val of 1

if RHS is not empty
  return RHS.pop()

while LHS is not empty:
  RHS.push(LHS.pop())

LHS | 
RHS | 1 2 3

return RHS.pop()

RHS | 2 3






```
