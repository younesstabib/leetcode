class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        mergedList = ListNode()
        currentList = mergedList

        while list1 and list2:
            if list1.val < list2.val:
                currentList.next = list1
                list1 = list1.next
            else:
                currentList.next = list2
                list2 = list2.next
            currentList = currentList.next
        
        if list1:
            currentList.next = list1
        else:
            currentList.next = list2
        
        return mergedList.next