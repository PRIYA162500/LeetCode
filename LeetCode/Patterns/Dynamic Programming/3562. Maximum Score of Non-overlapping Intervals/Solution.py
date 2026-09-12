from bisect import bisect_left

class Solution(object):
    def maximumWeight(self, intervals):
        n = len(intervals)

        # Store: (end, start, weight, original_index)
        arr = []
        for i, (l, r, w) in enumerate(intervals):
            arr.append((r, l, w, i))

        # Sort by ending point
        arr.sort()

        # Ends of sorted intervals
        ends = [x[0] for x in arr]

        # dp[i][k] = (maximum_score, lexicographically_smallest_indices)
        dp = [[(0, ()) for _ in range(5)] for _ in range(n + 1)]

        for i in range(1, n + 1):

            r, l, w, idx = arr[i - 1]

            # Find number of previous intervals having:
            # previous_end < current_start
            p = bisect_left(ends, l, 0, i - 1)

            for k in range(5):

                # Option 1: Don't choose current interval
                best = dp[i - 1][k]

                # Option 2: Choose current interval
                if k > 0:
                    prev_score, prev_indices = dp[p][k - 1]

                    candidate_score = prev_score + w
                    candidate_indices = tuple(
                        sorted(prev_indices + (idx,))
                    )

                    candidate = (
                        candidate_score,
                        candidate_indices
                    )

                    # Better score OR same score but lexicographically smaller
                    if (candidate_score > best[0] or
                        (candidate_score == best[0] and
                         candidate_indices < best[1])):

                        best = candidate

                dp[i][k] = best

        # We can choose AT MOST 4 intervals.
        # Find maximum score among 0,1,2,3,4 intervals.
        max_score = max(dp[n][k][0] for k in range(5))

        # Among all solutions with maximum score,
        # return lexicographically smallest indices.
        answer = min(
            dp[n][k][1]
            for k in range(5)
            if dp[n][k][0] == max_score
        )

        return list(answer)
        