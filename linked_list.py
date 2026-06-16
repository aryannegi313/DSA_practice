class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def createLL(arr):
    if not arr:
        return
    head = ListNode(arr[0])
    curr = head
    
    for i in range(1,len(arr)):
        curr.next = ListNode(arr[i])
        curr = curr.next
    
    return head

def printLL(head):
    if not head:
        print("NONE")
    curr = head
    
    while curr:
        print(curr.val, end=" -> ")
        curr = curr.next
    print("None")

def reverseLL(head):
    if not head:
        return
    curr = head
    prev = None
    while curr:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt
    
    return prev
        

head = createLL([1,2,3,4,5])
rev_head = reverseLL(head)
printLL(rev_head)