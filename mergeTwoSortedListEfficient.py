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
        temp = ListNode()
        current = temp
        
        #nice way to iterate over two lists together until either of them reached end
        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next
        
        #current now points to the last node of list after merging nodes of both list.
        # to have the final merged linked list, current next should continue to point to the
        #linked list which was longer in lenght meaning they will be NOT None now
        current.next = list1 if list1 else list2
        return temp.next
    

if __name__ == '__main__':
    l1 = ListNode(1, ListNode(2, ListNode(4)))
    l2 = ListNode(1, ListNode(3, ListNode(4)))
    
    o = (mergeTwoLists(l1, l2))
    
    while o is not None:
        print(o.val, end =" ")
        o = o.next
    
    
    
    
    
    


    

        




        
        