# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        if isinstance(x,int):
            self.val=x
            self.next=None
        elif isinstance(x,list):
            self.val=x[0]
            self.next=None
            cur=self
            for i in x[1:]:
                cur.next=ListNode(i)
                cur=cur.next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        if isinstance(l1,list):
            l1=ListNode(l1)
            l2=ListNode(l2)

        #记录头结点
        re=ListNode(0)
        r=re

        #进位值
        carry=0
        while (l1 or l2):
            a=l1.val if l1 else 0
            b=l2.val if l2 else 0
            s=carry+a+b
            carry=s//10
            r.next=ListNode(s%10)
            r=r.next
            if l1!=None:
                l1=l1.next
            if l2!=None:
                l2=l2.next
        if carry>0:
            r.next=ListNode(1)
        return re.next
