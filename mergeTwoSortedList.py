# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

def mergeTwoLists(list1: [ListNode], list2: [ListNode]):
    def llToList(list):
        l = []
        if list == None:
            l = []
        else:
            while list != None:
                l.append(list.val)
                list = list.next
        return l
    
    def listToLL(l):
        root = None     
        for item in l:
            temp = ListNode(item)
            if root == None:
                root = temp
                head = root
            else:
                root.next = ListNode(item)
                root = root.next
        return head
    
    l1 = llToList(list1)
    l2 = llToList(list2)

    l = l1 + l2
    l.sort()
    return listToLL(l)

if __name__ == '__main__':
    l1 = ListNode(1, ListNode(2, ListNode(4)))
    l2 = ListNode(1, ListNode(3, ListNode(4)))
    
    o = (mergeTwoLists(l1, l2))
    
    while o is not None:
        print(o.val, end =" ")
        o = o.next
    
    
    
    
    
    


    

        




        
        