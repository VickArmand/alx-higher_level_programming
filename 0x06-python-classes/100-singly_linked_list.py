#!/usr/bin/python3
"""
created by Vickarmand
class Node
"""


class Node:

    """ Node that defines a node of a singly linked list """
    def __init__(self, data, next_node=None):
        self.__data = data
        self.__next_node = next_node

    @property
    def data(self):
        """getter to return __data"""
        return self.__data

    @data.setter
    def data(self, value):
        """setter to add a new value"""
        if isinstance(value, int):
            self.__data = value
        else:
            raise TypeError("data must be an integer")

    @property
    def next_node(self):
        """getter to retrieve next node"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """setter to add a next node"""
        if not isinstance(value, Node) and not isinstance(value, None):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


"""
class SinglyLinkedList
"""


class SinglyLinkedList(Node):

    """ SinglyLinkedList that defines a singly linked list """
    def __init__(self, head=None):
        self.__head = head

    def sorted_insert(self, value):
        """
        inserts a new Node into the correct sorted position in the list
        (increasing order)
        """
        new_node = Node(value)
        if self.__head is None:
            self.__head = new_node
        else:
            current = self.__head
            while (current):
                if value > current.data and current.next_node is None:
                    current.next_node = new_node
                elif value < current.data and current == self.__head:
                    new_node.next_node = current
                    self.__head = new_node
                elif value > current.data and value <= current.next_node.data:
                    previous_next = current.next_node
                    current.next_node = new_node
                    new_node.next_node = previous_next
                current = current.next_node

    def __str__(self):
        """print the entire list"""
        current = self.__head
        res = []
        while (current is not None):
            res.append(str(current.data))
            current = current.next_node
        return "\n".join(res)
