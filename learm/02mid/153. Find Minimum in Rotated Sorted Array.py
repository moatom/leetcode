# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/description/?envType=problem-list-v2&envId=xo2bgr0r
# 両側inclusiveで統合のつかない例外パターン

def findMin(nums):
    left, right = 0, len(nums) - 1
    while left < right:
        mid = (left + right) // 2
        if nums[mid] > nums[right]: # midは範囲を麦側に抜けている
            left = mid + 1 # 左を大きく
        else:
            right = mid # rightをinclusiveに縮める。midを含むのがポイント。left=rightでループを止めたい。
    return nums[left]  # or nums[right] ## NUMSの値を返すのに注意！！！

'''
def findMin(nums):
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2

        # 1. 端がすでにソートされている → leftが最小
        if nums[left] <= nums[right]:
            return nums[left]

        # 2. mid の右側が乱れてる → 最小値は右側
        if nums[mid] >= nums[left]:
            left = mid + 1
        else:
            right = mid
    return nums[left]
'''

'''
🔶 1. 問題の要約（最初に面接官と共通認識）
「ソートされた昇順の配列があるんですが、それがあるところで回転されています。
この回転された配列の中から、最小値を O(log n) 時間で見つけてください。」
例：
Input:  [4,5,6,7,0,1,2]
Output: 0

🔶 2. 制約・前提
    要素は 昇順にソートされた配列を回転したもの（回転回数は不明）
    要素は すべてユニーク
    線形探索は不可（O(n)）→ 二分探索で O(log n) を狙う

🔶 3. 問題の構造（直感と観察）
    通常の昇順配列：[1, 2, 3, 4, 5] → 最小値は nums[0]
    回転された配列：[3, 4, 5, 1, 2] → 最小値は「回転点」
観察：
    回転されていると、「1か所だけ順序が崩れている」場所があり、そこが最小値。
    → つまり、「配列の一部が通常の昇順だが、他の部分で折れている」

🔶 4. 二分探索で解ける理由
「探索範囲の中央（mid）の値が、どちらのソートされた区間にいるかで判断できる」から。
👇 具体的には：
    nums[mid] > nums[right] のとき：
        最小値は右側にある（mid も含まない）
        → left = mid + 1

    nums[mid] <= nums[right] のとき：
        最小値は左側にある（mid は候補になる）
        → right = mid

🔶 5. 擬似コード（口頭で書きながら説明）
left = 0
right = len(nums) - 1
while left < right:
    mid = (left + right) // 2
    if nums[mid] > nums[right]:
        left = mid + 1
    else:
        right = mid

return nums[left]

🔶 6. なぜ正しいか（思考の深掘り）

    ループ終了時に left == right
    その位置が、最小値を指す唯一の場所
    各ステップで範囲を半分に絞っている → O(log n)

🔶 7. 面接官から聞かれそうなことへの備え
質問	答え
Q. ソートされていない場合は？	解けません。ソート前提が必要です。
Q. 重複がある場合は？	ロジックが変わります（>= や <= の境界が曖昧になるため）。別の実装が必要です。
Q. 最小値が末尾にあるときは？	問題ありません。条件分岐でしっかり見つけられます。

🔶 8. 実装Tips（コード上の注意）
    left < right で回すと、ループ後に left == right → nums[left] が答え
    nums[mid] > nums[right] という比較は、右半分が無秩序かどうかの判定に使う

🧠 最後に一言でまとめ
「この問題は、回転によって生じた不連続点（回転点）を、二分探索で検出する構造です。
midとrightの関係を見ることで、回転点の側を特定し、範囲を狭めていくことで O(log n) で最小値を見つけられます。」
'''
