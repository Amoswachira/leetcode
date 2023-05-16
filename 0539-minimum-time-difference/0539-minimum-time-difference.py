class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        def convert(time):
            hh, mm = time.split(':')
            return int(hh) * 60 + int(mm)

        time_slots = [False] * 1440
        start, end = 1440, -1
        for time in timePoints:
            minutes = convert(time)
            if time_slots[minutes]:
                return 0

            time_slots[minutes] = True
            start = min(start, minutes)
            end = max(end, minutes)

        prev, res = start, start - end + 1440
        for curr in range(start + 1, end + 1):
            if not time_slots[curr]:
                continue

            res = min(res, curr - prev)
            prev = curr

        return res
        