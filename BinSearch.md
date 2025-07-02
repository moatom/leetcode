## Bin Search

- ✅ 左閉右開 [left, right): 一番安全で一般的
  - lower_bound / upper_bound 系
  - 境界（最初・最後）を探す問題
  - Peak Finding のように mid+1 を安全に参照したい場合
- ✅ 左閉右閉 [left, right]: 必要に応じて使う
  - 値そのものを返したいとき（探索対象がインデックスではなく要素）
  - 「見つかったら return mid、なければ -1」型の探索
  - Binary Search Tree、Mountain Array の max 値探索など

| 型                        | 特徴                    | 典型用途                              |
| ------------------------ | --------------------- | --------------------------------- |
| **\[left, right)**（左閉右開） | 条件を満たす最小・最大のインデックスを探す | 境界探索（lower\_bound / upper\_bound） |
| **\[left, right]**（左閉右閉） | 値を「見つけたら即 return」したい  | 単純な値探索や、ターゲットが複数ある場合の端の探索         |

前者はロジックを使い回せる。
```python
def binary_search(nums, target, condition):
    left, right = 0, len(nums)
    while left < right:
        mid = (left + right) // 2
        if condition(nums[mid]):
            right = mid
        else:
            left = mid + 1
    return left
```

後者は==を使って「一致したら即座に結果を更新して再帰する or 拡張する」というロジックになることが多いため、問題ごとに書き分けが必要になりがち。
```python
def binary_search(nums, target, condition):
left, right = 0, len(nums) - 1
    while left <= right: # <のパターンも有る。このときは、right = midにして、統合成立で止める。
        mid = (left + right) // 2
        if nums[mid] == target : # `condition(nums[mid]), nums[mid]<nums[mid + 1]`なども有る
          pass
        else: nums[mid] < target :
          left = mid + 1
        else:
          right = mid - 1 # midから右側ではなかった場合。midを等号で見た場合は、除外することがおおい。
    return 
```

# https://leetcode.com/problems/search-insert-position/description/
```python
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) # left inclusive

        while l<r:
            m = (l+r)//2
            if target == nums[m]:
                return m
            elif target < nums[m]:
                r = m
            else:
                l = m+1
        return l
```

# https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/?envType=problem-list-v2&envId=xo2bgr0r
```python
class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def canShip(cap): # このcapでdays以内のship可能かを検査
            d = 1
            total = 0
            for w in weights:
                if total+w>cap: # 総量がcapを超えるタイミングで別日へ
                    d += 1
                    total = 0
                total += w
            return d <= days # equal

        l,r = max(weights), sum(weights) # region
        while l<r:
            mid = (l+r)//2
            if canShip(mid): # ship可能な最小のcapを求めたい
                r = mid
            else:
                l = mid+1
        return l # l==rで修了
```

# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/description/?envType=problem-list-v2&envId=xo2bgr0r　（LeetCode 153. Find Minimum in Rotated Sorted Array）
# 
```python
# ✅ 実装（左閉右開 [left, right) バージョン）
def findMin(nums):
    left, right = 0, len(nums)
    while left < right - 1:
        mid = (left + right) // 2
        if nums[mid] > nums[-1]:
            left = mid  # 最小値は右側にある
        else:
            right = mid  # 最小値を含む左側へ
    return nums[left]

# ✅ 実装（左閉右閉 [left, right] バージョン）：両側inclusiveで統合のつかない例外パターン
def findMin(nums):
    left, right = 0, len(nums) - 1
    while left < right:
        mid = (left + right) // 2
        if nums[mid] > nums[right]: # midは範囲を麦側に抜けている
            left = mid + 1 # 左を大きく
        else:
            right = mid # rightをinclusiveに縮める。midを含むのがポイント。left=rightでループを止めたい。
    return nums[left]  # or nums[right] ## NUMSの値を返すのに注意！！！
```

# https://leetcode.com/explore/interview/card/top-interview-questions-medium/110/sorting-and-searching/802/ https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/description/
```python
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def serach(isHigh):
            l = 0
            r = len(nums)-1

            bound = -1
            while l<=r:
                m = (l+r)//2
                if nums[m] < target: # exist in right
                    l = m+1
                elif nums[m] > target: # exist in left
                    r = m-1
                else:
                    bound = m
                    if isHigh:
                        l = m+1
                    else:
                        r = m-1
            return bound
        
        return [serach(False), serach(True)]

def searchRange(nums, target):
    def find_left():
        left, right = 0, len(nums)
        while left < right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid
        return left

    def find_right():
        left, right = 0, len(nums)
        while left < right:
            mid = (left + right) // 2
            if nums[mid] <= target:
                left = mid + 1
            else:
                right = mid
        return left

    l = find_left()
    if l == len(nums) or nums[l] != target: # 見つからない場合にlen(nums)や別のtargetになるので。
      return [-1, -1]
    r = find_right() - 1
    return [l, r]
```
| 機能名              | Python (`bisect`)           | C++ STL            | 説明                          |
| ---------------- | --------------------------- | ------------------ | --------------------------- |
| **lower\_bound** | `bisect.bisect_left(a, x)`  | `std::lower_bound` | 配列内で **`x` 以上** の最初の位置を返す   |
| **upper\_bound** | `bisect.bisect_right(a, x)` | `std::upper_bound` | 配列内で **`x` より大きい** 最初の位置を返す |


