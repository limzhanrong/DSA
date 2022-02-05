import heapq
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        if len(lists) == 1:
            return lists[0]
        mid = len(lists) // 2
        l, r = self.mergeKLists(lists[:mid]), self.mergeKLists(lists[mid:])
        return self.merge(l, r)
    def merge(self, l1, l2):
        curr = dummy = ListNode()
        while l1 and l2:
            if l1.val < l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next
            curr = curr.next
        curr. next = l1 or l2
        return dummy.next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        curr = dummy = ListNode()
        minHeap = []
#       O(NLogN): 0(N) for iteration, O(Log(N)) for heap push
        for l in lists:
            while l:
                heapq.heappush(minHeap, l.val)
                l = l.next
#       O(NLogN): 0(N) for iteration, O(Log(N)) for heap push
        while minHeap:
            curr.next = ListNode(heapq.heappop(minHeap))
            curr = curr.next
            
        return dummy.next