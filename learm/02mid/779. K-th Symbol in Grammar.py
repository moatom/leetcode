# https://leetcode.com/problems/k-th-symbol-in-grammar/description/?envType=problem-list-v2&envId=xo2bgr0r
# 0, 01, 0110, 01101001, 0110100110010110, ...
# x + ^(x, 0xFFFFFF...)
# x = x + (~x & 0b11111111) # 2の補数なので、64bit反転とかに補正されるので、無視しないとだめ
# f x = f x//2 + ~f x//2

class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        if n == 1:
            return 0
        parent = self.kthGrammar(n-1, (k+1)//2)
        is_k_even = k%2 == 0
        if is_k_even:
            return 1 - parent
        else:
            return parent

'''
✅ 親と子の関係（例）

行1：[0]
行2：[0, 1]
行3：[0, 1, 1, 0]
行4：[0,1,1,0,1,0,0,1]

この構造は、二分木のように考えられます。
🎯 ポイント：

各 n 行目の k 番目の文字は、n-1 行目の (k+1)//2 番目の文字の子になります。
✅ だから：
    k が 奇数 → 親の左の子（= 親と同じ）
    k が 偶数 → 親の右の子（= 親の反転）
⇒全体の左右ではなく、0,1の置き換えにおいて「左が同じ、右が反転」が重要。

---
✅ 実装のコアロジック（まとめ）
kの位置	親の位置 k'	子は？
奇数	(k+1)//2	親と同じ
偶数	(k+1)//2	親の反転

---

a_row = ['0']
for _ in range(1,n):
    for i in range(len(a_row)):
        x = a_row[i]
        if x == '0':
            a_row[i] = '01'
        elif x == '1':
            a_row[i] = '10'

    a_row = list(''.join(a_row))
return int(''.join(a_row)[k-1])

---

✅ 方法①：ビット演算による O(log k) 解法
🧠 観察ポイント
    何回「反転」したかが重要。
    k の 2進数表現の中にある 1 の数（popcount）が、**親からの「反転回数」**を表します。

🔁 結論
    k-1 の 2進数における 1 の個数（bit count）が偶数 → 0
    奇数 → 1

これは、k-1 の生成過程において何回「右側（=反転）」に降りたかを示します。

def kthGrammar(n, k):
    return bin(k - 1).count('1') % 2

def kthGrammar(n, k):
    return (k - 1).bit_count() % 2

---

from functools import cache

@cache
def kthGrammar(n, k):
    if n == 1:
        return 0
    parent = kthGrammar(n - 1, (k + 1) // 2)
    if k % 2 == 0:
        return 1 - parent
    else:
        return parent

---
@lru_cache	Python 3.2〜	最も広く使われていた。LRU（最近使ってない順に削除）方式のキャッシュ。
キャッシュサイズを指定できる。
@cache	Python 3.9〜	@lru_cache(maxsize=None) のシンプル版。
制限なし・高速。
'''