# 🧠 二分探索の inclusive / exclusive パターンまとめ

## ✅ 用語

| 用語        | 意味         | 表記例      |
|-------------|--------------|-------------|
| inclusive   | 境界を含む   | `[left, right]` |
| exclusive   | 境界を含まない | `[left, right)` |

---

## 🔷 二分探索の主な範囲パターン

| 範囲            | 初期値               | ループ条件        | 特徴                            |
|------------------|------------------------|---------------------|---------------------------------|
| `[left, right)`  | `left = 0`, `right = n`| `while left < right`| 安全で一般的。`mid+1`も安全。   |
| `[left, right]`  | `left = 0`, `right = n-1`| `while left <= right`| `==` 判定に向いている。      |

---

## 🔍 判断ガイドライン

| 探索目的                    | 推奨パターン   | 理由                                       |
|-----------------------------|----------------|--------------------------------------------|
| 境界を探す（最初/最後）      | `[left, right)` | 空区間が `left == right` で統一できる         |
| 要素の存在確認（`==`）      | `[left, right]` | `mid` でそのまま return できる               |
| `mid + 1` を参照する必要がある | `[left, right)` | 範囲外アクセスを避けられる                   |
| 解空間（二値探索）          | `[left, right)` | 条件を満たす最小/最大を見つけるのに最適     |

---

## 🔷 `[left, right)`（左閉右開）で書くべき問題

| 問題名 | LeetCode | コメント |
|--------|----------|----------|
| Search Insert Position | [35](https://leetcode.com/problems/search-insert-position) | `lower_bound` 型 |
| Find First and Last Position | [34](https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array) | 2回探索が必要 |
| First Bad Version | [278](https://leetcode.com/problems/first-bad-version) | 初めての失敗を探す |
| Find Peak Element | [162](https://leetcode.com/problems/find-peak-element) | `nums[mid + 1]` を参照 |
| Koko Eating Bananas | [875](https://leetcode.com/problems/koko-eating-bananas) | 解空間の二分探索 |
| Capacity To Ship Packages | [1011](https://leetcode.com/problems/capacity-to-ship-packages-within-d-days) | 同上 |

---

## 🔶 `[left, right]`（左閉右閉）で書くことが多い問題

| 問題名 | LeetCode | コメント |
|--------|----------|----------|
| Binary Search | [704](https://leetcode.com/problems/binary-search) | 最も基本 |
| Search in Rotated Sorted Array | [33](https://leetcode.com/problems/search-in-rotated-sorted-array) | 値の存在確認 |
| Search a 2D Matrix | [74](https://leetcode.com/problems/search-a-2d-matrix) | 同上　↔　[240. Search a 2D Matrix II](https://leetcode.com/problems/search-a-2d-matrix-ii/description/) |
| Search in Mountain Array | [1095](https://leetcode.com/problems/find-in-mountain-array) | ピーク後に検索が必要 |

---

## 🟡 どちらでも書けるが注意が必要な問題

| 問題名 | LeetCode | コメント |
|--------|----------|----------|
| Find Minimum in Rotated Sorted Array | [153](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array) | 書き方次第で両対応 |
| Search in Rotated Sorted Array II | [81](https://leetcode.com/problems/search-in-rotated-sorted-array-ii) | 重複があるため注意 |
| Minimum Days to Make m Bouquets | [1482](https://leetcode.com/problems/minimum-number-of-days-to-make-m-bouquets) | 解空間探索。両方式可 |

---

## 📘 練習に最適なおすすめ問題セット

| レベル | 問題名 | LeetCode |
|--------|--------|----------|
| ★☆☆ | Binary Search | [704](https://leetcode.com/problems/binary-search) |
| ★☆☆ | Search Insert Position | [35](https://leetcode.com/problems/search-insert-position) |
| ★★☆ | Find First and Last Position | [34](https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array) |
| ★★☆ | Find Peak Element | [162](https://leetcode.com/problems/find-peak-element) |
| ★★★ | Search in Rotated Sorted Array | [33](https://leetcode.com/problems/search-in-rotated-sorted-array) |
| ★★★ | Koko Eating Bananas | [875](https://leetcode.com/problems/koko-eating-bananas) |

---
