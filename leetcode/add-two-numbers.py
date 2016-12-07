# Definition for singly-linked list.


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

#this is a simple high-precision add


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        head = ListNode(None)
        q = head
        carry = 0
        while l1!=None and l2!=None:
            val = l1.val+l2.val+carry
            if (val>=10):
                carry = 1
                val %= 10
            else:
                carry = 0
            p = ListNode(val)
            q.next = p
            q = q.next
            l1 = l1.next
            l2 = l2.next
        if l1 == None and l2 == None:
            if carry == 1:
                q.next = ListNode(1)
            return head.next
        elif l1 == None:
            q.next = l2
        elif l2 == None:
            q.next = l1
        while carry == 1 and q != None:
            if q.next == None:
                q.next = ListNode(0)
            q = q.next
            q.val += 1
            if q.val>=10:
                q.val%= 10
            else:
                carry = 0
        return head.next

a = Solution()


t1 = [2,4,3,2,4,3,2,4,3,2,4,3,2,4,3,2,4,3,2,4,3,2,4,3,2,4,3,2,4,3,2,4,3,2,4,3,2,4,3,2,4,3,2,4,3,2,4,3,2,4,3,2,4,3,2,4,3,2,4,3,9]

t2 = [5,6,4,2,4,3,2,4,3,2,4,3,2,4,3,2,4,3,2,4,3,2,4,3,2,4,3,2,4,3,2,4,3,2,4,3,2,4,3,2,4,3,2,4,3,2,4,3,2,4,3,2,4,3,2,4,3,9,9,9,9]

