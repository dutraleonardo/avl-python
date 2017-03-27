#!/usr/bin/env python2
# -*- coding: utf-8 -*-
########################
##   Python AVL Tree  ##
##   Leonardo Dutra   ##
########################

class Node:
    def __init__(self, data):
        self.data = data
        self.setChilds(None, None)

    def setChilds(self, left, right):
        self.left = left
        self.right = right

    def balance(self):
        depth_left = 0
        if self.left:
            depth_left = self.left.depth()
        depth_right = 0
        if self.right:
            depth_right = self.right.depth()
        return depth_left - depth_right

    def depth(self):
        depth_left = 0
        if self.left:
            depth_left = self.left.depth()
        depth_right = 0
        if self.right:
            depth_right = self.right.depth()
        return 1 + max(depth_left, depth_right)

    def rotationLeft(self):
        self.data, self.right.data = self.right.data, self.data
        old_left = self.left
        self.setChilds(self.right, self.right.right)
        self.left.setChilds(old_left, self.left.left)

    def rotationRight(self):
        self.data, self.left.data = self.left.data, self.data
        old_right = self.right
        self.setChilds(self.left.left, self.left)
        self.right.setChilds(self.right.right, old_right)

    def rotationLeftRight(self):
        self.left.rotationLeft()
        self.rotationRight()

    def rotationRightLeft(self):
        self.right.rotationRight()
        self.rotationLeft()

    def executeBalance(self):
        bal = self.balance()
        if bal > 1:
            if self.left.balance() > 0:
                self.rotationRight()
            else:
                self.rotationLeftRight()
        elif bal < -1:
            if self.right.balance() < 0:
                self.rotationLeft()
            else:
                self.rotationRightLeft()

    def insert(self, data):
        if data <= self.data:
            if not self.left:
                self.left = Node(data)
            else:
                self.left.insert(data)
        else:
            if not self.right:
                self.right = Node(data)
            else:
                self.right.insert(data)
        self.executeBalance()

    def printTree(self, indent = 0):
        print " " * indent + str(self.data)
        if self.left:
            self.left.printTree(indent + 2)
        if self.right:
            self.right.printTree(indent + 2)