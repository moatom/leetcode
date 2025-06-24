# https://leetcode.com/problems/linked-list-cycle-ii/?envType=problem-list-v2&envId=xo2bgr0r
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow_p = fast_p = head

        while fast_p and fast_p.next:
            slow_p = slow_p.next
            fast_p = fast_p.next.next

            if slow_p == fast_p:
                ptr = head
                while ptr != slow_p:
                    ptr = ptr.next
                    slow_p = slow_p.next
                return ptr

        return None

'''
https://qiita.com/KHitoshi/items/17e71b6c1d34003f2ecf#%E8%A9%B3%E7%B4%B0

🧠 数式と距離の説明
距離の定義：
    a = head から cycle の開始点までの距離
    b = cycle 開始点から交差点までの距離
    c = cycle の残りの長さ（b + c = C, サイクルの長さ）

head →→→ a →→→ cycle_start →→→ b →→→ meeting_point
                        ↑                        ↓
                        ←←←←←←←←←←←←←←←←←←←←←←←←←←
                                     c

出会うときの距離：

    slow は a + b 進んでいる
    fast は 2(a + b) 進んでいる
    fast は余分に nC（サイクルを何周か）している：

2(a + b) = a + b + nC
→ a + b = nC
→ a = nC - b

🎯 重要な結論
    サイクルの開始点は、交差点から c = C - b だけ先にある。
    そして、head から a だけ進めば同じ位置に着く。

だから：
    一方を head から（距離 a）
    一方を 交差点 から（距離 c = C - b = nC - b mod C）
で動かすと 同時にサイクルの開始点に着く！

---
slow = a+b
fast = a+b+n(b+c) (n>=1)

2(a+b) = a+b+n(b+c)
a+b = n(b+c)
a = c + (n-1)(b+c)
→headとbから等速で進むポインタは、衝突開始点で出会う。(b側は複数周余計にしている可能性がある)
'''