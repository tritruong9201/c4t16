class Node:
    def __init__(content,next_node):
        self.content = content
        self.next_node = next_node

class LinkedList:
    def __init__(self,head):
        self.head = None

    def __str__(self):
        if self.head == None:
            return "<<E>>"
        else:
            res = ""
            current = self.head
            while current != None:
                res += str(current.content) + "->"
                current = current.next
        return res[:-2]

    def add_first(self,added_first_item):
        node = Node(added_first_item,None)
        node.next = self.head
        self.head = node

    def add_last(self,added_last_item):
        node = Node(added_last_item,None)
        current = self.head
        if current == None:
            self.head = Node
        while current.next != None:
            current = current.next
        current.next = node

    def remove_first(self):
        current = self.head.next
        result_content = current.content
        result_next = current.next
        node = Node(current.content,current.next)
        node.next = current.next
        self.head = node
        return Node(result_content,result_next)

    def remove_last(self):
        current = self.head
        if current == None:
            self.head = Node
        while current != None:
            current = current.next
        result_content = current.content
        current.content = None
        return Node(result_content,None)