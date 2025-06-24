# https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/?envType=problem-list-v2&envId=xo2bgr0r
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy_head = ListNode(0, head) # headにつないでおいて、elseのcurr代入で既存の連結をそのまま利用して進める
        prev = dummy_head
        curr = head

        while curr:
            if curr.next and curr.val == curr.next.val:
                dup = curr.val
                while curr and curr.val == dup: # ここでもcurrの存在保証が必要
                    curr = curr.next
                prev.next = curr # temp
            else:
                prev = curr # proceed
                curr = curr.next

        return dummy_head.next