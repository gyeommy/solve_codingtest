from queue import Queue
from typing import Any

class Self_Queue:

    def __init(self, *args:Any):
        self.__items: list[Any] = list(args)
        self.__size: int = len(self.__items)

    def enqueue(self, item:Any):
        self.__items.append(item)
        self.__size += 1


    def dequeue(self):
        if self.empty():
            raise IndexError("dequeue from empty queue")
        item: Any = self.__items.pop(0)
        self.__size -= 1
        return item
    
    def empty(self):
        return not self.__size
    
    def __str__(self):
        return f"{self.__items}"
    
    def __repr__(self):
        return f"{self.__items}"
    
    def __len__(self):
        return self.__size
    
    def __iter__(self):
        if self.empty():
            return None
        for item in self.__items:
            yield item