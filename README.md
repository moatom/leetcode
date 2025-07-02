# leetcode
leetcode

- https://leetcode.com/studyplan/top-interview-150/
- https://leetcode.com/explore/interview/card/top-interview-questions-medium/
- https://leetcode.com/problem-list/oizxjoit/


```bash
make new-<project name>
```

- https://github.com/Shunpoco/leetcode
- https://note.com/swe1/n/n67b2b6a45960#cf521b4a-5ffc-43d4-ac4d-1930864da77a
- https://qiita.com/baby-degu/items/fdc362d2d9e58d54e53f#2-%E3%82%B3%E3%83%BC%E3%83%87%E3%82%A3%E3%83%B3%E3%82%B0%E3%81%A8%E5%AD%A6%E7%BF%92%E3%83%97%E3%83%A9%E3%83%83%E3%83%88%E3%83%95%E3%82%A9%E3%83%BC%E3%83%A0
- https://nodchip.hatenadiary.org/entry/2023/03/03/205125#Google-%E3%81%AE%E9%9D%A2%E6%8E%A5%E3%81%AE%E8%A9%95%E4%BE%A1%E5%9F%BA%E6%BA%96%E3%81%A8%E5%AF%BE%E7%AD%96%E6%96%B9%E6%B3%95


# 雑テクニック集

- [./BinSearch.md](./BinSearch.md)

https://leetcode.com/problems/house-robber/description/?envType=problem-list-v2&envId=xo2bgr0r
```python
class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1: # i>2を仮定しているので、例外処理が必要。先にテンプレで雑に処理すると忘れやすいので、確実に処理すべき。
            return nums[0]

        dp = [0 for _ in range(n)]
        dp[0] = nums[0]
        dp[1] = max(nums[1], nums[0])

        for i in range(2, n):
            dp[i] = max(dp[i-1], dp[i-2]+nums[i]) # nums[i]が重要

        return dp[n-1]
```

https://leetcode.com/problems/unique-email-addresses/description/?envType=problem-list-v2&envId=xo2bgr0r
```python
local, domain = email.split('@')
local = local.split('+')[0].replace('.', '')
normalized_email = local + '@' + domain
unique.add(normalized_email)

# ---

local_name, domain_name = email.split('@')

# +
i = local_name.find('+')
if i != -1:
    local_name = local_name[:i]

# .
local_name = ''.join([s for s in list(local_name) if s != '.'])

uniq_mails.add((local_name, domain_name))
```

https://leetcode.com/problems/intersection-of-two-arrays/description/?envType=problem-list-v2&envId=xo2bgr0r
```python
def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
    a = set(nums1)
    b = set(nums2)
    ans = []
    for x in b:
        if x in a:
            ans.append(x)
    return ans

---

    return list(set(nums1) & set(nums2))

---

def intersection(nums1, nums2):
    nums1.sort()
    nums2.sort()

    i = j = 0
    result = set()

    while i < len(nums1) and j < len(nums2):
        if nums1[i] == nums2[j]:
            result.add(nums1[i])
            i += 1
            j += 1
        elif nums1[i] < nums2[j]:
            i += 1
        else:
            j += 1

    return list(result)

---

class Solution:
    def intersection(self, nums1, nums2):
        set1 = set(nums1)
        result = set()
        for num in nums2:
            if num in set1:
                result.add(num)
        return list(result)

```

https://leetcode.com/problems/max-area-of-island/?envType=problem-list-v2&envId=xo2bgr0r
```python
def dfs(r, c):
    if r < 0 or r >= rows or c < 0 or c >= cols:
        return 0
    if grid[r][c] == 0:
        return 0

    grid[r][c] = 0  # 訪問済にする
    area = 1

    for dr, dc in [(1,0), (-1,0), (0,1), (0,-1)]:
        area += dfs(r + dr, c + dc)

    return area

# ---

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # rc, rc, rc
        row = len(grid)
        col = len(grid[0])

        def dfs(i, j):
            if 0 <= i < row and 0 <= j < col and grid[i][j] == 1:
                grid[i][j] = 0
                dfs(i-1, j)
                dfs(i+1, j)
                dfs(i, j-1)
                dfs(i, j+1)
                return True
            return False

        cnt = 0
        for r in range(row): # range!!
            for c in range(col):
                if dfs(r, c):
                    cnt += 1
        return cnt
```

https://leetcode.com/problems/unique-paths-ii/description/?envType=problem-list-v2&envId=xo2bgr0r
```python
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        r = len(obstacleGrid)
        c = len(obstacleGrid[0])
        dp = [[0 for _ in range(c)] for _ in range(r)]


        for j in range(c):
            if obstacleGrid[0][j] == 1:
                break
            dp[0][j] = 1
        for i in range(r):
            if obstacleGrid[i][0] == 1:
                break
            dp[i][0] = 1

        for i in range(1,r):
            for j in range(1,c):
                if obstacleGrid[i][j] != 1:
                    dp[i][j] = dp[i][j-1] + dp[i-1][j]
                else:
                    dp[i][j] = 0 # いらない。

        return dp[r-1][c-1]

# ---

def uniquePathsWithObstacles(obstacleGrid):
    m, n = len(obstacleGrid), len(obstacleGrid[0])
    dp = [[0] * n for _ in range(m)]

    # 初期位置に障害物があれば経路ゼロ
    if obstacleGrid[0][0] == 1:
        return 0
    dp[0][0] = 1

    # 1行目
    for j in range(1, n):
        if obstacleGrid[0][j] == 0 and dp[0][j-1] == 1:
            dp[0][j] = 1

    # 1列目
    for i in range(1, m):
        if obstacleGrid[i][0] == 0 and dp[i-1][0] == 1:
            dp[i][0] = 1

    # 残りのマス
    for i in range(1, m):
        for j in range(1, n):
            if obstacleGrid[i][j] == 0:
                dp[i][j] = dp[i-1][j] + dp[i][j-1]

    return dp[m-1][n-1]

# ---

dp = [[0] * n # ここは0のコピー
for _ in range(m) # リストはshallowコピーになるので、回避するために逐次生成
]
```


https://leetcode.com/problems/remove-duplicates-from-sorted-list/description/?envType=problem-list-v2&envId=xo2bgr0r
```python
def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
    current = head

    while current:
        no_dup = current
        dup_elem = current.val
        while no_dup and no_dup.val == dup_elem: # skip to no dup
            no_dup = no_dup.next

        current.next = no_dup
        current = no_dup

    return head

# ---

def deleteDuplicates(head):
    current = head
    while current and current.next:
        if current.val == current.next.val:
            current.next = current.next.next  # 重複を飛ばす (まだ、current自体の更新操作はしない)
        else:
            current = current.next
    return head
```
