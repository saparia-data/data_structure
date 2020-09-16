'''
The task is to design and implement methods of an LRU cache. The class has two methods get() and set() which are defined as follows.
get(x)   : Returns the value of the key x if the key exists in the cache otherwise returns -1.
set(x,y) : inserts the value if the key x is not already present. 
If the cache reaches its capacity it should invalidate the least recently used item before inserting the new item.
In the constructor of the class the size of the cache should be intitialized.

Input:
The first line of input contain an integer T denoting the number of test cases. Then T test case follow. Each test case contains 3 lines. 
The first line of input contains an integer N denoting the capacity of the cache 
and then in the next line is an integer Q denoting the number of queries Then Q queries follow. A Query can be of two types
1. SET x y : sets the value of the key x with value y
2. GET x : gets the key of x if present else returns -1.

Output:
For each test case, in a new line, output will be space separated values of the query.

Your Task:
This is a function problem. You only need to complete the provided functions get() and set(). 

Expected Time Complexity: O(1) for both get() and set().
Expected Auxiliary Space: O(1) for both get() and set(). (though, you may use extra space for cache storage and implementation purposes).

Constraints:
1 <= T <= 100
1 <= N <= 1000
1 <= Q <= 100000
1 <= x, y <= 1000

Example:
Input:
2
2
2
SET 1 2 GET 1
2
7
SET 1 2 SET 2 3 SET 1 5 SET 4 5 SET 6 7 GET 4 GET 1
Output:
2
5 -1

Explanation: 
Test Case 1: Cache Size = 2
SET 1 2 GET 1
SET 1 2 : 1 -> 2
GET 1 : Print the value corresponding to Key 1, ie 2.
Test Case 2: Cache Size = 2
SET 1 2 SET 2 3 SET 1 5 SET 4 5 SET 6 7 GET 4 GET 1
SET 1 2 : 1 -> 2
SET 2 3 : 1 -> 2, 2 -> 3 (the most recently used one is kept at the rightmost position) 
SET 1 5 : 2 -> 3, 1 -> 5
SET 4 5 : 1 -> 5, 4 -> 5 (Cache size is 2, hence we delete the least recently used key-value pair)
SET 6 7 : 4 -> 5, 6 -> 7 
GET 4 : Prints 5
GET 1 : No key-value pair having key = 1. Hence prints -1. 


hint:

The key to solve this problem is using a double linked list which enables us to quickly move nodes.
The LRU cache is a hash map of keys and double linked nodes. The hash map makes the time of get() to be O(1). 
The list of double linked nodes make the nodes adding/removal operations O(1).

https://www.geeksforgeeks.org/design-a-data-structure-for-lru-cache/

'''
class Node:
    def __init__(self,key,value):
        self.key=key
        self.value=value
        self.next=self.pre=None
        
class LRUCache:
    hsmap=dict()
    capacity=count=0
    head=tail=None
    
    def __init__(self,cap):
        self.hsmap=dict()
        self.capacity=cap
        self.head=Node(0,0)
        self.tail=Node(0,0)
        
        self.head.next=self.tail
        self.head.pre=None
        self.tail.next=None
        self.tail.pre=self.head
        count=0
        
    def addToHead(self,node):
        node.next=self.head.next
        node.next.pre=node
        node.pre=self.head
        self.head.next=node
        
    def deleteNode(self,node):
        node.pre.next=node.next
        node.next.pre=node.pre
        
    def get(self,key):
        
        if key in self.hsmap:
            
            node=self.hsmap[key]
            result=node.value
            self.deleteNode(node)
            self.addToHead(node)
            return result
            
        else:
            return -1
        
    def set(self,key,value):
        
        if key in self.hsmap:
            
            node=self.hsmap[key]
            node.value=value
            self.deleteNode(node)
            self.addToHead(node)
        else:
            node=Node(key,value)
            self.hsmap[key]=node
            
            if self.count<self.capacity:
                self.count+=1
                self.addToHead(node)
            else:
                self.hsmap.pop(self.tail.pre.key)
                self.deleteNode(self.tail.pre)
                self.addToHead(node)
                
                
#using orderedDict
import collections

class LRUCacheUsingOrderedDict:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = collections.OrderedDict()

    def get(self, key):
        try:
            value = self.cache.pop(key)
            self.cache[key] = value
            return value
        except KeyError:
            return -1

    def set(self, key, value):
        try:
            self.cache.pop(key)
        except KeyError:
            if len(self.cache) >= self.capacity:
                self.cache.popitem(last=False)
        self.cache[key] = value


