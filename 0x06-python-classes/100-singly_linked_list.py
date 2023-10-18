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
        return self.__data
    @data.setter
    def data(self, value):
        if isinstance(value, int):
            self.__data = value
        else:
            raise TypeError("data must be an integer")
    @property
    def next_node(self):
        return self.__next_node
    @next_node.setter
    def next_node(self, value):
        if not isinstance(value, Node) and not isinstance(value, None):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value

"""

class SinglyLinkedList
"""


class SinglyLinkedList(Node):

    """ SinglyLinkedList that defines a singly linked list """
    def __init__(self, head):
        self.__head = head

    def sorted_insert(self, value):
        Node.data(value)
        if value < Node.next_node().data():
            self.__head = Node
        else:
            self.__head = Node.next_node()
