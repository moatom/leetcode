# https://leetcode.com/problems/maximum-product-subarray/description/?envType=problem-list-v2&envId=oizxjoit
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return 0

        curr_max = curr_min = global_max = nums[0]

        for i in range(1, len(nums)):
            num = nums[i]

            # 一時保存しないと curr_min が更新されてしまう
            temp_max = max(num, curr_max * num, curr_min * num)
            temp_min = min(num, curr_max * num, curr_min * num)

            curr_max, curr_min = temp_max, temp_min
            global_max = max(global_max, curr_max)

        return global_max

'''
定数個の変数で状態を持つ「状態圧縮DP」
---

🔷 1. 状態圧縮DP（Compressed Dynamic Programming）
✅ 定義：
    通常のDP配列（dp[i]）を使わず、過去の計算状態を定数個の変数で持って進めるDP。
✅ キーワード：
    「過去の状態を利用」
    「明示的な遷移式がある」
    配列を使わず、curr / prev / global_max のような変数で済ませる
✅ 代表例：
問題	                                状態圧縮の内容
53. Maximum Subarray	                curr_sum = max(num, curr_sum + num)（最大和）
152. Maximum Product Subarray	        curr_max, curr_min を使って符号反転を考慮したDP
121. Best Time to Buy and Sell Stock	min_price を保持しつつ max_profit 更新

🔷 2. Greedy（貪欲法）
✅ 定義：
    各ステップで局所的に最適な選択をすることで、最終的にも全体最適に至ると仮定して解く。
✅ キーワード：
    「後のことを考えず、今ベストな選択をとる」
    「構築的アプローチ」
    解が一意であるとは限らない

✅ Greedy で解けるのはどんなとき？
    局所最適 → 全体最適が保証される構造（例：貪欲選択性、最適部分構造）

✅ 代表例：
問題	                                  直感的な戦略
435. Non-overlapping Intervals	        終了時間が早い順に区間を「選ぶ」
452. Minimum Arrows to Burst Balloons	  風船を重ならないように貪欲に打つ
122. Best Time to Buy and Sell Stock II	価格が上がっているなら売買して利益を稼ぐ（未来を考えない）

🔷 3. スライディングウィンドウ（Sliding Window）
✅ 定義：
    配列などの部分範囲（ウィンドウ）を動かしながら、効率的に条件を満たす区間を求める手法。
✅ キーワード：
    「可変長 or 固定長の区間を持ち、左右のポインタで動かす」
    「部分配列・区間和・条件満たす区間系に強い」
    配列全体をスキャンせずに、O(n)で部分情報を得る
✅ 代表例：
問題	                           ウィンドウ操作
209. Minimum Size Subarray Sum	和がtarget以上になる最小長の連続部分列
3. Longest Substring Without    Repeating Characters	一意な文字列の最大長
76. Minimum Window Substring	  必要な文字を全て含む最小のウィンドウ

✅ では、どう区別する？
🧭 判断のための比較表
項目	          状態圧縮DP	                Greedy	                   スライディングウィンドウ
局所 or 全体	  局所最適を記録して全体最適へ	毎回局所最適を選び全体最適を仮定	条件満たす区間を動的に更新
「状態」を持つ？	✅（例：max/minを追跡）	    ❌（持たない or 即決）	      ✅（ウィンドウ内の情報を保持）
明示的な遷移式	  ✅（再帰・帰納関係あり）	    ❌（再利用しない）	            ⭕（状態更新式がある場合も）
適用対象	      積や和、条件付きの最大最小など	区間選択やスケジューリング	  部分列・部分配列に関する最適化
例で考えると？  	最大部分積、最大部分和	      区間スケジュール、株売買	    条件付き部分和、ユニーク文字列

🧠 判断クイズ！
問題	                          どの手法？	            理由（簡単に）
53. Maximum Subarray	          状態圧縮DP	           dp[i] = max(nums[i], dp[i-1] + nums[i]) を変数で保持
435. Non-overlapping Intervals	Greedy	               局所的に「終了が早い」区間を選ぶと全体も最適になる
209. Min Size Subarray Sum	    スライディングウィンドウ	区間和が条件を満たすまで right を動かし、縮める

🧠 総まとめ：コードが似ていても、本質は違う！
キーワードで思い出す！
✅ DP：状態遷移 + 再利用（状態が定義されている）
✅ Greedy：今がベスト！（一歩一歩即決）
✅ Sliding Window：部分区間をずらす（連続性の活用）
'''