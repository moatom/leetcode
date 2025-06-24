# https://leetcode.com/problems/merge-k-sorted-lists/description/?envType=problem-list-v2&envId=oizxjoit

'''
1. 分割統治法（Divide and Conquer）
    k個のリストをペアごとにマージしながら段階的に1つのリストにまとめる
    マージ2リストはO(n)
    深さは O(log k)
    全体で O(n log k) 時間
'''
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        interval = 1
        while interval < len(lists):
            for i in range(0, len(lists) - interval, interval * 2):
                lists[i] = self.mergeTwoLists(lists[i], lists[i + interval])
            interval *= 2
        return lists[0]

    def mergeTwoLists(self, l1, l2):
        dummy = ListNode(0)
        tail = dummy
        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next
        tail.next = l1 or l2
        return dummy.next

'''
2. 優先度付きキュー（Heap）を使う
    k個のリストの先頭をヒープに入れておく
    最小のノードを取り出し、それを結果に追加し、取り出したノードの次のノードをヒープに入れる
    全体で O(n log k) 時間
'''
import heapq

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        min_heap = []
        for i, node in enumerate(lists):
            if node:
                heapq.heappush(min_heap, (node.val, i, node))
        dummy = ListNode(0)
        tail = dummy

        while min_heap:
            val, i, node = heapq.heappop(min_heap)
            tail.next = node
            tail = tail.next
            if node.next:
                heapq.heappush(min_heap, (node.next.val, i, node.next))

        return dummy.next

'''
まとめ
方法	        時間計算量	空間計算量	ポイント
分割統治法	  O(n log k)	O(1)	    シンプルで速い
ヒープ利用法	O(n log k)	O(k)	    k個の先頭ノードを管理
'''