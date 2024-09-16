class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        # Sort time points
        timePoints.sort()
        min_diff = sys.maxsize  # Initialize to a large value

        def get_minutes(time: str) -> int:
            hr, mn = map(int, time.split(":"))
            return hr * 60 + mn

        # Compare consecutive time points
        for i in range(1, len(timePoints)):
            curr_time = get_minutes(timePoints[i])
            prev_time = get_minutes(timePoints[i - 1])
            diff = curr_time - prev_time
            min_diff = min(min_diff, diff)

        # Circular comparison (first and last)
        first_time = get_minutes(timePoints[0])
        last_time = get_minutes(timePoints[-1])
        circular_diff = (24 * 60 - last_time) + first_time
        min_diff = min(min_diff, circular_diff)
        return min_diff